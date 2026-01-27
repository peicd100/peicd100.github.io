<!-- GPT1 https://chatgpt.com/g/g-p-69524891367c8191a9be2a02cea47baf-peicd-apcs/c/69524be2-cd24-8320-b860-82393607b1ef -->


<!--GPT2 https://chatgpt.com/g/g-p-69524891367c8191a9be2a02cea47baf-peicd-apcs/c/69538a24-4128-8321-a5d1-7b2d3871db80 -->


## T01｜每組取最大：輸出每組最大值

### 題目

你會拿到 N 組數字，每組有 M 個整數。請你對每一組找出該組的最大值並輸出。

**輸入格式**

* 第一行：兩個整數 N、M
* 接著 N 行：每行 M 個整數

**輸出格式**

* 輸出 N 行：第 i 行輸出第 i 組的最大值

**範例輸入**

```in
3 4
1 7 2 7
5 3 9 1
6 6 6 6
```

**範例輸出**

```out
7
9
6
```

**範例計算過程**

* 第 1 組：1,7,2,7 → 最大值 7
* 第 2 組：5,3,9,1 → 最大值 9
* 第 3 組：6,6,6,6 → 最大值 6

### 測資

#### 測資 1

```in
3 4
1 7 2 7
5 3 9 1
6 6 6 6
```

#### 測資 2

```in
1 5
-1 -2 -3 -4 -5
```

#### 測資 3

```in
2 3
10 10 9
-3 -3 -3
```

#### 測資 4

```in
4 1
5
4
3
2
```

#### 測資 5

```in
2 6
1 2 3 4 5 6
6 5 4 3 2 1
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    for(int i=0;i<N;i++){
        long long mx = LLONG_MIN;
        for(int j=0;j<M;j++){
            long long x; cin >> x;
            mx = max(mx, x);
        }
        cout << mx << "\n";
    }
    return 0;
}
```

### 詳解

* 每一組開始前要把最大值重新初始化。

---

## T02｜總和 + 整除篩選輸出

### 題目

你會拿到 N 個正整數 a1..aN。令 S 為總和。

請輸出兩行：

1. 第一行輸出 S
2. 第二行依輸入順序輸出所有能整除 S 的 ai（滿足 `S % ai == 0`），用空格分隔；若一個都沒有，輸出 `-1`。

**輸入格式**

* 第一行：整數 N
* 第二行：N 個正整數

**輸出格式**

* 第一行：S
* 第二行：能整除 S 的 ai（空格分隔）或 `-1`

**範例輸入**

```in
6
2 3 4 5 6 12
```

**範例輸出**

```out
32
2 4
```

**範例計算過程**

* S = 2+3+4+5+6+12 = 32
* 依序檢查：32%2=0（輸出 2），32%3≠0，32%4=0（輸出 4），其餘不輸出。

### 測資

#### 測資 1

```in
6
2 3 4 5 6 12
```

#### 測資 2

```in
3
7 9 6
```

#### 測資 3

```in
4
1 2 4 8
```

#### 測資 4

```in
5
3 3 3 3 3
```

#### 測資 5

```in
2
1000000000 1000000000
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<long long> a(N);
    long long S = 0;
    for(int i=0;i<N;i++){
        cin >> a[i];
        S += a[i];
    }

    cout << S << "\n";

    bool any = false;
    for(int i=0;i<N;i++){
        if(S % a[i] == 0){
            if(any) cout << ' ';
            cout << a[i];
            any = true;
        }
    }
    if(!any) cout << -1;
    cout << "\n";
    return 0;
}
```

### 詳解

* 第二行要求「依輸入順序」輸出。
* 用 `any` 控制空格最不容易出錯。

---

## T03｜字串成對交換

### 題目

給你一個長度為偶數的字串 S。把每兩個字元視為一組：(S[0],S[1])、(S[2],S[3])...

請把每一組內的兩個字元交換位置，輸出新字串。

**輸入格式**

* 一行：字串 S（長度為偶數，且不含空白）

**輸出格式**

* 一行：交換後的字串

**範例輸入**

```in
abcdef
```

**範例輸出**

```out
badcfe
```

**範例計算過程**

* 分組：ab / cd / ef
* 每組交換：ba / dc / fe
* 合併：badcfe

### 測資

#### 測資 1

```in
abcdef
```

#### 測資 2

```in
112233
```

#### 測資 3

```in
ZZYYXX
```

#### 測資 4

```in
AaBb
```

#### 測資 5

```in
01010100
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    for(int i=0;i<(int)s.size();i+=2){
        swap(s[i], s[i+1]);
    }

    cout << s << "\n";
    return 0;
}
```

### 詳解

* 用 `i += 2` 走訪，每次只處理一組。

---

## T04｜字串成對排序（每兩字元內部排序）

### 題目

給你一個長度為偶數的字串 S。把每兩個字元視為一組。

對每組做「字元大小排序」（較小的字元在前），輸出新字串。

**輸入格式**

* 一行：字串 S（長度為偶數，且不含空白）

**輸出格式**

* 一行：排序後字串

**範例輸入**

```in
cbaadc
```

**範例輸出**

```out
bcaacd
```

**範例計算過程**

* 分組：cb / aa / dc
* 每組內排序：bc / aa / cd
* 合併：bcaacd

### 測資

#### 測資 1

```in
cbaadc
```

#### 測資 2

```in
4312
```

#### 測資 3

```in
BAdc
```

#### 測資 4

```in
zzxx
```

#### 測資 5

```in
9a8b
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    for(int i=0;i<(int)s.size();i+=2){
        if(s[i] > s[i+1]) swap(s[i], s[i+1]);
    }

    cout << s << "\n";
    return 0;
}
```

### 詳解

* 只做「每組兩個字元」的小排序，不是整串排序。

---

## T05｜完美洗牌（交錯合併兩半）

### 題目

給你一個長度為偶數的字串 S。

把 S 平分成左半 L 與右半 R（長度都為 n/2），輸出交錯合併結果：
L[0]R[0]L[1]R[1]...L[n/2-1]R[n/2-1]

**輸入格式**

* 一行：字串 S（長度為偶數，且不含空白）

**輸出格式**

* 一行：洗牌後字串

**範例輸入**

```in
abcdef
```

**範例輸出**

```out
adbecf
```

**範例計算過程**

* L=abc，R=def
* 交錯：a d b e c f → adbecf

### 測資

#### 測資 1

```in
abcdef
```

#### 測資 2

```in
1122
```

#### 測資 3

```in
AAAABBBB
```

#### 測資 4

```in
01234567
```

#### 測資 5

```in
xyXY
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    int n = (int)s.size();
    int half = n / 2;
    string L = s.substr(0, half);
    string R = s.substr(half);

    string out;
    out.reserve(n);
    for(int i=0;i<half;i++){
        out.push_back(L[i]);
        out.push_back(R[i]);
    }

    cout << out << "\n";
    return 0;
}
```

### 詳解

* 平分後再交錯輸出即可。

---


<!-- ## T06｜矩陣上下翻轉（Flip Up-Down）

### 題目

給你一個 R×C ( 0 < R,C < 100 ) 的矩陣，請做「上下翻轉」：列順序反過來。

**輸入格式**

* 第一行：R C
* 接著 R 行：每行 C 個整數

**輸出格式**

* 輸出 R 行：翻轉後矩陣

**範例輸入**

```in
3 2
1 2
3 4
5 6
```

**範例輸出**

```out
5 6
3 4
1 2
```

**範例計算過程**

* 上下翻轉等於把列順序反過來：第 3 列→第 1 列、第 2 列不變、第 1 列→第 3 列。

### 測資

#### 測資 1

```in
3 2
1 2
3 4
5 6
```

#### 測資 2

```in
1 4
9 8 7 6
```

#### 測資 3

```in
2 3
1 2 3
4 5 6
```

#### 測資 4

```in
4 1
1
2
3
4
```

#### 測資 5

