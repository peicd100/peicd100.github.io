List 中可以擺任何型態的資料

```py
a = [1, 3.1416, 'Python', 'x']
```

Python 用 list of list 來實作二維陣列，也就是 a 是一個有 m 個元素的 List，
而 a 的每個元素都是一個有 n 個元素的 list。如果執行下面的程式：

> 先注意 list 乘法是把 *n 相鄰的 list 裡面的資料給重複。
> 也就是 [[[0]]]*3 其實是重複三次 list 的內容 `[[0]]`，變成 `[[[0]], [[0]], [[0]]]`

`a = [[0]*4 for i in range(3)]`
=>`a = [[0,0,0,0] for i in range(3)]`
=>`a = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]`

`b = [[0]*4]*3`
=>`b = [[0,0,0,0]]*3`
=>`b = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]`


建一個九九乘法表


```py
t = [[0] * 10 for i in range(10)]
for i in range(1, 10):
    for j in range(1, 10):
        t[i][j] = i * j

for i in t:
    for j in i:
        print(j,end=" ")
    print()

```
output:
```
0 0 0 0 0 0 0 0 0 0 
0 1 2 3 4 5 6 7 8 9 
0 2 4 6 8 10 12 14 16 18 
0 3 6 9 12 15 18 21 24 27 
0 4 8 12 16 20 24 28 32 36 
0 5 10 15 20 25 30 35 40 45 
0 6 12 18 24 30 36 42 48 54 
0 7 14 21 28 35 42 49 56 63 
0 8 16 24 32 40 48 56 64 72 
0 9 18 27 36 45 54 63 72 81 
```



常見的二維陣列輸入格式是由上而下、由左而右。

例如，若輸入資料為：

```text
3 4
0 1 2 3
4 5 6 7
8 9 10 11
```

第一行的兩個數字是 `m` 與 `n`，我們可以用以下方式讀入：

```python
m, n = map(int, input().split())
a = []

for i in range(m):
    a.append([int(x) for x in input().split()])
```


也可以先將 `a` 初始化為 `m` 個空 list：

```python
m, n = map(int, input().split())
a = [[] for i in range(m)]

for i in range(m):
    a[i] = [int(x) for x in input().split()]
```

---

比較推薦使用前者初始化變數與 list，除非事前無法得知元素個數。