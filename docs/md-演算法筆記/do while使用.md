# do while使用
> while 是先判斷，再重複執行「要執行的內容」

>而 do wheile 是先執行「要執行的內容」再進行判斷，接著重複執行「要執行的內容」

## 使用時機

>假設要製作一個簡易加法計算機：

系統先輸出`Enter two numbers`
輸入兩個數字，輸出相加結果，並提供防呆機制：若其中一個數字輸入為字母，就持續輸出`Enter two numbers`並讓使用者重新輸入。

範例輸入：
1 a  
a 1  
a a  
1 1  

範例輸出：
Enter two numbers  
Enter two numbers  
Enter two numbers  
Enter two numbers  
2  

> 用while做：

```cpp title="code"
#include<bits/stdc++.h>
using namespace std;

#define nn "\n"

int main(){
    char c[3]="";
    cout<<"Enter two numbers"<<nn;
    cin>>c[0]>>c[1]; //先輸入
    while((!isdigit(c[0])) || (!isdigit(c[1])) ){ //判斷一次
        cout<<"Enter two numbers"<<nn;
        cin>>c[0]>>c[1];  //輸入第二次
    }
    cout<<c[0]-'0'+c[1]-'0'<<nn;
}
```

> 用do while做：

```cpp title="code"
#include<bits/stdc++.h>
using namespace std;

#define nn "\n"

int main(){
    char c[3]="";
    do{
        cout<<"Enter two numbers"<<nn;
        cin>>c[0]>>c[1];
    }while((!isdigit(c[0])) || (!isdigit(c[1])));

    cout<<c[0]-'0'+c[1]-'0'<<nn;
}
```

>可以發現，差別就是do while在執行第一次之後才判斷。