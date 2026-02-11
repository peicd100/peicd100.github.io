from __future__ import annotations

import argparse
import asyncio
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

import edge_tts


TTS_MARKER = '<span class="tts">'
NUMERIC_MD_PATTERN = re.compile(r"^(\d+)\.md$")
DEFAULT_OUTPUT_DIR_NAME = "產生複習音檔"
DEFAULT_THEME_COLOR = "#72e3fd"
OUTPUT_SAMPLE_RATE = 44100
OUTPUT_CHANNELS = 2
OUTPUT_BITRATE = "128k"
PREFERRED_DEFAULT_VOICES = (
    "en-US-AriaNeural",
    "en-US-JennyNeural",
    "en-US-GuyNeural",
)


class ConversionError(RuntimeError):
    pass


@dataclass
class ConvertOptions:
    voice: str
    rate_percent: int
    gap_seconds: float


def scan_numeric_markdown_files(workspace_root: Path) -> list[Path]:
    files: list[tuple[int, Path]] = []
    for item in workspace_root.iterdir():
        if not item.is_file():
            continue
        match = NUMERIC_MD_PATTERN.match(item.name)
        if match:
            files.append((int(match.group(1)), item))
    files.sort(key=lambda pair: pair[0])
    return [path for _, path in files]


def extract_tts_sentences(md_path: Path) -> list[str]:
    raw = md_path.read_text(encoding="utf-8")
    sentences: list[str] = []
    for line in raw.splitlines():
        if TTS_MARKER not in line:
            continue
        text = line.split(TTS_MARKER, 1)[1]
        text = re.sub(r"<[^>]+>", "", text)
        text = html.unescape(text).strip()
        if text:
            sentences.append(text)
    return sentences


def to_edge_rate(rate_percent: int) -> str:
    rate_percent = max(-100, min(100, int(rate_percent)))
    sign = "+" if rate_percent >= 0 else ""
    return f"{sign}{rate_percent}%"


def locate_binary(name: str) -> Path:
    found = shutil.which(name)
    if found:
        return Path(found)

    suffix = ".exe" if sys.platform == "win32" else ""
    executable = Path(sys.executable).resolve()
    env_root = executable.parent.parent
    candidates = [
        executable.parent / f"{name}{suffix}",
        executable.parent / "Library" / "bin" / f"{name}{suffix}",
        env_root / "Library" / "bin" / f"{name}{suffix}",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise ConversionError(f"找不到 {name} 可執行檔，請先安裝。")


def run_checked(cmd: list[str], cwd: Path | None = None) -> None:
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        cwd=str(cwd) if cwd else None,
    )
    if proc.returncode != 0:
        msg = (
            f"命令失敗（exit={proc.returncode}）:\n"
            f"{' '.join(cmd)}\n"
            f"stdout:\n{proc.stdout}\n"
            f"stderr:\n{proc.stderr}"
        )
        raise ConversionError(msg)


def detect_mp3_encoder(ffmpeg_bin: Path) -> str:
    cmd = [str(ffmpeg_bin), "-hide_banner", "-encoders"]
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if proc.returncode != 0:
        raise ConversionError("無法讀取 ffmpeg encoder 清單。")

    available: set[str] = set()
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line or line.startswith("------"):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        flags, name = parts[0], parts[1]
        if re.fullmatch(r"[A-Z\.]{6}", flags):
            available.add(name)

    for encoder in ("libmp3lame", "mp3_mf", "mp3"):
        if encoder in available:
            return encoder
    raise ConversionError("ffmpeg 找不到可用 MP3 編碼器（libmp3lame/mp3/mp3_mf）。")


def create_silence_mp3(ffmpeg_bin: Path, mp3_encoder: str, duration_sec: float, out_path: Path) -> None:
    cmd = [
        str(ffmpeg_bin),
        "-y",
        "-f",
        "lavfi",
        "-i",
        f"anullsrc=r={OUTPUT_SAMPLE_RATE}:cl=stereo",
        "-t",
        f"{duration_sec:.3f}",
        "-c:a",
        mp3_encoder,
        "-ar",
        str(OUTPUT_SAMPLE_RATE),
        "-ac",
        str(OUTPUT_CHANNELS),
        "-b:a",
        OUTPUT_BITRATE,
        str(out_path),
    ]
    run_checked(cmd)


