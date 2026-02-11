# 多益600

## 專案用途
把 `docs\md\多益600` 內所有 `<數字>.md` 的 `<span class="tts">` 文字批次轉成複習 MP4，並額外輸出合併檔 `全.mp4`。每支影片畫面為黑底，中央顯示檔名文字（如 `4`、`5`、`全`）。

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
```bat
call "C:\ProgramData\anaconda3\Scripts\activate.bat" "C:\ProgramData\anaconda3"
conda activate base
conda activate mkdocs
python "docs\md\多益600\轉換.py"
```

CLI 一次轉換（不開 GUI）：
```bat
call "C:\ProgramData\anaconda3\Scripts\activate.bat" "C:\ProgramData\anaconda3"
conda activate base
conda activate mkdocs
python "docs\md\多益600\轉換.py" --workspace "docs\md\多益600" --run-once --rate 0 --gap 0.4
```

## 打包指令
先 debug 測試版：
```bat
call "C:\ProgramData\anaconda3\Scripts\activate.bat" "C:\ProgramData\anaconda3"
conda activate base
conda activate mkdocs
pyinstaller --name 多益600 --clean --noconfirm "docs\md\多益600\轉換.py"
```

再 noconsole 版：
```bat
call "C:\ProgramData\anaconda3\Scripts\activate.bat" "C:\ProgramData\anaconda3"
conda activate base
conda activate mkdocs
pyinstaller --name 多益600 --clean --noconfirm --noconsole "docs\md\多益600\轉換.py"
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

