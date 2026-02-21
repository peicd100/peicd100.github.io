# AGENTS.md

## 基本原則

1. 第一次對話時，你必須先「從頭到尾完整讀完」本 AGENTS.md（workspace root/AGENTS.md）。不得依賴先前記憶或上次讀取結果；本次任務必須重新完整讀取一次。若你被要求重新閱讀：你必須回到 workspace root/AGENTS.md 重新讀取。
2. 若你沒有得到此檔案，就不需按照此規則。
3. 請全程使用繁體中文
4. 中文請使用 UTF-8
5. 你可以對 conda 環境進行任何安裝與修改，但是不行沒有經過我同意就對系統安裝與修改。
6. 東西盡量都安裝在 conda ，如果你有系統安裝與修改的需求，請先經過我的同意。你最後要跟我說你在哪裡安裝了什麼、修改了什麼，若無安裝也要告知。

## python 專案規則

如果你和我協作 python 專案，你要遵守以下原則

1. 我使用 conda 來管理 python 環境， conda 環境名稱(<ENV_NAME>)請先看REAMDME.md，如果沒有 REAMDME.md 的話請問我。
2. 如用 python 寫 GUI / 介面 / 視窗規則，請使用 PySide，主題色使用 #72e3fd。如需要語音，請使用Microsoft Edge / Azure Neural TTS，英文使用加拿大、美國、英國，英文語音預設 en-US-JennyNeural 。
3. 你使用 conda 的方式可以參考
    ```
    call "<CONDA_BASE>\\Scripts\\activate.bat" "<CONDA_BASE>"
    conda activate base
    conda activate PEICD100
    ```
4. 你執行 python 時應該要盡量使用 conda 來執行
5. 你每次對我的專案修改都需要維護 "README.md" 、 ".gitignore"
6. 我請你幫我打包時，請你先打包成 debug 版測試是否可以執行，再打包成 noconsole 。

## 每次你進行修改，都要依照以下格式對 README.md 維護。

1. 第一行必須為：# <workspace_root_basename>
2. 專案用途
3. <workspace_root_basename>、<ENV_NAME>(conda 環境名稱)。
4. conda環境完整安裝指令(使用'-y'一次複製安裝)
5. 程式執行指令
6. 打包指令(要打包成完全不依賴環境的.exe，.exe名稱請使用<workspace_root_basename>)
7. github 參考指令(完全照貼以下區塊，但是<ENV_NAME>要換成我的)，後期需要你來維護，像是.gitignore需要幫我修改。
    ### 初始化

    ```
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
    git remote add origin https://github.com/peicd100/<ENV_NAME>.git
    git add .
    git commit -m "PEICD100"
    git push -u origin main
    ```

    ### 例行上傳

    ```
    git add .
    git commit -m "PEICD100"
    git push -u origin main
    ```

    ### 還原成Git Hub最新資料

    ```
    git rebase --abort || echo "No rebase in progress" && git fetch origin && git switch main && git reset --hard origin/main && git clean -fd && git status
    ```

    ### 查看儲存庫

    ```
    git remote -v
    ```

    ### 克隆儲存庫

    ```
    git clone https://github.com/peicd100/<ENV_NAME>.git
    ```



## 硬體規格（供效能取捨參考）

* Windows 11（win-64）
* CPU：Intel Core i9
* GPU：NVIDIA GeForce RTX 4070（12GB VRAM）
* RAM：64GB


## 要求，以下要求須嚴格遵守