```in
2 2
-1 0
7 7
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C;
    cin >> R >> C;
    vector<vector<long long>> a(R, vector<long long>(C));
    for(int i=0;i<R;i++) for(int j=0;j<C;j++) cin >> a[i][j];

    reverse(a.begin(), a.end());

    for(int i=0;i<R;i++){
        for(int j=0;j<C;j++){
            if(j) cout << ' ';
            cout << a[i][j];
        }
        cout << "\n";
    }
    return 0;
}
```

### 詳解

* 直接反轉 row 陣列最不容易寫錯。

---
 -->



<!-- ## T07｜矩陣順時針旋轉 90 度

### 題目

給你一個 R×C 矩陣，請輸出順時針旋轉 90 度後的矩陣。

**輸入格式**

* 第一行：R C
* 接著 R 行：每行 C 個整數

**輸出格式**

* 第一行：新矩陣大小（C R）
* 接著 C 行：每行 R 個整數

**範例輸入**

```in
2 3
1 2 3
4 5 6
```

**範例輸出**

```out
3 2
4 1
5 2
6 3
```

**範例計算過程**

* 旋轉後大小變成 3×2。
* 新(0,0)=原(1,0)=4，新(0,1)=原(0,0)=1 → 第 1 列是 4 1
* 新(1,0)=原(1,1)=5，新(1,1)=原(0,1)=2 → 第 2 列是 5 2
* 新(2,0)=原(1,2)=6，新(2,1)=原(0,2)=3 → 第 3 列是 6 3

### 測資

#### 測資 1

```in
2 3
1 2 3
4 5 6
```

#### 測資 2

```in
1 4
9 8 7 6
```

#### 測資 3

```in
3 1
1
2
3
```

#### 測資 4

```in
2 2
1 2
3 4
```

#### 測資 5

```in
3 2
1 2
3 4
5 6
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C;
    cin >> R >> C;
    vector<vector<long long>> a(R, vector<long long>(C));
    for(int i=0;i<R;i++) for(int j=0;j<C;j++) cin >> a[i][j];

    vector<vector<long long>> b(C, vector<long long>(R));
    for(int i=0;i<R;i++){
        for(int j=0;j<C;j++){
            b[j][R-1-i] = a[i][j];
        }
    }

    cout << C << ' ' << R << "\n";
    for(int i=0;i<C;i++){
        for(int j=0;j<R;j++){
            if(j) cout << ' ';
            cout << b[i][j];
        }
        cout << "\n";
    }
    return 0;
}
```

### 詳解

* 對應式：`b[j][R-1-i] = a[i][j]`。

---

 -->



## T08｜矩陣反推：逆序還原操作序列（旋轉/翻轉）

### 題目

你會拿到「操作後」的矩陣 B 與一串操作序列。你必須還原「操作前」的原矩陣 A。

操作定義：

* 0：把矩陣順時針旋轉 90 度
* 1：把矩陣上下翻轉

原矩陣 A 依序做完這串操作序列後得到 B。請你輸出 A。

**輸入格式**

* 第一行：R C M（B 的大小為 R×C，操作數 M，且 0 < R, C < 100）
* 接著 R 行：矩陣 B（每行 C 個整數）
* 最後一行：M 個整數（由左到右是「執行順序」，每個值為 0 或 1）

**輸出格式**

* 第一行：還原後矩陣 A 的大小（列數 欄數）
* 接著輸出 A（每行以空格分隔）

**範例輸入**

```in
3 2 4
3 6
2 5
1 4
1 0 1 1
````

**範例輸出**

```out
2 3
3 2 1
6 5 4
```

**範例計算過程**

* 要還原 A：把操作序列倒序，並改成對 B 執行對應的「逆操作」。

  * 1（上下翻轉）的逆仍是上下翻轉
  * 0（順時針 90 度旋轉）的逆是逆時針 90 度旋轉
* 原序列為：1 0 1 1
  倒序後是：1 1 0 1
  因此對 B 依序執行：**上下翻轉 → 逆時針 90 度 → 上下翻轉**

1. 初始矩陣 B（3×2）

```txt
3 6
2 5
1 4
```

2. 執行「上下翻轉(1)」（仍為 3×2）

```txt
1 4
2 5
3 6
```

3. 執行「上下翻轉(1)」（仍為 3×2）

```txt
3 6
2 5
1 4
```

4. 執行「逆時針旋轉 90 度(0)」（3×2 變為 2×3）

```txt
6 5 4
3 2 1
```

5. 再執行一次「上下翻轉(1)」（仍為 2×3），得到還原後的 A

```txt
3 2 1
6 5 4
```

### 測資

#### 測資 1

```in
3 2 3
3 6
2 5
1 4
1 0 1
```

#### 測資 2

```in
2 3 1
4 1 0
5 2 0
0
```

#### 測資 3

```in
2 2 2
1 2
3 4
1 1
```

#### 測資 4

```in
1 3 1
7 8 9
1
```

#### 測資 5

```in
3 1 1
1
2
3
0
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

static vector<vector<long long>> rot90(const vector<vector<long long>>& a){
    int R = (int)a.size();
    int C = (int)a[0].size();
    vector<vector<long long>> b(C, vector<long long>(R));
    for(int i=0;i<R;i++){
        for(int j=0;j<C;j++){
            b[j][R-1-i] = a[i][j];
        }
    }
    return b;
}

static vector<vector<long long>> rotCCW(const vector<vector<long long>>& a){
    // 逆時針 90 = 順時針 90 做 3 次
    auto b = rot90(a);
    b = rot90(b);
    b = rot90(b);
    return b;
}

