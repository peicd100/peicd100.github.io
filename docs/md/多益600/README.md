# 多益600

## 專案用途
批次產生複習檔案：把所有 `<數字>.md` 的 `<span class="tts">` 文字轉成 MP4 視頻，支持「一次」和「兩次」（每句重複兩次）兩種模式。輸出到 `產生複習檔案\一次` 或 `產生複習檔案\兩次` 資料夾，每種模式包含 `<數字>.mp4` 和 `全.mp4`。語速可調整，聲音樣式預設為 JennyNeural，包含進度條顯示。

## 專案名稱與環境
- workspace: `多益600`
- ENV_NAME: `mkdocs`（conda）

## conda 環境完整安裝指令
```bat
call "C:\ProgramData\anaconda3\Scripts\activate.bat" "C:\ProgramData\anaconda3"
conda activate base
conda create -n mkdocs -y python=3.13
conda install -n mkdocs -y -c conda-forge ffmpeg pyside6
conda run -n mkdocs python -m pip install edge-tts
```

## 程式執行指令

### 啟動 GUI（推薦）
```bat
call "C:\ProgramData\anaconda3\Scripts\activate.bat" "C:\ProgramData\anaconda3"
conda activate base
conda activate mkdocs
python 紀錄.py
```

### CLI 模式（不開 GUI）：
```bat
call "C:\ProgramData\anaconda3\Scripts\activate.bat" "C:\ProgramData\anaconda3"
conda activate base
conda activate mkdocs
python 紀錄.py --workspace . --run-once --rate 0 --gap 0.4 --mode both
```

參數說明：
- `--rate 0`：語速為 1 倍速（0%），範圍 -100~100
- `--gap 0.4`：每句間隔 0.4 秒
- `--mode both`：同時產生「一次」和「兩次」，或選 `once` / `twice`
- `--voice en-US-JennyNeural`：可指定聲音（預設自動選擇 JennyNeural）

## 打包指令

### Debug 版（帶主控台）
```bat
call "C:\ProgramData\anaconda3\Scripts\activate.bat" "C:\ProgramData\anaconda3"
conda activate base
conda activate mkdocs
pyinstaller --name 紀錄 --clean --noconfirm 紀錄.py
```

### Release 版（無主控台）
```bat
call "C:\ProgramData\anaconda3\Scripts\activate.bat" "C:\ProgramData\anaconda3"
conda activate base
conda activate mkdocs
pyinstaller --name 紀錄 --clean --noconfirm --noconsole 紀錄.py
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

### 更新

```bat
git add .
git commit -m "PEICD100"
git push -u origin main
```

### 強制同步 GitHub

```bat
git rebase --abort || echo "No rebase in progress" && git fetch origin && git switch main && git reset --hard origin/main && git clean -fd && git status
```

### 查詢遠端

```bat
git remote -v
```

### 下載專案

```bat
git clone https://github.com/peicd100/mkdocs.git
```

