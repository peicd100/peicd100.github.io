# 多益600

## 專案用途
批次產生複習檔案：把所有 `<數字>.md` 的 `<span class="tts">` 文字轉成 MP4 影片，支援「一次」與「兩次（每句重複兩次）」模式，輸出到 `產生複習檔案`。目前已優化為共用句子快取、`ffmpeg encoder` 單次掃描、兩次模式重用單句音檔，且在 `--mode both` 時共用同一輪 TTS（不再重複合成第二輪），並加入無效 proxy（`127.0.0.1:9`）自動停用、暫存資料夾建立在 `產生複習檔案/tts_tmp_*` 且流程結束自動刪除，以及自動略過僅標點句子（避免 `No audio was received`）。

## 多益600、mkdocs(conda 環境名稱)
- workspace_root_basename: `多益600`
- ENV_NAME: `mkdocs`

## conda環境完整安裝指令(使用'-y'一次複製安裝)
```bat
call "C:\ProgramData\anaconda3\Scripts\activate.bat" "C:\ProgramData\anaconda3"
conda activate base
conda create -n mkdocs -y python=3.13
conda install -n mkdocs -y -c conda-forge ffmpeg pyside6
conda run -n mkdocs python -m pip install edge-tts
```

## 程式執行指令
### GUI（推薦）
```bat
call "C:\ProgramData\anaconda3\Scripts\activate.bat" "C:\ProgramData\anaconda3"
conda activate base
conda activate mkdocs
python 紀錄.py
```

### CLI（單次執行）
```bat
call "C:\ProgramData\anaconda3\Scripts\activate.bat" "C:\ProgramData\anaconda3"
conda activate base
conda activate mkdocs
python 紀錄.py --workspace . --run-once --rate 1.0 --gap 0.4 --mode both
```

## 打包指令(要打包成完全不依賴環境的.exe，.exe名稱請使用<workspace_root_basename>)
### debug 版（先驗證）
```bat
call "C:\ProgramData\anaconda3\Scripts\activate.bat" "C:\ProgramData\anaconda3"
conda activate base
conda activate mkdocs
pyinstaller --name 多益600 --clean --noconfirm 紀錄.py
```

### noconsole 版
```bat
call "C:\ProgramData\anaconda3\Scripts\activate.bat" "C:\ProgramData\anaconda3"
conda activate base
conda activate mkdocs
pyinstaller --name 多益600 --clean --noconfirm --noconsole 紀錄.py
```

## github 參考指令
### 初始化

```bat
(
echo.
echo # PyInstaller
echo dist/
echo build/
echo user_data/
echo # Python-generated files
echo __pycache__/
echo *.py[oc]
echo build/
echo dist/
echo wheels/
echo *.egg-info
echo # Virtual environments
echo .venv
)>> .gitignore
git init
git branch -M main
git remote add origin https://github.com/peicd100/mkdocs.git
git add .
git commit -m "PEICD100"
git push -u origin main
```

### 例行上傳

```bat
git add .
git commit -m "PEICD100"
git push -u origin main
```

### 還原成Git Hub最新資料

```bat
git rebase --abort || echo "No rebase in progress" && git fetch origin && git switch main && git reset --hard origin/main && git clean -fd && git status
```

### 查看儲存庫

```bat
git remote -v
```

### 克隆儲存庫

```bat
git clone https://github.com/peicd100/mkdocs.git
```




## Filename Rules (2026-02-21)
- Per-item files in the `一次` output folder use `_一次` suffix (example: `4_一次.mp4`).
- Per-item files in the `兩次` output folder use `_兩次` suffix (example: `4_兩次.mp4`).
- Merged file names use range format: `<min>~<max>_一次.mp4` and `<min>~<max>_兩次.mp4`.

## GUI Resource Monitor
- GUI now shows live CPU and GPU utilization bars.
- CPU utilization uses `psutil`.
- GPU utilization uses `nvidia-smi` (NVIDIA driver tool).
- If a source is unavailable, that bar shows `N/A`.
- GPU monitor now uses a short timeout and catches subprocess exceptions, reducing GUI freeze risk.

## GUI Progress Bar
- Progress now estimates total output size before conversion starts.
- It then tracks current converted file size and computes percentage from `current_size / estimated_total_size`.
- The bar displays `百分比 + 目前大小 / 預估總大小`.
- Existing output files from previous runs are excluded until they are rewritten in the current run.
- Progress size scan is throttled with a cache to avoid full rescans on every log message.

## GUI Stop Button
- GUI now provides a `強制停止` button during conversion.
- Clicking it sends a cancellation signal and terminates active ffmpeg subprocesses to stop current conversion quickly.
- A cancelled run shows `已強制停止轉換。` instead of a generic failure dialog.

## Performance Notes (2026-02-21)
- Conversion concurrency is capped (`MAX_FILE_CONCURRENCY=6`) to avoid too many simultaneous jobs causing contention.
- With sentence cache + audio cache + throttled progress scan, runtime behavior is closer to linear in effective workload.
- A manifest file (`產生複習檔案/_convert_manifest.json`) now stores `<數字>.md` 的 `size + mtime_ns + hash` 與設定簽章，先用 `size + mtime_ns` 快速命中，再決定是否重算 hash。
- A sentence cache file (`產生複習檔案/_sentence_cache.json`) persists extracted TTS sentences per file fingerprint to avoid repeated markdown parsing.
- When file fingerprints and options are unchanged and outputs exist, conversion is skipped and existing outputs are reused.