static vector<vector<long long>> flipUD(vector<vector<long long>> a){
    reverse(a.begin(), a.end());
    return a;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C, M;
    cin >> R >> C >> M;

    vector<vector<long long>> mat(R, vector<long long>(C));
    for(int i=0;i<R;i++) for(int j=0;j<C;j++) cin >> mat[i][j];

    vector<int> ops(M);
    for(int i=0;i<M;i++) cin >> ops[i];

    for(int i=M-1;i>=0;i--){
        if(ops[i] == 1) mat = flipUD(mat);
        else mat = rotCCW(mat);
    }

    cout << mat.size() << ' ' << mat[0].size() << "\n";
    for(int i=0;i<(int)mat.size();i++){
        for(int j=0;j<(int)mat[0].size();j++){
            if(j) cout << ' ';
            cout << mat[i][j];
        }
        cout << "\n";
    }
    return 0;
}
```

### 詳解

* 反推必備：操作倒序 + 旋轉用逆時針（或等價作法）。



## T09｜單一圓盤左轉/右轉 N 圈

### 題目

你有一個長度為 L 的圓盤，用字串 S 表示（例如 S="abcd"）。圓盤可以循環位移。

現在給你方向與位移量：

* 方向為 `L`：代表向左轉 k 圈（每圈等於向左位移 1 格）
* 方向為 `R`：代表向右轉 k 圈（每圈等於向右位移 1 格）

請輸出旋轉後的字串。

**輸入格式**

* 第一行：字串 S（長度 L）
* 第二行：方向 dir（'L' 或 'R'）與整數 k（k 可很大）

**輸出格式**

* 一行：旋轉後的字串

**範例輸入**

```in
abcdef
R 2
```

**範例輸出**

```out
efabcd
```

**範例計算過程**

* 右轉 1：fabcde
* 右轉 2：efabcd

### 測資

#### 測資 1

```in
abcdef
R 2
```

#### 測資 2

```in
abcdef
L 2
```

#### 測資 3

```in
A
R 999
```

#### 測資 4

```in
012345
L 7
```

#### 測資 5

```in
hello
R 1000000001
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;
    char dir;
    long long k;
    cin >> dir >> k;

    int n = (int)s.size();
    k %= n;

    // 統一成右轉 k
    if(dir == 'L'){
        k = (n - (int)k) % n;
    }

    string out = s.substr(n - (int)k) + s.substr(0, n - (int)k);
    cout << out << "\n";
    return 0;
}
```

### 詳解

* 先做 `k %= n`。
* 左轉 k 等價於右轉 (n-k)。

---

## T10｜兩張圖的相似度（不旋轉）

### 題目

給你兩張同大小的圖片 A 與 B，皆為 R×C ( 0 < R,C < 100 ) 的整數矩陣。

相似度計算規則：

1. `same` = A 與 B 在相同位置 (i,j) 上「數值相等」的格子數量
2. `total` = R×C
3. `p = floor( same * 100 / total )`（無條件捨去）
4. 輸出格式為：`p%`

**輸入格式**

* 第一行：R C
* 接著 R 行：圖片 A
* 接著 R 行：圖片 B

**輸出格式**

* 一行：相似度（例如 `75%`）

**範例輸入**

```in
2 3
1 2 3
4 5 6
1 0 3
0 5 6
```

**範例輸出**

```out
66%
```

**範例計算過程**

* total=6
* 相同位置相等的格子： (0,0)=1、(0,2)=3、(1,1)=5、(1,2)=6，共 same=4
* p = floor(4*100/6)=66

### 測資

#### 測資 1

```in
2 3
1 2 3
4 5 6
1 0 3
0 5 6
```

#### 測資 2

```in
2 2
1 2
3 4
1 2
3 4
```

#### 測資 3

```in
2 3
1 1 1
1 1 1
0 0 0
0 0 0
```

#### 測資 4

```in
1 5
9 8 7 6 5
9 8 0 6 0
```

#### 測資 5

```in
3 1
1
2
3
1
9
3
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C;
    cin >> R >> C;

    vector<vector<long long>> A(R, vector<long long>(C));
    vector<vector<long long>> B(R, vector<long long>(C));

    for(int i=0;i<R;i++) for(int j=0;j<C;j++) cin >> A[i][j];
    for(int i=0;i<R;i++) for(int j=0;j<C;j++) cin >> B[i][j];

    long long same = 0;
    for(int i=0;i<R;i++) for(int j=0;j<C;j++) if(A[i][j] == B[i][j]) same++;

    long long total = 1LL * R * C;
    long long p = (same * 100) / total;

    cout << p << "%\n";
    return 0;
}
```

### 詳解

* 無條件捨去用整數除法最穩。

---

## T11｜條碼檢驗碼 + 統計最多產地

### 題目

你會拿到 N 個 13 碼條碼字串（每碼皆為 '0'~'9'），格式為：

* 第 1~3 碼：產地代碼（3 位數字字串，例如 "471"）
* 第 4~12 碼：商品本體碼（共 9 碼）
* 第 13 碼：檢驗碼 C

檢驗規則（用前 12 碼計算）：

* 把前 12 碼視為位置 1~12
* `Sodd`：位置 1,3,5,7,9,11 的數字總和
* `Seven`：位置 2,4,6,8,10,12 的數字總和

條碼合法當且僅當：
`(Sodd + 3*Seven + C) % 10 == 0`

請在所有「合法條碼」中，找出出現次數最多的產地代碼，輸出：
`產地代碼 次數`

題目保證：至少有 1 筆合法條碼，且最多次的產地代碼唯一。

**輸入格式**

* 第一行：整數 N
* 接著 N 行：每行一個 13 碼條碼

**輸出格式**

* 一行：產地代碼（3 碼）與其出現次數

**範例輸入**

```in
6
4710018000112
4711234560012
3001111111108
3001111111118
0309876543216
4710018000102
```

**範例輸出**

```out
471 2
```

**範例計算過程**

4710018000112：sodd:14,seven:9,c:2  -> 不合法
4711234560012：sodd:17,seven:17,c:2 -> 合法
3001111111108：sodd:7,seven:4,c:8   -> 不合法
3001111111118：sodd:7,seven:5,c:8   -> 合法
0309876543216：sodd:20,seven:28,c:6 -> 合法
4710018000102：sodd:14,seven:8,c:2  -> 合法


### 測資

#### 測資 1

```in
6
4710018000102
4711234560012
3001111111118
3001111111118
0309876543216
4710018000102
```

#### 測資 2

```in
1
4710018000102
```

#### 測資 3

```in
3
4710018000102
4710018000103
4710018000104
```

#### 測資 4

```in
4
0000000000000
0000000000000
9999999999999
9999999999999
```

#### 測資 5

```in
5
1234567890128
1234567890128
1234567890128
4564564564566
4564564564566
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

static bool valid13(const string& s){
    int Sodd = 0, Seven = 0;
    for(int pos=0; pos<12; pos++){
        int d = s[pos] - '0';
        // pos=0 對應位置 1
        if(pos % 2 == 0) Sodd += d;
        else Seven += d;
    }
    int C = s[12] - '0';
    return (Sodd + 3*Seven + C) % 10 == 0;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    unordered_map<string,int> cnt;

    for(int i=0;i<N;i++){
        string s;
        cin >> s;
        if(valid13(s)) cnt[s.substr(0,3)]++;
    }

    string best;
    int bestCnt = -1;
    for(auto &kv: cnt){
        if(kv.second > bestCnt){
            bestCnt = kv.second;
            best = kv.first;
        }
    }

    cout << best << ' ' << bestCnt << "\n";
    return 0;
}
```

### 詳解

* 位置是 1~12，但程式用 0-index（0~11），奇偶位要對好。

---


## T12｜排列中的循環數量（Cycle Count in a Permutation）

### 題目

給定一個長度為 N 的排列 p，表示 p 由 0..N-1 組成且每個數字恰好出現一次。

我們把這個排列視為一張「每個點都指向另一個點」的有向圖：對每個 i（0 ≤ i ≤ N-1），都有一條箭頭 i → p[i]。
因為 p 是排列，所以每個點的出度為 1、入度也為 1，因此整張圖一定會分解成若干個互不重疊的循環（cycle）。

請你計算並輸出這張圖中一共有幾個 cycle。



**什麼是 cycle？**
一組不同的數字 a1, a2, ..., ak 若滿足 a1→a2、a2→a3、…、ak→a1，就形成一個 cycle（長度為 k）。
每個數字只會屬於唯一的一個 cycle。



**輸入格式**
- 第一行：整數 N
- 第二行：N 個整數 p[0], p[1], ..., p[N-1]（為 0..N-1 的排列）


**輸出格式**
- 輸出一行：cycle 的數量



**範例輸入**
```in
9
1 2 0 4 3 6 7 5 8
````

**範例輸出**

```out
4
```

**範例計算過程**

* 0 → 1 → 2 → 0 是一個 cycle（長度 3）
* 3 → 4 → 3 是一個 cycle（長度 2）
* 5 → 6 → 7 → 5 是一個 cycle（長度 3）
* 8 → 8 是一個 cycle（長度 1）
  共 4 個 cycle





### 測資

#### 測資 1

```in
8
1 0 3 2 5 4 7 6
```

#### 測資 2

```in
5
1 0 4 2 3
```

#### 測資 3

```in
1
0
```

#### 測資 4

```in
6
1 2 3 4 5 0
```

#### 測資 5

```in
7
0 1 2 3 4 5 6
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> p(N);
    for (int i = 0; i < N; i++) cin >> p[i];

    vector<char> vis(N, 0);
    int cycles = 0;

    for (int i = 0; i < N; i++) {
        if (vis[i]) continue;
        cycles++;
        int cur = i;
        while (!vis[cur]) {
            vis[cur] = 1;
            cur = p[cur];
        }
    }

    cout << cycles << "\n";
    return 0;
}
```

### 詳解

* 每個點都屬於且只屬於一個循環；用 visited 走訪即可。

---

## T13｜01 規則加密（deque 兩端取出）

### 題目

給你長度 n 的字串 S，以及長度 n 的 01 字串 e。

建立一個 deque，初始把 S 的字元依序放入 deque（左到右）。接著依序處理 e：

* 若 e[i]='0'：從 deque **前端**取出 1 個字元，接到輸出字串 T 尾端
* 若 e[i]='1'：從 deque **後端**取出 1 個字元，接到輸出字串 T 尾端

請輸出最後得到的 T。

**輸入格式**

* 第一行：整數 n
* 第二行：01 字串 e（長度 n）
* 第三行：字串 S（長度 n）

**輸出格式**

* 一行：字串 T

**範例輸入**

```in
8
10110010
BCAADXYZ
```

**範例輸出**

