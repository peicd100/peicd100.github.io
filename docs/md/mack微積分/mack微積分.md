# mack微積分

<!-- # 帳號密碼
x10640305@ycsh 
A13200@ncu

[線上課程](https://learnix.edu.tw/moodle/my/?fbclid=IwAR2e6PCLoDPClVwFYamudFyw5CD-6Trk_9t2usTg8Strxb_3UBDX-6N13-E)

[總攬](https://shann.idv.tw/calculus/ap.html)


[Maple Ta](https://learnix.edu.tw/mapleta/)
 -->
## 易忘記的重點

[無限](#無限)
[曲線間的面積](#曲線間的面積)
[反函數的微分](#反函數的微分)
[chk1-37 微量符號用於估計](#chk1-37微量符號用於估計)
[自然對數的圖形與微分](#自然對數的圖形與微分)

[指對數的微分應用](#指對數的微分應用)

![image](https://hackmd.io/_uploads/SJ1KUhvD6.png)

![image](https://hackmd.io/_uploads/rkN2T2wPp.png)


## 錯題本


### chk1-18 導函數的極限定義
![](https://hackmd.io/_uploads/SJUJQDHxp.png)


## bisection method
[**二分法**是一种根查找算法，适用于任何连续函数，其中已知两个具有相反符号的值。该方法由重复将由这些值定义的区间二分并选择其中函数更改符号的子区间组成，因此必须包含根](https://en.wikipedia.org/wiki/Bisection_method) [1](https://en.wikipedia.org/wiki/Bisection_method)。

[该算法非常简单且稳健，但相对较慢。因此，它通常用于获得粗略的解决方案，然后用作更快收敛方法的起点](https://en.wikipedia.org/wiki/Bisection_method) [1](https://en.wikipedia.org/wiki/Bisection_method)。

以下是二分法的伪代码：

```
输入：函数f、区间[a，b]、容差TOL、最大迭代次数NMAX
输出：近似解p或失败消息
步骤：
1. 如果f（a）* f（b）> = 0，则
    1.1 返回“方法失败：f（a）和f（b）必须具有相反的符号”
2. 让p = a
3. 对于i = 1到NMAX
    3.1 让p =（a + b）/ 2
    3.2 如果f（p）= 0或（b-a）/ 2 <TOL，则
        3.3 返回p
    3.4 如果f（p）* f（a）> 0，则让a = p
    3.5 否则让b = p
4. 返回“方法失败：超过最大迭代次数”

``` 

请注意，这只是二分法的概述，还有许多其他根查找算法可用。

## Maxima
### 輸入：
打入算是之後按下Shift Enter

![](https://hackmd.io/_uploads/HJO9Ghmka.png)
### 四則運算
![](https://hackmd.io/_uploads/r1r0Ghmya.png)
### 引用
可以引用之前得到的答案

![](https://hackmd.io/_uploads/rJym73QJp.png)

### 微分
![](https://hackmd.io/_uploads/BkIjGW6Ja.png)

### 宣告方程式
![](https://hackmd.io/_uploads/rkITfZpJa.png)

### 帶入方程式
![](https://hackmd.io/_uploads/SJ81XZ61a.png)

### 三角函數

![](https://hackmd.io/_uploads/ByG4mbTJT.png)

![](https://hackmd.io/_uploads/rkcP7WpJT.png)

### 展開
![](https://hackmd.io/_uploads/B1d2jdaJp.png)




## Desmos

### 語法
乘法：*
(2*x可寫2x)
除法：/
次方：^
平方根：sqrt(自動轉換為根號

### 使用
#### 一般
![](https://hackmd.io/_uploads/S1J74hQ1p.png)
#### 限制
![](https://hackmd.io/_uploads/HJHsN2XJT.png)
#### 改變顏色
![](https://hackmd.io/_uploads/rywkHhQJp.png)


### 新增滑桿

隨便打個英文

![](https://hackmd.io/_uploads/BkKDH2XJ6.png)

點下可更改值

![](https://hackmd.io/_uploads/ryCxIh7y6.png)

![](https://hackmd.io/_uploads/BkGzLhmya.png)

### 取得座標
要有交點

![](https://hackmd.io/_uploads/rkUvU3Xkp.png)

## 泰勒多項式


將 $ax^2 + bx + c$ 轉換為 $c + b(x - h) + a(x - h)^2$ 的形式為降幂排列！
以 $h$ 為參考點之轉換方法：使用綜合除法計算（右側放 $h$）
計算一個函數為 $y = f(x) = x^3 - 2x^2 + 6$ 他的一階導函數為：

$$
x^3 - 2x^2 + 6
$$






## 多項式函數的局部圖形像直線
若像直線
取0次方以及1次方項，其他捨去
得到一條直線即為局部圖形

## 多項式函數的切線與導數
導數：`f'(x)`
「'」念法：prime

為f(x)之一次微分、一階導函數
意思是帶入x，可以得到在圖上x位置的切線斜率


ps.
`f"(x)`
「"」念法：double prime
為f(x)知二次微分、二階導函數

f^(n)(x)為為f(x)之n次微分、n階導函數

---

舉例：
  f(x)=3X^2
=>f'(x)=6x

f'(x)=6x為一階導函數
帶入不同的x會得到不同斜率
可從點斜式得到直線方程式



----

f'(x)=0 方程式的解
其解可能為臨界點

筆記
![](https://hackmd.io/_uploads/S11_oev1p.png)


![](https://hackmd.io/_uploads/HJGdTxwJa.png)

![](https://hackmd.io/_uploads/BkF56lDkp.png)



## chk1-08 微分與導函數

這邊要講 $f'(x)$、$f'(-1)$ 以及 $[2x^2]'$ 的差異：


$f'(x)$ 是寫出整個多項式，例如：$f'(x) = x^2 + 2x$


$f'(-1)$ 是求出帶進導數的數值，例如：$f'(-1) = 10$


$[2x^2]'$ 是求出導數函數，例如：$[2x^2]' = 4x$


## chk1-10 多項式函數的增減
要計算函數值在某區段的增減
方法：將該位置的x帶入導函數，進而求到斜率
m>0：區域內遞增
m=0：區域極值
m<0：區域內遞減

## chk1-11 相對極值

1. 先微分
2. 讓斜率為0，求出符合之x，此時x為極值
3. 看x加一點、減一點是變多還變少，就可以知道x為區域及大值還是區域極小值進

## chk1-12 當泰勒一次項消失時

這邊要看的是如果拿到的參考點斜率為0，也就是f'(x)=0時，寫成泰勒多項式一次式就會消失了

所以最小的次數為2，如果只取2與0次式，圖形就會與出現極值的函數相似

而這個二次函數我們也可以看成一個二次函數的平移(h、k帶0)

例如：

![](https://hackmd.io/_uploads/Bktg1p7gp.png)
在x=1附近的函數圖形為-2/3+(x-1)^2
也就是x^2向右1，向下2/3

## chk1-13 求多項式極值的一般性方法

求極值就是
1. 先微分
2. 讓斜率為0，求出符合之x，此時x為極值
3. 看x加一點、減一點是變多還變少，就可以知道x為區域及大值還是區域極小值進

## chk1-15 導數的極限記號
![](https://hackmd.io/_uploads/HkhoWpQxa.png)

可知：
f'(x)=g(x)=

![](https://hackmd.io/_uploads/S1Hkf6Qea.png)

所以算法就是將f(x)微分後帶入參考點即為答案

## chk1-16 多項式的極限運算

![](https://hackmd.io/_uploads/Syr2cLrxT.png)


## chk1-17 導數的極限定義 

這邊是要說lim形式是導數的極限樣子的定義

![](https://hackmd.io/_uploads/BJUzALSxa.png)


## chk1-18 導函數的極限定義



題目有點難

![](https://hackmd.io/_uploads/HJXqmDBgT.png)

亂算法：

![](https://hackmd.io/_uploads/Hk-FQPBgp.png)

認真算法：

![](https://hackmd.io/_uploads/HJjdRPrxa.png)

--- 


![](https://hackmd.io/_uploads/ByDCXwBxT.png)
![](https://hackmd.io/_uploads/BkDoHvBep.png)


---


![](https://hackmd.io/_uploads/rke1NwSla.png)
![](https://hackmd.io/_uploads/BJPHkdrga.png)

---

![](https://hackmd.io/_uploads/r1iJEPBla.png)
![](https://hackmd.io/_uploads/HJdxluHgp.png)


---

![](https://hackmd.io/_uploads/rJReNDBg6.png)
![](https://hackmd.io/_uploads/H1jsxdrgT.png)

![](https://hackmd.io/_uploads/rJltgwulp.png)


## chk1-20 微分乘法律
f(x)=a*b
f'(x)=a'*b+a*b'

## chk1-23 擴張的微分基本公式
![](https://hackmd.io/_uploads/Hy7Rs6Ob6.jpg)

## chk1-28 微分連鎖律

最強大之性質
![](https://hackmd.io/_uploads/BJjLZ8mMp.png)


## chk1-30 微分除法律


![](https://hackmd.io/_uploads/SkZE2L7M6.png)

## chk1-30 微分除法律

1. b
2. d
3. ?
4. d
5. b


## chk1-33 三次函數圖形

![](https://hackmd.io/_uploads/B11Y0-BMT.png)


k=f(h)，代表向上偏移量
q=f'(x)，代表一次項的係數，其正負影響圖形，如下：

![](https://hackmd.io/_uploads/ryH-zfBzp.png)

![](https://hackmd.io/_uploads/SydfMGBfp.png)


## chk1-35 少數的意外狀況

每個的意義




f'(x)=0
切線為0

f''(x)=0或是無意義
該點附近像是一條線，若曲率相反，也就是他的左右的二次微分正負相反，稱為反曲點




可知：


f’(x)=0 && f''(x)=0

![](https://hackmd.io/_uploads/rk1Dox9fT.png)


f’(x)!=0 && f''(x)=0

![](https://hackmd.io/_uploads/BJIKuxqfT.png)

若f’(x)!=0 && f''(x)=0但f'''(x)==0，該處並非反曲點，如下四次函數

![](https://hackmd.io/_uploads/BJgZYecf6.png)





f’(x)=0 && f''(x)=0

![](https://hackmd.io/_uploads/HkAPtl9zT.png)




## chk1-37微量符號用於估計

![image.png](https://hackmd.io/_uploads/SJ6NBFP7a.png)

![](https://hackmd.io/_uploads/HJwQfL9Ga.png)


## chk1-45 反導函數

![image.png](https://hackmd.io/_uploads/rJutZtwmT.png)


![image.png](https://hackmd.io/_uploads/Syya2V7mT.png)

可以看成「誰的倒數為x」，符合都是f(x)的反導函數

![image.png](https://hackmd.io/_uploads/BkOIMtDXa.png)

## 自由落體

![image.png](https://hackmd.io/_uploads/SynI_YPmT.png)


## chk1-48 微積分基本定理


定積分
找出反倒數之後帶進去相減

![image.png](https://hackmd.io/_uploads/HkkCI8876.png)

![image.png](https://hackmd.io/_uploads/Bk8EcKDQp.png)

![image.png](https://hackmd.io/_uploads/ryRUjYDmp.png)

![image.png](https://hackmd.io/_uploads/Hypx3FvQ6.png)


## 弓形面積

![image](https://hackmd.io/_uploads/rkyJOMT7a.png)


![384567805_1074286380253132_380474773142400268_n](https://hackmd.io/_uploads/BJq6Id0mp.jpg)


在積分之前先減掉，意思等於積分之後相減


![385400088_2611921672300216_3492488799368852245_n](https://hackmd.io/_uploads/Hylb7DuCma.jpg)



請問y=x和x軸圍的面積？
在（-2,4）範圍內

![400648860_1166242394336193_2242224529141948754_n](https://hackmd.io/_uploads/Hyj_vuCQT.png)


兩個函數交叉的地方要分開計算(上下相對位置會改變)



## 積分的計算 


### 一般積分

![image](https://hackmd.io/_uploads/BJ1y_OCQ6.png)


### 定積分

![image](https://hackmd.io/_uploads/S1xB_d0X6.png)


### 數值積分

無法積分時，直接切成很多ㄌ小塊計算

![image](https://hackmd.io/_uploads/ryHO_u0ma.png)

![image](https://hackmd.io/_uploads/ByXc__0mT.png)

選數值積分


![image](https://hackmd.io/_uploads/BysCddAQp.png)

得到科學記號:

\[數值,誤差估計,做了幾次計算,錯誤碼(0是正確,1、2、3、4...為出現錯誤)\]

### 交點計算 

solve(x^3-3*x^2+1=-x^2+2*x, x) 求兩曲線的交點


### 無限

![image](https://hackmd.io/_uploads/H1SH6d3rT.png)


嚴謹寫法

![386468700_3836064339947836_1343917441546537808_n](https://hackmd.io/_uploads/H1GMiJyPa.jpg)



## 曲線間的面積

![image](https://hackmd.io/_uploads/BkGycxJN6.png)

一個在上一個在下，還要包住

## 供需平衡

![下載 (1)](https://hackmd.io/_uploads/SJ5sGXyV6.jpg)

![image](https://hackmd.io/_uploads/HyGCfXkVT.png)




## chk1-55 連續函數值的平均

![image](https://hackmd.io/_uploads/SyxgmQ1E6.png)


算法：

S=∫^2^~0~(x^2^-0)dx

ans=S/2


## chk1-56 代換積分法

![Screenshot 2023-11-19 01.45.52](https://hackmd.io/_uploads/Bk4pdOIE6.png)



最後要帶回去的是u，也就是（x^2^+1）不是直接把x帶到u


## chk1-57 直方圖

![image](https://hackmd.io/_uploads/BynWKdUNT.png)

1. 相連
2. 底（下面刻度）*高（左邊）=面積（機率）

ex.  40~80的機率是(80-40)\*0.006=0.24=24%


## 1-58機率密度函數

![image](https://hackmd.io/_uploads/Sk9XfgD4a.png)


![image](https://hackmd.io/_uploads/BJhIMgPE6.png)

面積為機率!!!




## 定積分的機率意涵

![image](https://hackmd.io/_uploads/BJUCoZDVp.png)


## 圓的面積

![image](https://hackmd.io/_uploads/rJo2w9-8T.png)

圓的面積可以看成把所有半徑的圓周長積分
也就是2rπ (r:0~r\)，積分之後得到πr^2^


## 球的體積

![image](https://hackmd.io/_uploads/Sk6nAq-Ia.png)


圓盤面積：![image](https://hackmd.io/_uploads/B1tN1ibIa.png)

## chk1-62 球的表面積

![image](https://hackmd.io/_uploads/rkOlGobU6.png)


##  連續複利的年增率

![image](https://hackmd.io/_uploads/SkwxBs-86.png)

![image](https://hackmd.io/_uploads/HJpoqsZIT.png)

所以年利率為2%時


![image](https://hackmd.io/_uploads/HJcxojbL6.png)

減去1

![image](https://hackmd.io/_uploads/rJAWjiWUp.png)

再乘100%

![image](https://hackmd.io/_uploads/HJxVooZ8T.png)

就是效年利率


## chk2-02 指函數的微分

![image](https://hackmd.io/_uploads/By5Toj-Up.png)

![image](https://hackmd.io/_uploads/ByOmlT-L6.png)


## 標準指函數及其微分

![image](https://hackmd.io/_uploads/SywBL3b86.png)



## 標準指函數的反導函數

想要積分標準指數就一樣用代數變換

![image](https://hackmd.io/_uploads/ryOWllzUa.png)



## 函數與反函數上

![image](https://hackmd.io/_uploads/Hk8JCxfUp.png)

![image](https://hackmd.io/_uploads/r1PW0gzU6.png)


## 反函數的微分

![image](https://hackmd.io/_uploads/rkcxGsGIp.png)


## 自然對數與一般指數的微分

![image](https://hackmd.io/_uploads/HyxgF2GI6.png)

![image](https://hackmd.io/_uploads/Hy0jHsBUT.png)


## 自然對數的圖形與微分

![image](https://hackmd.io/_uploads/rkxJUxNaIT.png)


## 計算指對數 [電腦]

![image](https://hackmd.io/_uploads/B1WMN36I6.png)



![image](https://hackmd.io/_uploads/H1N_gNpUT.png)

## 指對數的微分應用

![image](https://hackmd.io/_uploads/rygbl4p86.png)


![image](https://hackmd.io/_uploads/Hye2ex1wp.png)
估計


## 指數與對數的積分

![image](https://hackmd.io/_uploads/SkuRONTIT.png)



![image](https://hackmd.io/_uploads/H1R4KNaIa.png)


![image](https://hackmd.io/_uploads/Bk4KC4aLT.png)

處理前面有x的
![Screenshot 2023-12-24 18.44.25](https://hackmd.io/_uploads/ByAVhYrwp.png)


![Screenshot 2023-12-19 18.43.49](https://hackmd.io/_uploads/S1hZg5Bva.png)





## 指對數的微積分計算 [電腦]

微分

![image](https://hackmd.io/_uploads/rkPAZBaUa.png)

積分

![image](https://hackmd.io/_uploads/Hkb-fHpLa.png)


## 反比函數的積分


![Screenshot 2023-12-19 12.38.52](https://hackmd.io/_uploads/SJSmJjA86.png)

![Screenshot 2023-12-19 12.41.17](https://hackmd.io/_uploads/Hy9XJsAUp.png)


