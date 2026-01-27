# scanf & printf

## scanf：輸入

成功輸入(成功更改變數內容)，回傳true，否則回傳false

### 基本
```cpp
scanf("%d",&n);
```
使用 & 來取得位置 ， scanf 找到位置後將數字存入


### 限制輸入
```cpp
scanf("is%d",&n);
```
要輸入is(加一個數字)才能順利輸入

## printf 輸出

### 基本
```cpp
printf("%d",n);
```
直接讀取變數後輸出。

### 連帶輸出
```cpp
printf("number is : %d",100);
```