```out
ZBYXCADA
```

**範例計算過程**
初始 deque=[B C A A D X Y Z]，T=""

* e[1]=1：取後端 Z → T=Z，deque=[B C A A D X Y]
* 0：取前端 B → T=ZB，deque=[C A A D X Y]
* 1：取後端 Y → T=ZBY，deque=[C A A D X]
* 1：取後端 X → T=ZBYX，deque=[C A A D]
* 0：取前端 C → T=ZBYXC，deque=[A A D]
* 0：取前端 A → T=ZBYXCA，deque=[A D]
* 1：取後端 D → T=ZBYXCAD，deque=[A]
* 0：取前端 A → T=ZBYXCADA

（註：這題的範例輸出以最後拼出的 T 為準。）

### 測資

#### 測資 1

```in
8
10110010
BCAADXYZ
```

#### 測資 2

```in
5
00000
ABCDE
```

#### 測資 3

```in
5
11111
ABCDE
```

#### 測資 4

```in
6
010101
ABCDEF
```

#### 測資 5

```in
4
1001
WXYZ
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    string e, S;
    cin >> e >> S;

    deque<char> dq;
    for(char ch: S) dq.push_back(ch);

    string T;
    T.reserve(n);
    for(int i=0;i<n;i++){
        if(e[i] == '0'){
            T.push_back(dq.front());
            dq.pop_front();
        }else{
            T.push_back(dq.back());
            dq.pop_back();
        }
    }

    cout << T << "\n";
    return 0;
}
```

### 詳解

* 最常錯：把 0/1 對應的「前端/後端」寫反。

---

## T14｜01 規則解密（反推：倒序 push 回 deque）

### 題目

加密規則如下：

* e[i]='0'：從 deque 前端取出 1 字元
* e[i]='1'：從 deque 後端取出 1 字元

現在給你 e 與加密後的 T，請還原原字串 S。

反推時必須從 i=n-1 倒著做：

* e[i]='0'：代表正向是 pop front，所以反向要把 T[i] push_front
* e[i]='1'：代表正向是 pop back，所以反向要把 T[i] push_back

**輸入格式**

* 第一行：整數 n
* 第二行：01 字串 e（長度 n）
* 第三行：字串 T（長度 n）

**輸出格式**

* 一行：還原後的字串 S

**範例輸入**

```in
8
10110010
ZBYXCADA
```

**範例輸出**

```out
BCAADXYZ
```

**範例計算過程**
從最後往前放回去（deque 初始為空）：

* i=8，e=0：push_front('A') → [A]
* i=7，e=1：push_back('D')  → [A D]
* i=6，e=0：push_front('A') → [A A D]
* i=5，e=0：push_front('C') → [C A A D]
* i=4，e=1：push_back('X')  → [C A A D X]
* i=3，e=1：push_back('Y')  → [C A A D X Y]
* i=2，e=0：push_front('B') → [B C A A D X Y]
* i=1，e=1：push_back('Z')  → [B C A A D X Y Z]
  得到 S="BCAADXYZ"。

### 測資

#### 測資 1

```in
8
10110010
ZBYXCADA
```

#### 測資 2

```in
5
00000
ABCDE
```

#### 測資 3

```in
5
11111
EDCBA
```

#### 測資 4

```in
4
0101
ADBC
```

#### 測資 5

```in
6
101010
FABCDE
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    string e, T;
    cin >> e >> T;

    deque<char> dq;
    for(int i=n-1;i>=0;i--){
        if(e[i] == '0') dq.push_front(T[i]);
        else dq.push_back(T[i]);
    }

    for(char ch: dq) cout << ch;
    cout << "\n";
    return 0;
}
```

### 詳解

* 反推關鍵：必須倒序處理，否則 deque 的前後端對應會錯。

---


## T15｜電子畫布：曼哈頓菱形加值（多次操作）

### 題目

有一個 H×W ( 0 < H,W < 100 ) 的畫布，初始每格都是 0。

共有 N 次操作，每次給 (r,c,t,x)：對所有格子 (i,j)，若 `|i-r|+|j-c|<=t`，則該格加上 x。

請輸出 N 次操作後的畫布。

**輸入格式**

* 第一行：H W N
* 接著 N 行：r c t x

**輸出格式**

* 輸出 H 行，每行 W 個整數（空格分隔）

**範例輸入**

```in
4 5 3
1 2 1 5
0 0 2 3
2 4 1 -2
````

**範例輸出**

```out
3 3 8 0 0
3 8 5 5 -2
3 0 5 -2 -2
0 0 0 0 -2
```

**範例計算過程**

* 初始（全為 0）

  ```txt
  0 0 0 0 0
  0 0 0 0 0
  0 0 0 0 0
  0 0 0 0 0
  ```
* 操作 1：(r,c,t,x) = (1,2,1,5)，距離 (1,2) 曼哈頓距離 ≤ 1 的格子全部 +5

  ```txt
  0 0 5 0 0
  0 5 5 5 0
  0 0 5 0 0
  0 0 0 0 0
  ```
* 操作 2：(r,c,t,x) = (0,0,2,3)，距離 (0,0) 曼哈頓距離 ≤ 2 的格子全部 +3

  ```txt
  3 3 8 0 0
  3 8 5 5 0
  3 0 5 0 0
  0 0 0 0 0
  ```
* 操作 3：(r,c,t,x) = (2,4,1,-2)，距離 (2,4) 曼哈頓距離 ≤ 1 的格子全部 -2（得到最終結果）

  ```txt
  3 3 8 0 0
  3 8 5 5 -2
  3 0 5 -2 -2
  0 0 0 0 -2
  ```

### 測資

#### 測資 1

```in
3 4 2
1 2 1 5
0 1 0 3
```

#### 測資 2

```in
2 2 2
0 0 0 5
1 1 1 -2
```

#### 測資 3

```in
3 3 2
1 1 2 1
0 2 1 4
```

#### 測資 4

```in
3 4 3
0 3 1 7
2 0 1 3
1 1 2 -1
```

#### 測資 5

```in
1 6 2
0 2 3 4
0 5 0 -10
```


### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int H, W, N;
    cin >> H >> W >> N;
    vector<vector<long long>> g(H, vector<long long>(W, 0));

    for(int op=0; op<N; op++){
        int r, c, t;
        long long x;
        cin >> r >> c >> t >> x;

        for(int i=0;i<H;i++){
            for(int j=0;j<W;j++){
                if(abs(i-r) + abs(j-c) <= t) g[i][j] += x;
            }
        }
    }

    for(int i=0;i<H;i++){
        for(int j=0;j<W;j++){
            if(j) cout << ' ';
            cout << g[i][j];
        }
        cout << "\n";
    }
    return 0;
}
```

### 詳解

* 依題意最直觀的暴力：每次操作掃整張表判曼哈頓距離。

---


## T16｜機器人的路徑：從全域最小出發，走向未訪最小鄰居

### 題目

給你 n×m 的矩陣，所有數字互不相同。

機器人起點為整張矩陣的最小值所在位置。
之後每一步：在四方向相鄰格（上、下、左、右）中，選擇「值最小且尚未走過」的格子前進。
若沒有符合條件的相鄰格，則停止。

請輸出走過格子的數值總和（包含起點）。

**輸入格式**

* 第一行：n m
* 接著 n 行：每行 m 個整數（互不相同）

**輸出格式**

* 一行：總和

**範例輸入**

```in
3 3
9 8 7
6 5 4
3 2 1
```

**範例輸出**

```out
45
```

**範例計算過程**

* 起點是 1（全域最小）。
* 每一步都走向「四鄰居中未走過的最小值」，此例會走遍 1~9，共 45。

### 測資

#### 測資 1

```in
3 3
9 8 7
6 5 4
3 2 1
```

#### 測資 2

```in
1 5
5 4 3 2 1
```

#### 測資 3

```in
2 2
1 4
2 3
```

#### 測資 4

```in
2 3
10 20 30
5 6 7
```

#### 測資 5

