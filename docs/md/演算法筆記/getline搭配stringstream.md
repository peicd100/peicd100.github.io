
# getline搭配stringstream

> 這邊講解cin、getline的運作方式

## 總結

cin會將分割元素捨去，getline不會

## cin

>從左至右忽略所有「`' '`或是`'\n'`」，當遇到非「`' '`或是`'\n'`」時認作**輸入目標**，直到再次遇到「`' '`或是`'\n'`」時，停止認作**輸入目標**，將**輸入目標**及**輸入目標**之前的所有元素捨棄。

假設一開始的緩衝區為
```
" \n  \n   \n  123  \n 4 5"
```
執行以下程式
```
cin>>n;
```
緩衝區會從這樣
```
" \n  \n   \n  123  \n 4 5"
```
變為這樣
```
"  \n 4 5"
```
而輸入目標(n)為
```
"123"
```


過程圖示：
![alt text](../images/getline搭配stringstream/image-18.png)
---


```cpp  
#include <bits/stdc++.h>
using namespace std;
int main(){
    istringstream cin(" \n  \n   \n  123  \n 4 5");
    int n;
    cin>>n;
    cout<<n;
}
```

/// html | div.result
```
123
```
///

## getline

### 介紹

>`getline(輸入流,字串);`   
`getline(輸入流,字串,分割元素);`   
```
getline(cin,s);
getline(cin,s,'2');
```

- 輸入流種類：  
    cin  
    stringstream  
    istringstream  
- 字串種類：  
    必須是string  
- 分割元素種類：  
    必須是char  



> 分割元素可以選擇要不要打，若沒有打，分割元素預設為`'\n'`。  
> 如果打了字元，會將分割元素變更為該字元

範例：
```
getline(cin,s);     //遇到'\n'分割
getline(cin,s,'2');  //遇到'2'分割
```



### 運作



> 從左至右將所有元素認作輸入目標，直到遇到**分割元素**，將**分割元素**以及**分割元素**之前所有元素捨棄。


#### 1. 不選擇分割元素

假設一開始的緩衝區為
```
"545 1 \n 1 2 3"
```
執行以下程式
```
getline(cin,s);
```
緩衝區會從這樣
```
"545 1 \n 1 2 3"
```
變為這樣
```
" 1 2 3"
```
而輸入目標(s)為
```
"545 1 "
```

過程圖示：
![alt text](images/getline搭配stringstream/image.png)
---
```cpp  
#include <bits/stdc++.h>
using namespace std;
int main(){
    istringstream cin("545 1 \n 1 2 3");
    string s;
    getline(cin,s);
    cout<<s<<";";
}
```

/// html | div.result
```
545 1 ;
```
///
#### 2. 選擇分割元素

假設緩衝區
```
"545 1 \n 1 2 3"
```
執行程式
```
getline(cin,s,'2');
```
緩衝區會從
```
"545 1 \n 1 2 3"
```
變為
```
" 3"
```
而輸入目標(s)為
```
"545 1 \n 1 "
```

過程圖示：
![alt text](../images/getline搭配stringstream/image-20.png)
---

```cpp  
#include <bits/stdc++.h>
using namespace std;
int main(){
    istringstream cin("545 1 \n 1 2 3");
    string s;
    getline(cin,s,'2');
    cout<<s<<";";
}
```

/// html | div.result
```
545 1
 1 ;
```
///
>注意到了嗎
>因為s中有換行符號，所以會換行

## 要注意的情形
>有時候getline配合cin使用，會是空字串，原因如下：


假設緩衝區為
```
"1\n2 3 4\n5 6 7"
```
也就是
```
1
2 3 4
5 6 7
```

執行程式
```
cin>>n;
```
緩衝區從
```
"1\n2 3 4\n5 6 7"
```
變為
```
"\n2 3 4\n5 6 7"
```
而輸入目標(n)為
```
"1"
```
執行程式
```
getline(cin,s);
```
緩衝區從
```
"\n2 3 4\n5 6 7"
```
變為
```
"2 3 4\n5 6 7"
```
而輸入目標(s)為
```
""
```

這時候s不會有任何東西(因為`\n`前面沒有東西)，為空字串，需要注意!!!

>總而言之，cin會丟掉分割元素，getline不會


## 實作：不知道數量的問題

當遇到問題：  
第一行給定數字n  
第二行給定未知數量數字  
請將第二行所有數字加總後乘以n輸出  



範例輸入：
5
1 2 3 7 8 9 4 5 6 4

範例輸出：
245

範例講解:
(1+2+3+7+8+9+4+5+6+4)*5=245


```cpp  
#include <bits/stdc++.h>
using namespace std;
#define nn "\n"
int main(){
    istringstream cin("5\n1 2 3 7 8 9 4 5 6 4");
    int n;
    cin>>n;
    string s;
    getline(cin,s);//此時s為空字串，以\n分割
    getline(cin,s);//此時s才有東西，以\n分割
    stringstream ss(s);
    int sum=0;
    while(getline(ss,s,' ')){//以空格分割
        sum+=s[0]-'0';
    }
    cout<<sum*n;
}

```


