


## GPT 對話

[連結](PEICD - windows 虛擬機.html)

## 配置
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001546-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001549-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001551-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001552-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001554-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001556-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001557-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001559-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001601-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001605-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001607-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001608-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001610-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001612-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001613-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001616-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001617-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001619-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001621-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001623-1.png>)
![alt text](<images/windows虛擬機/螢幕擷取畫面 2026-02-06 001625-1.png>)


## 磁碟更正路徑

![alt text](images/windows虛擬機/image.png)

你這張圖裡，右鍵選單**就有你要的那個**：

### 你要把 Shared Folders 變成「磁碟代號（永久）」

請點右鍵選單裡的 **「連線網路磁碟機…」**（有鏈結圖示那一個）。

接著在跳出的視窗這樣填：

1. **磁碟機代號**：選你想要的（例如 `V:`；你現在已經有 `Z:` 也可以不用改）
2. **資料夾**：輸入
   `\\vmware-host\Shared Folders`
3. 勾選 **「在登入時重新連線」**
4. 完成

---

### 如果你只是想打開它

就點右鍵選單最上面的 **「開啟」**（或直接雙擊那個 `Shared Folders (Z:)`）。

---

### 補一句：你其實已經成功映射成 Z: 了

所以要解你之前 CMD 的 UNC 問題，直接在 CMD 這樣用就行：

1. 輸入 `Z:` 按 Enter
2. 再 `cd` 到你的子資料夾路徑

你現在是想**沿用 Z:** 就好，還是想**改成 V:**？我就照你的選擇給你下一步的最短路徑。