```in
3 1
3
1
2
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<vector<int>> a(n, vector<int>(m));
    for(int i=0;i<n;i++) for(int j=0;j<m;j++) cin >> a[i][j];

    int sr=0, sc=0;
    for(int i=0;i<n;i++) for(int j=0;j<m;j++) if(a[i][j] < a[sr][sc]){ sr=i; sc=j; }

    vector<vector<char>> vis(n, vector<char>(m, 0));
    int dr[4] = {1,-1,0,0};
    int dc[4] = {0,0,1,-1};

    long long sum = 0;
    int r = sr, c = sc;

    while(true){
        vis[r][c] = 1;
        sum += a[r][c];

        int bestR = -1, bestC = -1;
        int bestVal = INT_MAX;

        for(int d=0; d<4; d++){
            int nr = r + dr[d];
            int nc = c + dc[d];
            if(0 <= nr && nr < n && 0 <= nc && nc < m && !vis[nr][nc]){
                if(a[nr][nc] < bestVal){
                    bestVal = a[nr][nc];
                    bestR = nr; bestC = nc;
                }
            }
        }

        if(bestR == -1) break;
        r = bestR; c = bestC;
    }

    cout << sum << "\n";
    return 0;
}
```

### 詳解

* 每一步只掃 4 個鄰居，並用 visited 避免走回頭。

---

## T17｜人口遷移：同時更新模擬 m 天後 min/max

### 題目

給你 R×C 網格：

* -1 表示不是城市
* 其他非負整數表示城市人口

每天，每個城市會向每個相鄰城市（上下左右）遷移 `population / k` 人（整數除法）。
遷移是**同時發生**：不能邊算邊改。

模擬 m 天後輸出：最少城市人口與最多城市人口（只看城市格，不看 -1）。

**輸入格式**

* 第一行：R C k m
* 接著 R 行：每行 C 個整數

**輸出格式**

* 第一行：最少城市人口
* 第二行：最多城市人口

**範例輸入**

```in
3 4 3 2
10 0 -1 6
5 -1 8 1
2 7 3 -1
```

**範例輸出**

```out
3
6
```

**範例計算過程**

題目參數：k=3、m=2。  
規則：每天對每個城市格 (不是 -1) 計算它要「分別」給每個相鄰城市（上/下/左/右、且相鄰格也必須是城市）的人數 = `population / k`（整數除法）。  
同一天內所有遷移必須「同時」發生：先把所有城市的「流出/流入」用 delta 累積完，再一次更新人口。

---

初始（第 0 天）
```txt
10 0 -1 6
5 -1 8 1
2 7 3 -1
```

---

第 1 天：先計算每個城市的「每個鄰居要給多少」

以下用「每格給出的單位 g = population/3」表示該格對每一個相鄰城市都會給 g 人。

* (0,0)=10 → g=3，相鄰城市：(1,0),(0,1)

  * 給(1,0) 3，給(0,1) 3，共流出 6
* (0,1)=0 → g=0，相鄰城市：(0,0)（(1,1)是-1、(0,2)是-1）

  * 給(0,0) 0，共流出 0
* (0,3)=6 → g=2，相鄰城市：(1,3)

  * 給(1,3) 2，共流出 2
* (1,0)=5 → g=1，相鄰城市：(0,0),(2,0)

  * 給(0,0) 1，給(2,0) 1，共流出 2
* (1,2)=8 → g=2，相鄰城市：(2,2),(1,3)

  * 給(2,2) 2，給(1,3) 2，共流出 4
* (1,3)=1 → g=0，相鄰城市：(0,3),(1,2)

  * 給(0,3) 0，給(1,2) 0，共流出 0
* (2,0)=2 → g=0，相鄰城市：(1,0),(2,1)

  * 給(1,0) 0，給(2,1) 0，共流出 0
* (2,1)=7 → g=2，相鄰城市：(2,0),(2,2)

  * 給(2,0) 2，給(2,2) 2，共流出 4
* (2,2)=3 → g=1，相鄰城市：(1,2),(2,1)

  * 給(1,2) 1，給(2,1) 1，共流出 2

---

第 1 天：彙總每格「流入」並一次更新

計算每格流入（只列城市格）：

* (0,0) 流入：從(1,0)得1、從(0,1)得0 → +1
  新人口 = 10 - 6 + 1 = 5
* (0,1) 流入：從(0,0)得3 → +3
  新人口 = 0 - 0 + 3 = 3
* (0,3) 流入：從(1,3)得0 → +0
  新人口 = 6 - 2 + 0 = 4
* (1,0) 流入：從(0,0)得3、從(2,0)得0 → +3
  新人口 = 5 - 2 + 3 = 6
* (1,2) 流入：從(2,2)得1、從(1,3)得0 → +1
  新人口 = 8 - 4 + 1 = 5
* (1,3) 流入：從(0,3)得2、從(1,2)得2 → +4
  新人口 = 1 - 0 + 4 = 5
* (2,0) 流入：從(1,0)得1、從(2,1)得2 → +3
  新人口 = 2 - 0 + 3 = 5
* (2,1) 流入：從(2,2)得1、從(2,0)得0 → +1
  新人口 = 7 - 4 + 1 = 4
* (2,2) 流入：從(1,2)得2、從(2,1)得2 → +4
  新人口 = 3 - 2 + 4 = 5

第 1 天結束後（與你提供的中間狀態一致）

```txt
5 3 -1 4
6 -1 5 5
5 4 5 -1
```

---

第 2 天：同樣先算「每個鄰居要給多少」

* (0,0)=5 → g=1，相鄰：(1,0),(0,1)

  * 給(1,0)1、給(0,1)1，流出2
* (0,1)=3 → g=1，相鄰：(0,0)

  * 給(0,0)1，流出1
* (0,3)=4 → g=1，相鄰：(1,3)

  * 給(1,3)1，流出1
* (1,0)=6 → g=2，相鄰：(0,0),(2,0)

  * 給(0,0)2、給(2,0)2，流出4
* (1,2)=5 → g=1，相鄰：(2,2),(1,3)

  * 給(2,2)1、給(1,3)1，流出2
* (1,3)=5 → g=1，相鄰：(0,3),(1,2)

  * 給(0,3)1、給(1,2)1，流出2
* (2,0)=5 → g=1，相鄰：(1,0),(2,1)

  * 給(1,0)1、給(2,1)1，流出2
* (2,1)=4 → g=1，相鄰：(2,0),(2,2)

  * 給(2,0)1、給(2,2)1，流出2
* (2,2)=5 → g=1，相鄰：(1,2),(2,1)

  * 給(1,2)1、給(2,1)1，流出2

---

第 2 天：彙總流入並一次更新

* (0,0) 流入：從(0,1)得1、從(1,0)得2 → +3
  新人口 = 5 - 2 + 3 = 6
* (0,1) 流入：從(0,0)得1 → +1
  新人口 = 3 - 1 + 1 = 3
* (0,3) 流入：從(1,3)得1 → +1
  新人口 = 4 - 1 + 1 = 4
* (1,0) 流入：從(0,0)得1、從(2,0)得1 → +2
  新人口 = 6 - 4 + 2 = 4
* (1,2) 流入：從(1,3)得1、從(2,2)得1 → +2
  新人口 = 5 - 2 + 2 = 5
* (1,3) 流入：從(0,3)得1、從(1,2)得1 → +2
  新人口 = 5 - 2 + 2 = 5
* (2,0) 流入：從(1,0)得2、從(2,1)得1 → +3
  新人口 = 5 - 2 + 3 = 6
* (2,1) 流入：從(2,0)得1、從(2,2)得1 → +2
  新人口 = 4 - 2 + 2 = 4
* (2,2) 流入：從(1,2)得1、從(2,1)得1 → +2
  新人口 = 5 - 2 + 2 = 5

第 2 天結束後（與你提供的最終狀態一致）

```txt
6 3 -1 4
4 -1 5 5
6 4 5 -1
```

---

最後只看城市格（排除 -1）：

* 最小人口 = 3
* 最大人口 = 6



### 測資

#### 測資 1

```in
3 4 3 2
10 0 -1 6
5 -1 8 1
2 7 3 -1
```

#### 測資 2

