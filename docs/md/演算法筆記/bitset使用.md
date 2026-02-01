# bitset使用


> From 2024 IONC

細心的讀者可能會發現 `bool` 這個型別明明只能表示 `true` 或 `false`，通常卻佔了 1 Byte 的記憶體空間。這主要的原因是因為電腦的架構通常不需要也很難去操作 1 bit 的空間。單純宣告一個 `bool` 影響可能不大，但若是宣告 `bool` 陣列可能會造成很多記憶體的浪費。因此 STL 就包含了一個好用的工具 `bitset` 可以宣告固定長度的 bits。

基本上你可以把 `bitset` 當成一個效率很快的 `bool` 陣列，而越低位是在 `bitset` 的越右邊。`bitset` 也支援位元運算。也能將 `bitset` 轉換成 `string` 或 `unsigned integer`。通常在 `bitset` 上做操作的時間是 `vector<bool>` 的 $\frac{1}{32}$ 倍。


/// collapse-code 
```cpp
#include<bits/stdc++.h>
using namespace std;

int  main(){
    bitset<5> b; // 宣告大小為 5 的 bitset 初始為 00000
    cout<<"b: "<<b<<"\n";

    b[0] = 1; // 將第 0 個 bit 設為 1 也就是 bitset 變成了 00001
    cout<<"b: "<<b<<"\n";

    b.reset(); // set all bits to 0
    cout<<"b: "<<b<<"\n";

    b.set(); // set all bits to 1
    cout<<"b: "<<b<<"\n";

    bitset<5> a(10011);
    cout<<"a.count(): " << a.count() << '\n'; // 輸出 bitset 中有幾個 1
    cout<<"a: "<<a<<"\n";

    b=5;
    cout<<"b: "<<b<<"\n";

    cout<<"(a & b): " << (a & b) << endl; // 因為運算子優先順序的關係，() 是必須的

    string str = a.to_string();
    unsigned long val = a.to_ulong();
    cout<<"a: "<<str<<"\n";

    bitset<20> c=10;
    cout<<c;
}
```


///