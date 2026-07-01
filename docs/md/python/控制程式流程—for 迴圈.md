## range 是啥？

Python 的 `range()` 格式是：


```py
range(start, stop, step)
```

其中：

```py
start  # 起始值，會包含
stop   # 結束值，不包含
step   # 每次增加或減少多少
```

如果 `step` 是負數，就可以倒數。

```py
print(list(range(5))) # [0, 1, 2, 3, 4]
```

```py
print(list(range(2,5))) # [2, 3, 4]
```

```py
print(list(range(5, 0, -1))) # [5, 4, 3, 2, 1]
```


## for 迴圈

```py
for i in range(10):
    print(i, end=" ") # 0 1 2 3 4 5 6 7 8 9 
```

> 所以格式是 for i in <一個 list>

也可以是字串
```py
a = "axxple"
x= 0
for i in a:
    if i=='x':
        x+=1
print(x)     # 2
```
上面程式碼其實就是

```py
a = "axxple"
print(a.count("x"))

```




## 提早結束迴圈 break 與 continue


break：跳離迴圈，到迴圈結束的下一個指令。
continue：略過本回合迴圈剩下的部分，跳到迴圈的起點，是否進入迴圈的下一回合要看是否到達迴圈結束條件。


```py
for i in range(100):
    if input() == "1":
        print("It is 1")
        continue
    
    print("It is not 1")
    break

```

輸出：
```
1
It is 1
1
It is 1
1
It is 1
2
It is not 1

```