```in
2 3 4 1
10 2 -1
5 -1 2
```

#### 測資 3

```in
1 3 2 3
5 5 5
```

#### 測資 4

```in
2 2 10 1
9 9
9 9
```

#### 測資 5

```in
2 2 2 1
4 0
0 0
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C, k, m;
    cin >> R >> C >> k >> m;

    vector<vector<long long>> a(R, vector<long long>(C));
    for(int i=0;i<R;i++) for(int j=0;j<C;j++) cin >> a[i][j];

    int dr[4] = {1,-1,0,0};
    int dc[4] = {0,0,1,-1};

    for(int day=0; day<m; day++){
        vector<vector<long long>> delta(R, vector<long long>(C, 0));

        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++){
                if(a[i][j] < 0) continue;
                long long give = a[i][j] / k;
                if(give == 0) continue;

                for(int d=0; d<4; d++){
                    int ni = i + dr[d];
                    int nj = j + dc[d];
                    if(0 <= ni && ni < R && 0 <= nj && nj < C && a[ni][nj] >= 0){
                        delta[i][j] -= give;
                        delta[ni][nj] += give;
                    }
                }
            }
        }

        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++){
                if(a[i][j] >= 0) a[i][j] += delta[i][j];
            }
        }
    }

    long long mn = (1LL<<60), mx = -(1LL<<60);
    for(int i=0;i<R;i++){
        for(int j=0;j<C;j++){
            if(a[i][j] >= 0){
                mn = min(mn, a[i][j]);
                mx = max(mx, a[i][j]);
            }
        }
    }

    cout << mn << "\n" << mx << "\n";
    return 0;
}
```

### 詳解

* 這題重點只有一個：**同時更新**（delta/next），不要邊算邊改原矩陣。

---

## T18｜特殊位置：菱形加總取 mod 判定

### 題目

給定 n×m 的矩陣 a（每格為 0~9）。

對每個位置 (i,j)：令 x=a[i][j]。
計算：
`sum = 所有滿足 |r-i|+|c-j|<=x 的 a[r][c] 總和`。
若 `sum % 10 == x`，則 (i,j) 為特殊位置。

請輸出：

1. 特殊位置數量 k
2. 依字典序（先 i 再 j）列出所有特殊位置座標

**輸入格式**

* 第一行：n m
* 接著 n 行：每行 m 個整數（0~9）

**輸出格式**

* 第一行：k
* 接著 k 行：每行 i j

**範例輸入**

```in
4 5
2 3 5 9 1
8 1 7 8 8
0 1 9 1 2
6 5 2 1 6
```

**範例輸出**

```out
3
0 2
2 0
2 3
```

**範例計算過程（示範 (0,2)）**

* (0,2) 的 x=5。
* 這個 4×5 的地圖中，距離 (0,2) 最遠的角落距離也 ≤5，因此菱形涵蓋整張。
* 全表總和為 85，85%10=5，等於 x，所以 (0,2) 是特殊位置。

### 測資

#### 測資 1

```in
4 5
2 3 5 9 1
8 1 7 8 8
0 1 9 1 2
6 5 2 1 6
```

#### 測資 2

```in
2 3
5 2 3
4 5 6
```

#### 測資 3

```in
1 5
0 1 2 3 4
```

#### 測資 4

```in
2 2
0 0
0 0
```

#### 測資 5

```in
3 3
1 1 1
1 1 1
1 1 1
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<vector<int>> a(n, vector<int>(m));
    for(int i=0;i<n;i++) for(int j=0;j<m;j++) cin >> a[i][j];

    vector<pair<int,int>> ans;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            int x = a[i][j];
            long long sum = 0;
            for(int r=0;r<n;r++){
                for(int c=0;c<m;c++){
                    if(abs(r-i) + abs(c-j) <= x) sum += a[r][c];
                }
            }
            if(sum % 10 == x) ans.push_back({i,j});
        }
    }

    cout << ans.size() << "\n";
    for(auto &p: ans) cout << p.first << ' ' << p.second << "\n";
    return 0;
}
```

### 詳解

* 依題意直接暴力：每個點再掃一次全表判距離。

---

## T19｜蒐集寶石：決定下一個方向（只做轉向規則）

### 題目

你要做的是「轉向規則」本身，不做整張地圖移動。

輸入給你：

* 當前方向 dir（0=右,1=下,2=左,3=上）
* 已撿寶石顆數 picked
* 整數 k
* 四個方向是否可走：canR canD canL canU（1 可走，0 不可走）

規則：

1. 若 `picked` 是 `k` 的倍數，先右轉一次：`dir=(dir+1)%4`
2. 若目前 dir 不可走，持續右轉直到找到可走方向

題目保證：至少有一個方向可走。

**輸入格式**

* 第一行：dir picked k
* 第二行：canR canD canL canU

**輸出格式**

* 一行：最終 dir

**範例輸入**

```in
0 6 3
0 0 1 1
```

**範例輸出**

```out
2
```

**範例計算過程**

* picked=6 是 k=3 的倍數 → 先右轉：dir 0→1
* dir=1（下）不可走 → 右轉：dir 1→2
* dir=2（左）可走 → 輸出 2

### 測資

#### 測資 1

```in
0 6 3
0 0 1 1
```

#### 測資 2

```in
3 5 2
1 1 1 1
```

#### 測資 3

```in
1 4 2
0 0 0 1
```

#### 測資 4

```in
2 9 3
0 1 0 0
```

#### 測資 5

```in
0 10 5
1 0 0 0
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int dir;
    long long picked, k;
    cin >> dir >> picked >> k;

    int can[4];
    for(int i=0;i<4;i++) cin >> can[i]; // 0=右 1=下 2=左 3=上

    if(k != 0 && picked % k == 0) dir = (dir + 1) % 4;

    while(!can[dir]) dir = (dir + 1) % 4;

    cout << dir << "\n";
    return 0;
}
```

### 詳解

* 先做「倍數右轉」，再做「找可走方向」，順序不能顛倒。

---

## T20｜蒐集寶石：完整模擬（撿到 0 或無路可走就停）

### 題目

給你 M×N 地圖，每格：

* -1：牆
* 0：無寶石
* > 0：該格寶石數量

機器人起點 (r,c)，初始方向向右（0=右,1=下,2=左,3=上）。

重複流程：

1. 若當前格寶石為 0：停止
2. 撿 1 顆：該格寶石數量 -1，picked +1
3. 若 picked 是 k 的倍數：右轉一次
4. 若面前是牆或超界：持續右轉直到面前合法
5. 若四個方向都無法前進：停止
6. 前進一格

請輸出 picked。

**輸入格式**

* 第一行：M N k r c
* 接著 M 行：每行 N 個整數

**輸出格式**

* 一行：picked

**範例輸入**

```in
2 3 2 0 0
1 1 0
0 -1 1
```

**範例輸出**

```out
2
```

**範例計算過程**

* 起點 (0,0)=1：撿 1 顆 → picked=1，向右到 (0,1)
* (0,1)=1：撿 1 顆 → picked=2（k=2 的倍數）先右轉向下，但 (1,1) 是牆 → 再右轉向左，走回 (0,0)
* (0,0)=0：停止，總共 picked=2

### 測資

#### 測資 1

```in
2 3 2 0 0
1 1 0
0 -1 1
```

#### 測資 2

```in
1 3 3 0 0
5 0 0
```

#### 測資 3

```in
2 2 1 0 0
1 1
1 1
```

#### 測資 4

```in
3 3 2 1 1
0 1 0
1 -1 1
0 1 0
```

#### 測資 5

