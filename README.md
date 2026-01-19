# PEICD100

## 預覽
```
activate mkdocs
mkdocs serve

```
## 每次寫完
```
mkdocs gh-deploy
git add .
git commit -m "PEICD100"
git branch -M main
git push -u origin main

```
# 其他

## 第一次操作
```
conda create -n mkdocs python=3.13 -y
activate mkdocs
git init
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/peicd100/peicd100.github.io.git
conda install pip -y 
pip install -r requirements.txt
git push -u origin main
mkdocs gh-deploy

```
## 初始化
```
git init
git remote add origin https://github.com/peicd100/peicd100.github.io.git

```
## 推送到main
```
git add .
git commit -m "PEICD100"
git branch -M main
git push -u origin main

```
## 推送到網頁
```
mkdocs gh-deploy

```
## 還原成 GitHub 最新資料
```
git fetch origin && git switch main && git reset --hard origin/main && git clean -fd && git status

```
## 查看儲存庫
```
git remote -v

```