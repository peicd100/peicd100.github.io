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

## 有哪些 %




### 1. 核心觀念

`scanf` 和 `printf` 的 `%` 叫做 **format specifier(格式指定符)**。

簡單講：

```c
printf("%d", x);   // 把 x 用整數格式印出來
scanf("%d", &x);   // 從輸入讀一個整數，存到 x
```

但兩者很重要的差別是：

```c
printf("%f", double變數);
scanf("%f", &float變數);
scanf("%lf", &double變數);
```

`printf` 因為 function argument promotion(函式參數提升)，`float` 會被提升成 `double`，所以印 `float/double` 都用 `%f`；但 `scanf` 要知道你給的是哪種「指標」，所以 `float*` 用 `%f`，`double*` 用 `%lf`。這是初學者最常錯的地方之一。`scanf` 的 `%c`、`%[`、`%n` 不會自動跳過空白字元，所以常見寫法是 `scanf(" %c", &c);`，前面加空白吃掉換行。([Cppreference][1])

---

### 2. `printf` 常用 `%`

`printf` 是「輸出」，參數通常直接放變數，不加 `&`。

| 格式          | 意思                                  | 對應常見型別               |
| ----------- | ----------------------------------- | -------------------- |
| `%d` / `%i` | signed decimal integer(有號十進位整數)     | `int`                |
| `%u`        | unsigned decimal integer(無號十進位整數)   | `unsigned int`       |
| `%o`        | unsigned octal(八進位)                 | `unsigned int`       |
| `%x`        | unsigned hexadecimal(十六進位，小寫)       | `unsigned int`       |
| `%X`        | unsigned hexadecimal(十六進位，大寫)       | `unsigned int`       |
| `%f`        | decimal floating point(小數)          | `double`             |
| `%e` / `%E` | scientific notation(科學記號)           | `double`             |
| `%g` / `%G` | 自動選 `%f` 或 `%e` 較短者                 | `double`             |
| `%a` / `%A` | hexadecimal floating point(十六進位浮點數) | `double`             |
| `%c`        | character(字元)                       | `int`，通常放 `char` 也可以 |
| `%s`        | string(字串)                          | `char *`             |
| `%p`        | pointer address(指標位址)               | `void *`             |
| `%n`        | 把目前已輸出的字元數存進變數                      | `int *`              |
| `%%`        | 印出 `%` 本身                           | 不吃參數                 |

`printf` 的完整格式大概長這樣：`%[flags][width][.precision][length]specifier`，例如 `printf("%08.2f", x);` 代表寬度 8、不足補 0、小數 2 位。([Cppreference][1])

---

### 3. `scanf` 常用 `%`

`scanf` 是「輸入」，除了字串陣列等少數情況，通常要放變數位址，也就是加 `&`。

| 格式          | 意思                                  | 對應常見型別           |
| ----------- | ----------------------------------- | ---------------- |
| `%d`        | 讀 signed decimal integer(有號十進位整數)   | `int *`          |
| `%i`        | 讀整數，自動判斷 10/8/16 進位                 | `int *`          |
| `%u`        | 讀 unsigned decimal integer(無號十進位整數) | `unsigned int *` |
| `%o`        | 讀八進位整數                              | `unsigned int *` |
| `%x` / `%X` | 讀十六進位整數                             | `unsigned int *` |
| `%f`        | 讀 `float`                           | `float *`        |
| `%lf`       | 讀 `double`                          | `double *`       |
| `%Lf`       | 讀 `long double`                     | `long double *`  |
| `%c`        | 讀一個字元，不會跳過空白                        | `char *`         |
| `%s`        | 讀一段字串，遇空白停止                         | `char *`         |
| `%[`        | scanset(指定可接受字元集合)                  | `char *`         |
| `%p`        | 讀指標格式                               | `void **`        |
| `%n`        | 儲存目前已讀取的字元數                         | `int *`          |
| `%%`        | 匹配輸入中的 `%`                          | 不存值              |

`scanf` 的完整格式大概長這樣：`%[*][width][length]specifier`。其中 `*` 代表讀了但不存，例如 `scanf("%*d %d", &x);` 會跳過第一個整數，只存第二個。([Cppreference][2])

---

### 4. 長度修飾：`h`、`l`、`ll` 這些是什麼？

這些不是獨立的 `%`，而是用來修飾資料型別大小。

#### 4.1 整數

| 型別                   | `printf` | `scanf` |
| -------------------- | -------: | ------: |
| `short`              |    `%hd` |   `%hd` |
| `int`                |     `%d` |    `%d` |
| `long`               |    `%ld` |   `%ld` |
| `long long`          |   `%lld` |  `%lld` |
| `unsigned short`     |    `%hu` |   `%hu` |
| `unsigned int`       |     `%u` |    `%u` |
| `unsigned long`      |    `%lu` |   `%lu` |
| `unsigned long long` |   `%llu` |  `%llu` |

例如：

```c
long long x;
scanf("%lld", &x);
printf("%lld\n", x);
```

---

#### 4.2 浮點數

| 型別            | `printf` | `scanf` |
| ------------- | -------: | ------: |
| `float`       |     `%f` |    `%f` |
| `double`      |     `%f` |   `%lf` |
| `long double` |    `%Lf` |   `%Lf` |

這裡最容易錯：

```c
double x;
scanf("%lf", &x);   // 對
printf("%f", x);    // 對
```

不要寫成：

```c
double x;
scanf("%f", &x);    // 錯，%f 期待 float*
```

---

### 5. 競程最常用版本

你寫 ZeroJudge、APCS、競程時，通常記這些就夠了：

```c
int a;
long long b;
double c;
char ch;
char s[100];

scanf("%d", &a);
scanf("%lld", &b);
scanf("%lf", &c);
scanf(" %c", &ch);
scanf("%s", s);

printf("%d\n", a);
printf("%lld\n", b);
printf("%.2f\n", c);
printf("%c\n", ch);
printf("%s\n", s);
```

重點是：

```c
scanf("%s", s);     // 不加 &
scanf("%d", &a);    // 要加 &
scanf(" %c", &ch);  // %c 前面常加空白，吃掉換行
```

---

### 6. 超短背法

```c
%d      int
%lld    long long
%f      printf 印 float/double
%lf     scanf 讀 double
%c      char
%s      string / char array
%x      hex
%p      pointer
%%      percent sign
```

你目前寫 C++ 的話，其實大多數情況用 `cin/cout` 比較不容易踩型別坑；但競程追求速度時，`scanf/printf` 還是很常見。

[1]: https://en.cppreference.com/c/io/fprintf?utm_source=chatgpt.com "printf, fprintf, sprintf, snprintf, printf_s, fprintf_s, sprintf_s, ..."
[2]: https://en.cppreference.com/c/io/fscanf?utm_source=chatgpt.com "scanf, fscanf, sscanf, scanf_s, fscanf_s, sscanf_s"