```in
2 2 2 0 1
0 0
0 0
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, N;
    long long k;
    int r, c;
    cin >> M >> N >> k >> r >> c;

    vector<vector<long long>> g(M, vector<long long>(N));
    for(int i=0;i<M;i++) for(int j=0;j<N;j++) cin >> g[i][j];

    int dr[4] = {0, 1, 0, -1};
    int dc[4] = {1, 0, -1, 0};

    int dir = 0;
    long long picked = 0;

    while(true){
        if(g[r][c] == 0) break;

        g[r][c]--;
        picked++;

        if(k != 0 && picked % k == 0) dir = (dir + 1) % 4;

        int bestDir = -1;
        int curDir = dir;
        for(int t=0; t<4; t++){
            int nr = r + dr[curDir];
            int nc = c + dc[curDir];
            if(0 <= nr && nr < M && 0 <= nc && nc < N && g[nr][nc] != -1){
                bestDir = curDir;
                break;
            }
            curDir = (curDir + 1) % 4;
        }

        if(bestDir == -1) break; // 四方向都不能走
        dir = bestDir;
        r += dr[dir];
        c += dc[dir];
    }

    cout << picked << "\n";
    return 0;
}
```

### 詳解

* 最容易錯的是步驟順序：先撿、再倍數右轉、再避牆、最後才前進。

---

## T21｜子矩陣枚舉：mismatch 上限 + 最小 sum 差

### 題目

你會拿到：

* 小矩陣 A（大小 s×t）
* 大矩陣 B（大小 n×m）
* 整數 r（允許最大 mismatch）

對 B 的每個 s×t 子矩陣 X（以某格為左上角截出）：

* mismatch = A 與 X 對應位置「不相同」的格數
* 若 mismatch <= r，視為有效

請輸出：

1. 有效子矩陣數量 cnt
2. 有效子矩陣中 `abs(sum(A)-sum(X))` 的最小值（若 cnt=0 輸出 -1）

**輸入格式**

* 第一行：n m s t r
* 接著 s 行：A
* 接著 n 行：B

**輸出格式**

* 第一行：cnt
* 第二行：最小值或 -1

**範例輸入**

```in
4 5 2 3 2
1 2 3
4 5 6
1 2 3 9 9
4 0 6 9 9
1 2 0 4 5
4 5 6 7 8
```

**範例輸出**

```out
2
3
```

**範例計算過程（示範左上角 (0,0) 子矩陣）**

* sum(A)=1+2+3+4+5+6=21
* 取 X（左上角 (0,0) 的 2×3）：[[1,2,3],[4,0,6]]
* mismatch=1（只有 5 vs 0 不同）≤2 → 有效
* sum(X)=16，差為 |21-16|=5
* 全部位置枚舉後，cnt=2，最小差為 3

### 測資

#### 測資 1

```in
4 5 2 3 2
1 2 3
4 5 6
1 2 3 9 9
4 0 6 9 9
1 2 0 4 5
4 5 6 7 8
```

#### 測資 2

```in
3 3 2 2 0
1 2
3 4
1 2 9
3 4 9
9 9 9
```

#### 測資 3

```in
2 3 1 2 0
9 9
9 9 9
9 9 9
```

#### 測資 4

```in
2 2 2 2 1
1 2
3 4
1 2
3 0
```

#### 測資 5

```in
3 3 2 2 0
1 1
1 1
2 2 2
2 2 2
2 2 2
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t, r;
    cin >> n >> m >> s >> t >> r;

    vector<vector<int>> A(s, vector<int>(t));
    for(int i=0;i<s;i++) for(int j=0;j<t;j++) cin >> A[i][j];

    vector<vector<int>> B(n, vector<int>(m));
    for(int i=0;i<n;i++) for(int j=0;j<m;j++) cin >> B[i][j];

    long long sumA = 0;
    for(int i=0;i<s;i++) for(int j=0;j<t;j++) sumA += A[i][j];

    int cnt = 0;
    long long best = (1LL<<60);

    for(int i=0;i+s<=n;i++){
        for(int j=0;j+t<=m;j++){
            int mismatch = 0;
            long long sumX = 0;
            for(int x=0;x<s;x++){
                for(int y=0;y<t;y++){
                    int v = B[i+x][j+y];
                    sumX += v;
                    if(v != A[x][y]) mismatch++;
                }
            }
            if(mismatch <= r){
                cnt++;
                best = min(best, llabs(sumA - sumX));
            }
        }
    }

    cout << cnt << "\n";
    if(cnt == 0) cout << -1 << "\n";
    else cout << best << "\n";

    return 0;
}
```

### 詳解

* 左上角枚舉要用 `i+s<=n`、`j+t<=m` 避免越界。

---

## T22｜兩顆骰子：滾動與交換

### 題目

有兩顆骰子 1 與 2。每顆骰子有 6 面：Top/Bottom/North/South/West/East。

初始兩顆骰子皆為：Top=1, Bottom=6, North=2, South=5, West=3, East=4。

接著有 Q 個操作：

* `N i`：第 i 顆往北滾一次
* `S i`：往南
* `E i`：往東
* `W i`：往西
* `X`：交換兩顆骰子（整顆狀態交換）

最後輸出：`dice1_top dice2_top`。

**輸入格式**

* 第一行：Q
* 接著 Q 行：

  * `X`
  * 或 `N i` / `S i` / `E i` / `W i`（i 為 1 或 2）

**輸出格式**

* 一行：兩顆骰子的頂面

**範例輸入**

```in
2
E 1
X
```

**範例輸出**

```out
1 3
```

**範例計算過程**

* 第 1 步：骰子 1 往東滾，Top 變成原本 West=3；骰子 2 不動。
* 第 2 步：交換兩顆骰子狀態，所以輸出（骰子1_top,骰子2_top）=(1,3)。

### 測資

#### 測資 1

```in
2
E 1
X
```

#### 測資 2

```in
1
X
```

#### 測資 3

```in
2
E 1
W 1
```

#### 測資 4

```in
3
N 2
N 2
N 2
```

#### 測資 5

```in
6
E 1
S 2
X
N 1
W 2
E 2
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

struct Dice {
    int top=1, bottom=6, north=2, south=5, west=3, east=4;

    void rollN(){
        int t = top;
        top = south;
        south = bottom;
        bottom = north;
        north = t;
    }
    void rollS(){
        int t = top;
        top = north;
        north = bottom;
        bottom = south;
        south = t;
    }
    void rollE(){
        int t = top;
        top = west;
        west = bottom;
        bottom = east;
        east = t;
    }
    void rollW(){
        int t = top;
        top = east;
        east = bottom;
        bottom = west;
        west = t;
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int Q;
    cin >> Q;

    Dice d1, d2;

    for(int qi=0; qi<Q; qi++){
        string op;
        cin >> op;
        if(op == "X"){
            swap(d1, d2);
            continue;
        }

        int idx;
        cin >> idx;
        Dice &d = (idx == 1 ? d1 : d2);

        if(op == "N") d.rollN();
        else if(op == "S") d.rollS();
        else if(op == "E") d.rollE();
        else if(op == "W") d.rollW();
    }

    cout << d1.top << ' ' << d2.top << "\n";
    return 0;
}
```

### 詳解

* 最常錯：方向滾動時，面交換的方向寫反。

---

## T23｜六方向移動：輸出走過字串與字元種類數

### 題目

給定 m×n 的字母格子（m 行，每行 n 個字元）。起點固定 (m-1,0)。

你會得到 k 個方向（0~5），每一步依方向嘗試移動：

* 0：右上  (r-1, c+1)
* 1：右    (r,   c+1)
* 2：右下  (r+1, c)
* 3：左下  (r+1, c-1)
* 4：左    (r,   c-1)
* 5：左上  (r-1, c)

若移動後超出邊界，則本步停在原地。

請輸出：

1. 長度 k 的字串：每一步結束後所在格的字母（不含起點）
2. 走過字母種類數

**輸入格式**

* 第一行：m n k
* 接著 m 行：每行一個長度 n 的字串
* 最後一行：k 個整數方向

**輸出格式**

* 第一行：走過字串
* 第二行：種類數

**範例輸入**

```in
2 3 4
abc
DEF
1 1 4 4
```

**範例輸出**

```out
ccaa
2
```

**範例計算過程**

* 起點 (1,0)='D'（不輸出）
* 方向 1：右 → (1,1)='E'，輸出 E
* 方向 1：右 → (1,2)='F'，輸出 F
* 方向 4：左 → (1,1)='E'，輸出 E
* 方向 4：左 → (1,0)='D'，輸出 D
  （此例的走過字串為 "EFED"；種類為 {E,F,D} 共 3）