def write_concat_list(input_files: Iterable[Path], list_file: Path) -> None:
    base_dir = list_file.parent
    lines: list[str] = []
    for input_file in input_files:
        relative = os.path.relpath(str(input_file), str(base_dir))
        escaped = Path(relative).as_posix().replace("'", r"'\''")
        lines.append(f"file '{escaped}'")
    list_file.write_text("\n".join(lines), encoding="utf-8")


def concat_mp3(
    ffmpeg_bin: Path,
    mp3_encoder: str,
    input_files: list[Path],
    out_path: Path,
    list_file: Path,
) -> None:
    if not input_files:
        raise ConversionError("沒有可供串接的音訊檔案。")
    write_concat_list(input_files, list_file)
    cmd = [
        str(ffmpeg_bin),
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(list_file),
        "-c:a",
        mp3_encoder,
        "-ar",
        str(OUTPUT_SAMPLE_RATE),
        "-ac",
        str(OUTPUT_CHANNELS),
        "-b:a",
        OUTPUT_BITRATE,
        str(out_path),
    ]
    run_checked(cmd, cwd=list_file.parent)


def with_gap(items: list[Path], gap_file: Path | None) -> list[Path]:
    if not items:
        return []
    if gap_file is None:
        return list(items)
    result: list[Path] = []
    for idx, item in enumerate(items):
        if idx > 0:
            result.append(gap_file)
        result.append(item)
    return result


async def synthesize_sentence(
    text: str,
    voice: str,
    rate: str,
    out_path: Path,
    retries: int = 1,
) -> None:
    for attempt in range(retries + 1):
        try:
            communicator = edge_tts.Communicate(text=text, voice=voice, rate=rate)
            await communicator.save(str(out_path))
            return
        except Exception:
            if attempt >= retries:
                raise
            await asyncio.sleep(0.4)


async def fetch_voice_choices() -> list[tuple[str, str]]:
    voices = await edge_tts.list_voices()
    choices: list[tuple[str, str]] = []
    for voice in voices:
        short_name = voice.get("ShortName") or voice.get("Name")
        if not short_name:
            continue
        locale = voice.get("Locale", "")
        gender = voice.get("Gender", "")
        label = f"{short_name} | {locale} | {gender}".strip(" |")
        choices.append((label, short_name))
    choices.sort(key=lambda x: x[1])
    return choices


def pick_default_voice(choices: list[tuple[str, str]]) -> str:
    if not choices:
        raise ConversionError("取得 voice 清單失敗。")
    choice_ids = {voice_id for _, voice_id in choices}
    for preferred in PREFERRED_DEFAULT_VOICES:
        if preferred in choice_ids:
            return preferred
    for _, voice_id in choices:
        if voice_id.startswith("en-US-"):
            return voice_id
    return choices[0][1]


