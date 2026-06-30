# CPE

歷屆英文試題
https://cpe.mcu.edu.tw/history.php

https://cpe.mcu.edu.tw/cpe/test_data/problems

歷屆線上評測
https://yuihuang.com/cpe/

## CPE 一顆星選集 49 道必考題


vjudge 網址：https://vjudge.net/article/2679

### 1.[c039. 00100 – The 3n + 1 problem](https://zerojudge.tw/ShowProblem?problemid=c039)

[英文題目網址](https://vjudge.net/problem/UVA-100)

/// collapse-code

```py
from functools import cmp_to_key


def f(x):
    global p
    if x < 0:
        return -(-x % p)
    return x % p


def cmp(a, b):
    ma = f(a)
    mb = f(b)

    if ma == mb:
        if a & 1 and b & 1:  # odd、odd
            return b - a
        if not (a & 1) and not (b & 1):
            return a - b

        # odd and even
        if a & 1 and not (b & 1):
            return -1
        if not (a & 1) and (b & 1):
            return 1

    return ma - mb


while 1:
    n, p = map(int, input().split())
    print(n, p)
    if n == 0 and p == 0:
        break

    a = [int(input()) for i in range(n)]

    a.sort(key=cmp_to_key(cmp))

    for i in a:
        print(i)


note = """

odd、even in the same % -> odd priority 
odd、odd -> large
even、even -> small

"""

```

///

### 2.[c082. 00118 – Mutant Flatworld Expolrers](https://zerojudge.tw/ShowProblem?problemid=c082)

[英文題目網址](https://vjudge.net/problem/UVA-118)

/// collapse-code

```py
```

///

### 3.[c007. 00272 – TeX Quotes](https://zerojudge.tw/ShowProblem?problemid=c007)

[英文題目網址](https://vjudge.net/problem/UVA-272)

/// collapse-code

```py
```

///

### 4.[e561. 00299 – Train Swapping](https://zerojudge.tw/ShowProblem?problemid=e561)

[英文題目網址](https://vjudge.net/problem/UVA-299)

/// collapse-code

```py
```

///

### 5.[c045. 00490 – Rotating Sentences](https://zerojudge.tw/ShowProblem?problemid=c045)

[英文題目網址](https://vjudge.net/problem/UVA-490)

/// collapse-code

```py
```

///

### 6.[a134. 00948 – Fibonaccimal Base](https://zerojudge.tw/ShowProblem?problemid=a134)

[英文題目網址](https://vjudge.net/problem/UVA-948)

/// collapse-code

```py
```

///

### 7.[c044. 10008 – What’s Cryptanalysis](https://zerojudge.tw/ShowProblem?problemid=c044)

[英文題目網址](https://vjudge.net/problem/UVA-10008)

/// collapse-code

```py
```

///

### 8.[e545. 10019 – Funny Encryption Method](https://zerojudge.tw/ShowProblem?problemid=e545)

[英文題目網址](https://vjudge.net/problem/UVA-10019)

/// collapse-code

```py
```

///

### 9.[c014. 10035 – Primary Arithmetic](https://zerojudge.tw/ShowProblem?problemid=c014)

[英文題目網址](https://vjudge.net/problem/UVA-10035)

/// collapse-code

```py
```

///

### 10.[d097. 10038 – Jolly Jumpers](https://zerojudge.tw/ShowProblem?problemid=d097)

[英文題目網址](https://vjudge.net/problem/UVA-10038)

/// collapse-code

```py
```

///

### 11.[a737. 10041 – Vito’s family](https://zerojudge.tw/ShowProblem?problemid=a737)

[英文題目網址](https://vjudge.net/problem/UVA-10041)

/// collapse-code

```py
```

///

### 12.[e579. 10050 – Hartals](https://zerojudge.tw/ShowProblem?problemid=e579)

[英文題目網址](https://vjudge.net/problem/UVA-10050)

/// collapse-code

```py
```

///

### 13.[a012. 10055 – Hashmat the Brave Warrior](https://zerojudge.tw/ShowProblem?problemid=a012)

[英文題目網址](https://vjudge.net/problem/UVA-10055)

/// collapse-code

```py
```

///

### 14.[e510. 10056 – What is the Probability?](https://zerojudge.tw/ShowProblem?problemid=e510)

[英文題目網址](https://vjudge.net/problem/UVA-10056)

/// collapse-code

```py
```

///

### 15.[e606. 10057 – A mid-summer nights dream](https://zerojudge.tw/ShowProblem?problemid=e606)

[英文題目網址](https://vjudge.net/problem/UVA-10057)

/// collapse-code

```py
```

///

### 16.[c012. 10062 – Tell me the frequencies!](https://zerojudge.tw/ShowProblem?problemid=c012)

[英文題目網址](https://vjudge.net/problem/UVA-10062)

/// collapse-code

```py
```

///

### 17.[d226. 10071 – Back to High School Physics](https://zerojudge.tw/ShowProblem?problemid=d226)

[英文題目網址](https://vjudge.net/problem/UVA-10071)

/// collapse-code

```py
```

///

### 18.[UVA-10093 An Easy Problem!](https://vjudge.net/problem/UVA-10093)

[英文題目網址](https://vjudge.net/problem/UVA-10093)

/// collapse-code

```py
```

///

### 19.[a741. 10101 – Bangla Numbers](https://zerojudge.tw/ShowProblem?problemid=a741)

[英文題目網址](https://vjudge.net/problem/UVA-10101)

/// collapse-code

```py
```

///

### 20.[e555. 10170 – The Hotel with Infinite Rooms](https://zerojudge.tw/ShowProblem?problemid=e555)

[英文題目網址](https://vjudge.net/problem/UVA-10170)

/// collapse-code

```py
```

///

### 21.[e605. 10189 – Minesweeper](https://zerojudge.tw/ShowProblem?problemid=e605)

[英文題目網址](https://vjudge.net/problem/UVA-10189)

/// collapse-code

```py
```

///

### 22.[e566. 10190 – Divide, But Not Quite Conquer!](https://zerojudge.tw/ShowProblem?problemid=e566)

[英文題目網址](https://vjudge.net/problem/UVA-10190)

/// collapse-code

```py
```

///

### 23.[d306. 10193 – All You Need Is Love](https://zerojudge.tw/ShowProblem?problemid=d306)

[英文題目網址](https://vjudge.net/problem/UVA-10193)

/// collapse-code

```py
```

///

### 24.[UVA-10221 Satellites](https://vjudge.net/problem/UVA-10221)

[英文題目網址](https://vjudge.net/problem/UVA-10221)

/// collapse-code

```py
```

///

### 25.[e578. 10222 – Decode the Mad man](https://zerojudge.tw/ShowProblem?problemid=e578)

[英文題目網址](https://vjudge.net/problem/UVA-10222)

/// collapse-code

```py
```

///

### 26.[d492. 10226 – Hardwood species](https://zerojudge.tw/ShowProblem?problemid=d492)

[英文題目網址](https://vjudge.net/problem/UVA-10226)

/// collapse-code

```py
```

///

### 27.[d387. 10235 – Simply Emirp](https://zerojudge.tw/ShowProblem?problemid=d387)

[英文題目網址](https://vjudge.net/problem/UVA-10235)

/// collapse-code

```py
```

///

### 28.[e512. 10242 – Fourth Point!!](https://zerojudge.tw/ShowProblem?problemid=e512)

[英文題目網址](https://vjudge.net/problem/UVA-10242)

/// collapse-code

```py
```

///

### 29.[e507. 10252 – Common Permutation](https://zerojudge.tw/ShowProblem?problemid=e507)

[英文題目網址](https://vjudge.net/problem/UVA-10252)

/// collapse-code

```py
```

///

### 30.[f444: 10268 – 498-bis](https://zerojudge.tw/ShowProblem?problemid=f444)

[英文題目網址](https://vjudge.net/problem/UVA-10268)

/// collapse-code

```py
```

///

### 31.[e516. 10409 – Die Game](https://zerojudge.tw/ShowProblem?problemid=e516)

[英文題目網址](https://vjudge.net/problem/UVA-10409)

/// collapse-code

```py
```

///

### 32.[e531. 10415 – Eb Alto Saxophone Player](https://zerojudge.tw/ShowProblem?problemid=e531)

[英文題目網址](https://vjudge.net/problem/UVA-10415)

/// collapse-code

```py
```

///

### 33.[a743. 10420 – List of Conquests](https://zerojudge.tw/ShowProblem?problemid=a743)

[英文題目網址](https://vjudge.net/problem/UVA-10420)

/// collapse-code

```py
```

///

### 34.[UVA-10642 Can You Solve It?](https://vjudge.net/problem/UVA-10642)

[英文題目網址](https://vjudge.net/problem/UVA-10642)

/// collapse-code

```py
```

///

### 35.[c022. 10783 – Odd Sum](https://zerojudge.tw/ShowProblem?problemid=c022)

[英文題目網址](https://vjudge.net/problem/UVA-10783)

/// collapse-code

```py
```

///

### 36.[c004. 10812 – Beat the Spread!](https://zerojudge.tw/ShowProblem?problemid=c004)

[英文題目網址](https://vjudge.net/problem/UVA-10812)

/// collapse-code

```py
```

///

### 37.[e575. 10908 – Largest Squares](https://zerojudge.tw/ShowProblem?problemid=e575)

[英文題目網址](https://vjudge.net/problem/UVA-10908)

/// collapse-code

```py
```

///

### 38.[d672. 10922 – 2 the 9s](https://zerojudge.tw/ShowProblem?problemid=d672)

[英文題目網址](https://vjudge.net/problem/UVA-10922)

/// collapse-code

```py
```

///

### 39.[d235. 10929 – You can say 11](https://zerojudge.tw/ShowProblem?problemid=d235)

[英文題目網址](https://vjudge.net/problem/UVA-10929)

/// collapse-code

```py
```

///

### 40.[a132. 10931 – Parity](https://zerojudge.tw/ShowProblem?problemid=a132)

[英文題目網址](https://vjudge.net/problem/UVA-10931)

/// collapse-code

```py
```

///

### 41.[UVA-11005 Cheapest Base](https://vjudge.net/problem/UVA-11005)

[英文題目網址](https://vjudge.net/problem/UVA-11005)

/// collapse-code

```py
```

///

### 42.[d123. 11063 – B2-Sequence](https://zerojudge.tw/ShowProblem?problemid=d123)

[英文題目網址](https://vjudge.net/problem/UVA-11063)

/// collapse-code

```py
```

///

### 43.[d189. 11150 – Cola](https://zerojudge.tw/ShowProblem?problemid=d189)

[英文題目網址](https://vjudge.net/problem/UVA-11150)

/// collapse-code

```py
```

///

### 44.[d750. 11321 – Sort! Sort!! and Sort!!!](https://zerojudge.tw/ShowProblem?problemid=d750)

[英文題目網址](https://vjudge.net/problem/UVA-11321)

/// collapse-code

```py
```

///

### 45.[c813. 11332 – Summing Digits](https://zerojudge.tw/ShowProblem?problemid=c813)

[英文題目網址](https://vjudge.net/problem/UVA-11332)

/// collapse-code

```py
```

///

### 46.[e513. 11349 – Symmetric Matrix](https://zerojudge.tw/ShowProblem?problemid=e513)

[英文題目網址](https://vjudge.net/problem/UVA-11349)

/// collapse-code

```py
```

///

### 47.[d255. 11417 – GCD](https://zerojudge.tw/ShowProblem?problemid=d255)

[英文題目網址](https://vjudge.net/problem/UVA-11417)

/// collapse-code

```py
```

///

### 48.[d186. 11461 – Square Numbers](https://zerojudge.tw/ShowProblem?problemid=d186)

[英文題目網址](https://vjudge.net/problem/UVA-11461)

/// collapse-code

```py
```

///

### 49.[f709: 12019 – Doom’s Day Algorithm](https://zerojudge.tw/ShowProblem?problemid=f709)

[英文題目網址](https://vjudge.net/problem/UVA-12019)

/// collapse-code

```py
```

///