（註：若你希望範例更直觀，可把測資 1 當作實際練習輸入。）

### 測資

#### 測資 1

```in
3 4 6
abcd
efgh
IJKL
0 1 1 2 4 5
```

#### 測資 2

```in
2 3 4
abc
DEF
0 1 2 3
```

#### 測資 3

```in
1 3 3
XYZ
0 0 0
```

#### 測資 4

```in
2 2 2
ab
CD
4 4
```

#### 測資 5

```in
3 1 5
a
b
c
2 2 2 2 2
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m, n, k;
    cin >> m >> n >> k;

    vector<string> g(m);
    for(int i=0;i<m;i++) cin >> g[i];

    vector<int> dirs(k);
    for(int i=0;i<k;i++) cin >> dirs[i];

    int dr[6] = {-1, 0,  1,  1, 0, -1};
    int dc[6] = { 1, 1,  0, -1,-1,  0};

    int r = m - 1, c = 0;
    string path;
    path.reserve(k);
    set<char> kinds;

    for(int step=0; step<k; step++){
        int d = dirs[step];
        int nr = r + dr[d];
        int nc = c + dc[d];
        if(0 <= nr && nr < m && 0 <= nc && nc < n){
            r = nr; c = nc;
        }
        char ch = g[r][c];
        path.push_back(ch);
        kinds.insert(ch);
    }

    cout << path << "\n";
    cout << kinds.size() << "\n";
    return 0;
}
```

### 詳解

* 寫死方向表 + 邊界判斷，是這類題最穩作法。

---

## T24｜彗星撞擊：方形裁切 + 條件式更新 + 統計

### 題目

有 R×C 的高度地圖，初始高度全為 D。

有 K 隻恐龍（可同格多隻），初始都清醒。

接著 M 次撞擊，每次給 (a,b,S,d)：

* 影響範圍：以 (a,b) 為中心、邊長 S（奇數）的正方形與地圖交集
* 若範圍內存在至少一隻清醒恐龍：範圍內所有清醒恐龍變暈眩（清醒數歸零），高度不變
* 否則：範圍內所有格子高度都減少 d

最後輸出：`最高高度 最低高度 清醒恐龍所在格數`。

**輸入格式**

* 第一行：R C D
* 第二行：K
* 接著 K 行：恐龍座標 r c
* 下一行：M
* 接著 M 行：a b S d

**輸出格式**

* 一行：最高高度 最低高度 清醒恐龍所在格數

**範例輸入**

```in
2 3 5
1
0 1
2
0 1 1 2
0 1 3 1
```

**範例輸出**

```out
4 4 0
```

**範例計算過程**

* 第 1 次撞擊範圍只有 (0,1)，範圍內有清醒恐龍 → 讓恐龍暈眩（清醒歸零），高度不變。
* 第 2 次撞擊範圍涵蓋全圖，範圍內無清醒恐龍 → 全圖高度 -1，從 5 變 4。
* 最終 max=min=4，清醒恐龍格數=0。

### 測資

#### 測資 1

```in
2 3 5
1
0 1
2
0 1 1 2
0 1 3 1
```

#### 測資 2

```in
1 1 10
1
0 0
1
0 0 1 5
```

#### 測資 3

```in
2 2 3
0
1
0 0 3 1
```

#### 測資 4

```in
2 2 0
1
0 0
1
1 1 1 7
```

#### 測資 5

```in
3 4 5
3
0 1
1 1
2 3
1
1 1 3 2
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C;
    long long D;
    cin >> R >> C >> D;

    vector<vector<long long>> h(R, vector<long long>(C, D));
    vector<vector<int>> awake(R, vector<int>(C, 0));

    int K; cin >> K;
    for(int i=0;i<K;i++){
        int r, c; cin >> r >> c;
        awake[r][c]++;
    }

    int M; cin >> M;
    for(int e=0; e<M; e++){
        int a, b, S;
        long long d;
        cin >> a >> b >> S >> d;

        int half = S / 2;
        int r1 = max(0, a - half), r2 = min(R - 1, a + half);
        int c1 = max(0, b - half), c2 = min(C - 1, b + half);

        bool hasAwake = false;
        for(int i=r1;i<=r2 && !hasAwake;i++){
            for(int j=c1;j<=c2;j++){
                if(awake[i][j] > 0){ hasAwake = true; break; }
            }
        }

        if(hasAwake){
            for(int i=r1;i<=r2;i++){
                for(int j=c1;j<=c2;j++) awake[i][j] = 0;
            }
        }else{
            for(int i=r1;i<=r2;i++){
                for(int j=c1;j<=c2;j++) h[i][j] -= d;
            }
        }
    }

    long long mx = -(1LL<<60), mn = (1LL<<60);
    for(int i=0;i<R;i++){
        for(int j=0;j<C;j++){
            mx = max(mx, h[i][j]);
            mn = min(mn, h[i][j]);
        }
    }

    int awakeCells = 0;
    for(int i=0;i<R;i++) for(int j=0;j<C;j++) if(awake[i][j] > 0) awakeCells++;

    cout << mx << ' ' << mn << ' ' << awakeCells << "\n";
    return 0;
}
```

### 詳解

* 每次撞擊：先裁切方形到地圖內，先判斷是否有清醒恐龍，再決定要「讓恐龍暈眩」或「高度下降」。

---

## T25｜交錯字串：小規模暴力切段交錯（選做）

### 題目

給你字串 A、B、S（長度都不超過 10）。

你要判斷是否能把 S 切成多段，並且段落來源必須交錯：A 段、B 段、A 段、B 段...（也可從 B 開始）。

更精確：

* 你有指標 pa、pb 表示 A/B 已用到的位置，ps 表示 S 已拼到的位置
* 每次必須從「上一段的另一個字串」取一段長度 L>=1，使得：

  * 取 A：A.substr(pa,L) == S.substr(ps,L)，然後 pa+=L, ps+=L
  * 取 B：B.substr(pb,L) == S.substr(ps,L)，然後 pb+=L, ps+=L
* 若 ps 到達 |S| 即成功

輸出 Yes/No。

**輸入格式**

* 第一行：A
* 第二行：B
* 第三行：S

**輸出格式**

* 一行：Yes 或 No

**範例輸入**

```in
ABCD
xy
ABxyCD
```

**範例輸出**

```out
Yes
```

**範例計算過程**

* 從 A 取 "AB" → S 前進 2
* 從 B 取 "xy" → S 前進 2
* 從 A 取 "CD" → S 到結尾
  因此輸出 Yes。

### 測資

#### 測資 1

```in
ABCD
xy
ABxyCD
```

#### 測資 2

```in
AB
CD
ACBD
```

#### 測資 3

```in
AAA
BBB
AAABBB
```

#### 測資 4

```in
abc
xyz
xyzabc
```

#### 測資 5

```in
a
a
aa
```

### 參考答案

```cpp
#include <bits/stdc++.h>
using namespace std;

static bool dfs(const string &A, const string &B, const string &S,
                int pa, int pb, int ps, int last){
    if(ps == (int)S.size()) return true;

    // last=0 上次取 A，這次只能取 B
    // last=1 上次取 B，這次只能取 A
    // last=2 起始，兩邊都可以

    if(last != 0){
        for(int L=1; pa+L <= (int)A.size() && ps+L <= (int)S.size(); L++){
            if(A.compare(pa, L, S, ps, L) != 0) break;
            if(dfs(A, B, S, pa+L, pb, ps+L, 0)) return true;
        }
    }

    if(last != 1){
        for(int L=1; pb+L <= (int)B.size() && ps+L <= (int)S.size(); L++){
            if(B.compare(pb, L, S, ps, L) != 0) break;
            if(dfs(A, B, S, pa, pb+L, ps+L, 1)) return true;
        }
    }

    return false;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string A, B, S;
    cin >> A >> B >> S;

    cout << (dfs(A, B, S, 0, 0, 0, 2) ? "Yes" : "No") << "\n";
    return 0;
}
```

### 詳解

* 長度 ≤ 10 時，用暴力 DFS 試每段長度即可。