async def convert_workspace(
    workspace_root: Path,
    options: ConvertOptions,
    progress: Callable[[str], None] | None = None,
) -> tuple[list[Path], Path, list[str]]:
    progress = progress or (lambda _: None)
    ffmpeg_bin = locate_binary("ffmpeg")
    mp3_encoder = detect_mp3_encoder(ffmpeg_bin)
    markdown_files = scan_numeric_markdown_files(workspace_root)
    if not markdown_files:
        raise ConversionError("找不到任何 <數字>.md 檔案。")

    output_dir = workspace_root / DEFAULT_OUTPUT_DIR_NAME
    output_dir.mkdir(parents=True, exist_ok=True)

    warnings: list[str] = []
    generated_files: list[Path] = []
    rate = to_edge_rate(options.rate_percent)

    progress(f"ffmpeg MP3 編碼器：{mp3_encoder}")
    progress(f"已找到 {len(markdown_files)} 個 .md，開始轉換。")
    with tempfile.TemporaryDirectory(prefix="tts_tmp_", dir=str(output_dir)) as tmpdir:
        tmp_root = Path(tmpdir)
        gap_file: Path | None = None
        if options.gap_seconds > 0:
            gap_file = tmp_root / "gap.mp3"
            progress(f"建立靜音片段：{options.gap_seconds:.2f} 秒")
            create_silence_mp3(ffmpeg_bin, mp3_encoder, options.gap_seconds, gap_file)

        for md_path in markdown_files:
            sentences = extract_tts_sentences(md_path)
            if not sentences:
                warning = f"{md_path.name} 沒有 tts 句子，已略過。"
                warnings.append(warning)
                progress(f"警告：{warning}")
                continue

            progress(f"處理 {md_path.name}（{len(sentences)} 句）")
            part_dir = tmp_root / md_path.stem
            part_dir.mkdir(parents=True, exist_ok=True)
            sentence_audio_files: list[Path] = []

            for idx, sentence in enumerate(sentences, start=1):
                segment = part_dir / f"{idx:04d}.mp3"
                try:
                    await synthesize_sentence(
                        text=sentence,
                        voice=options.voice,
                        rate=rate,
                        out_path=segment,
                        retries=1,
                    )
                except Exception as exc:
                    raise ConversionError(
                        f"{md_path.name} 第 {idx} 句轉換失敗：{exc}"
                    ) from exc
                sentence_audio_files.append(segment)
                if idx % 20 == 0 or idx == len(sentences):
                    progress(f"{md_path.name} 進度 {idx}/{len(sentences)}")

            concat_inputs = with_gap(sentence_audio_files, gap_file)
            output_file = output_dir / f"{md_path.stem}.mp3"
            concat_list_file = part_dir / "concat.txt"
            concat_mp3(ffmpeg_bin, mp3_encoder, concat_inputs, output_file, concat_list_file)
            generated_files.append(output_file)
            progress(f"完成 {output_file.name}")

        if not generated_files:
            raise ConversionError("沒有任何檔案完成轉換，請檢查 .md 內容。")

        all_audio_inputs = with_gap(generated_files, gap_file)
        all_concat_list_file = tmp_root / "concat_all.txt"
        full_output = output_dir / "全.mp3"
        concat_mp3(ffmpeg_bin, mp3_encoder, all_audio_inputs, full_output, all_concat_list_file)
        progress("完成 全.mp3")

    return generated_files, full_output, warnings


def run_once_cli(
    workspace_root: Path,
    voice: str | None,
    rate: int,
    gap: float,
) -> int:
    try:
        choices = asyncio.run(fetch_voice_choices())
        chosen_voice = voice or pick_default_voice(choices)
        options = ConvertOptions(
            voice=chosen_voice,
            rate_percent=rate,
            gap_seconds=max(0.0, gap),
        )
        print(f"使用 voice: {chosen_voice}")
        generated, full_output, warnings = asyncio.run(
            convert_workspace(workspace_root, options, progress=lambda msg: print(msg, flush=True))
        )
        print(f"成功：{len(generated)} 個單檔 + {full_output.name}")
        for warning in warnings:
            print(f"警告：{warning}")
        return 0
    except Exception as exc:
        print(f"失敗：{exc}", file=sys.stderr)
        return 1


def run_gui(workspace_root: Path) -> int:
    from PySide6.QtCore import QObject, QThread, Signal, Slot
    from PySide6.QtWidgets import (
        QApplication,
        QComboBox,
        QDoubleSpinBox,
        QFormLayout,
        QHBoxLayout,
        QLabel,
        QMessageBox,
        QPushButton,
        QPlainTextEdit,
        QSpinBox,
        QVBoxLayout,
        QWidget,
    )

    class ConvertWorker(QObject):
        progress = Signal(str)
        finished = Signal(bool, str, list)

        def __init__(self, root: Path, options: ConvertOptions):
            super().__init__()
            self.root = root
            self.options = options

        @Slot()
        def run(self) -> None:
            try:
                generated, full_output, warnings = asyncio.run(
                    convert_workspace(self.root, self.options, progress=self.progress.emit)
                )
                summary = f"完成轉換：{len(generated)} 個單檔，另含 {full_output.name}"
                self.finished.emit(True, summary, warnings)
            except Exception as exc:
                detail = f"{exc}\n\n{traceback.format_exc()}"
                self.finished.emit(False, detail, [])

    class MainWindow(QWidget):
        def __init__(self, root: Path):
            super().__init__()
            self.workspace_root = root
            self.thread: QThread | None = None
            self.worker: ConvertWorker | None = None

            self.setWindowTitle("多益600 轉換工具")
            self.resize(880, 560)
            self._build_ui()
            self._apply_theme()
            self._load_voices()

        def _build_ui(self) -> None:
            main_layout = QVBoxLayout(self)

            title = QLabel("批次產生複習音檔（<數字>.md → <數字>.mp3 + 全.mp3）")
            main_layout.addWidget(title)

            form = QFormLayout()
            self.voice_combo = QComboBox()
            self.rate_spin = QSpinBox()
            self.rate_spin.setRange(-100, 100)
            self.rate_spin.setValue(0)
            self.rate_spin.setSuffix("%")
            self.gap_spin = QDoubleSpinBox()
            self.gap_spin.setRange(0.0, 10.0)
            self.gap_spin.setDecimals(2)
            self.gap_spin.setSingleStep(0.1)
            self.gap_spin.setValue(0.40)
            self.gap_spin.setSuffix(" 秒")

            form.addRow("聲音樣式", self.voice_combo)
            form.addRow("語速", self.rate_spin)
            form.addRow("每句間隔時間", self.gap_spin)
            main_layout.addLayout(form)

            button_layout = QHBoxLayout()
            self.reload_button = QPushButton("重新載入聲音")
            self.convert_button = QPushButton("轉換")
            self.convert_button.setObjectName("convertButton")
            self.reload_button.clicked.connect(self._load_voices)
            self.convert_button.clicked.connect(self._start_convert)
            button_layout.addWidget(self.reload_button)
            button_layout.addWidget(self.convert_button)
            button_layout.addStretch()
            main_layout.addLayout(button_layout)

            self.status_box = QPlainTextEdit()
            self.status_box.setReadOnly(True)
            main_layout.addWidget(self.status_box)

            self._append_status(f"workspace: {self.workspace_root}")
            self._append_status(f"輸出目錄: {self.workspace_root / DEFAULT_OUTPUT_DIR_NAME}")

        def _apply_theme(self) -> None:
            self.setStyleSheet(
                f"""
                QWidget {{
                    font-size: 13px;
                }}
                QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox, QPlainTextEdit {{
                    border: 1px solid #c6d1d8;
                    border-radius: 6px;
                    padding: 4px;
                }}
                QComboBox:focus, QSpinBox:focus, QDoubleSpinBox:focus, QPlainTextEdit:focus {{
                    border: 1px solid {DEFAULT_THEME_COLOR};
                }}
                QPushButton {{
                    border: 1px solid #9aa7ad;
                    border-radius: 7px;
                    padding: 7px 14px;
                }}
                QPushButton#convertButton {{
                    background: {DEFAULT_THEME_COLOR};
                    border: 1px solid #42bdd8;
                    color: #06323a;
                    font-weight: 700;
                }}
                QPushButton:disabled {{
                    color: #7c8a90;
                    background: #edf2f4;
                }}
                """
            )

        def _append_status(self, message: str) -> None:
            self.status_box.appendPlainText(message)

        def _load_voices(self) -> None:
            self.reload_button.setEnabled(False)
            self._append_status("讀取 voice 清單中...")
            try:
                choices = asyncio.run(fetch_voice_choices())
                self.voice_combo.clear()
                for label, voice_id in choices:
                    self.voice_combo.addItem(label, voice_id)
                default_voice = pick_default_voice(choices)
                idx = self.voice_combo.findData(default_voice)
                if idx >= 0:
                    self.voice_combo.setCurrentIndex(idx)
                self._append_status(f"已載入 {len(choices)} 個聲音。")
            except Exception as exc:
                self._append_status(f"載入 voice 失敗：{exc}")
                QMessageBox.warning(self, "voice 載入失敗", str(exc))
            finally:
                self.reload_button.setEnabled(True)

        def _current_options(self) -> ConvertOptions:
            voice = self.voice_combo.currentData()
            if not voice:
                raise ConversionError("請先選擇聲音樣式。")
            return ConvertOptions(
                voice=str(voice),
                rate_percent=int(self.rate_spin.value()),
                gap_seconds=float(self.gap_spin.value()),
            )

        def _start_convert(self) -> None:
            if self.thread is not None:
                self._append_status("目前已有轉換進行中。")
                return

            try:
                options = self._current_options()
            except Exception as exc:
                QMessageBox.warning(self, "設定錯誤", str(exc))
                return

            self.convert_button.setEnabled(False)
            self.reload_button.setEnabled(False)
            self._append_status(
                f"開始轉換，voice={options.voice}, rate={options.rate_percent}%, gap={options.gap_seconds:.2f}s"
            )

            self.thread = QThread(self)
            self.worker = ConvertWorker(self.workspace_root, options)
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.progress.connect(self._append_status)
            self.worker.finished.connect(self._on_finished)
            self.worker.finished.connect(self.thread.quit)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.finished.connect(self._cleanup_thread)
            self.thread.start()

        @Slot(bool, str, list)
        def _on_finished(self, ok: bool, message: str, warnings: list[str]) -> None:
            self.convert_button.setEnabled(True)
            self.reload_button.setEnabled(True)
            self._append_status(message)
            for warning in warnings:
                self._append_status(f"警告：{warning}")

            if ok:
                if warnings:
                    QMessageBox.information(
                        self,
                        "轉換完成（含警告）",
                        message + "\n\n" + "\n".join(warnings),
                    )
                else:
                    QMessageBox.information(self, "轉換完成", message)
            else:
                QMessageBox.critical(self, "轉換失敗", message)

        @Slot()
        def _cleanup_thread(self) -> None:
            if self.worker is not None:
                self.worker.deleteLater()
            self.thread = None
            self.worker = None

    app = QApplication(sys.argv)
    window = MainWindow(workspace_root)
    window.show()
    return app.exec()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="多益600 Markdown 批次 TTS 轉檔工具")
    parser.add_argument(
        "--workspace",
        default=str(Path(__file__).resolve().parent),
        help="工作目錄（預設為本腳本所在資料夾）",
    )
    parser.add_argument("--run-once", action="store_true", help="不開 GUI，直接執行一次轉換")
    parser.add_argument("--voice", default=None, help="edge-tts voice，例如 en-US-AriaNeural")
    parser.add_argument("--rate", type=int, default=0, help="語速百分比（-100~100）")
    parser.add_argument("--gap", type=float, default=0.4, help="每句間隔秒數（>=0）")
    parser.add_argument("--list-voices", action="store_true", help="列出可用 voice 後離開")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    workspace_root = Path(os.path.abspath(os.path.expanduser(args.workspace)))

    if not workspace_root.exists():
        print(f"workspace 不存在：{workspace_root}", file=sys.stderr)
        return 2

    if args.list_voices:
        try:
            choices = asyncio.run(fetch_voice_choices())
            for label, voice_id in choices:
                print(f"{voice_id}\t{label}")
            return 0
        except Exception as exc:
            print(f"列出 voice 失敗：{exc}", file=sys.stderr)
            return 1

    if args.run_once:
        return run_once_cli(workspace_root, args.voice, args.rate, args.gap)

    return run_gui(workspace_root)


if __name__ == "__main__":
    raise SystemExit(main())
