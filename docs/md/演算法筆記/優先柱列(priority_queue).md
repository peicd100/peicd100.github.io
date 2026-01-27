# 優先柱列(priority_queue)
## 優先柱列(priority_queue)

> 需要一直排序，取用最大值，就使用pq最快
> 
> 可以想成會自動排序的stack(堆疊)
> 
> 「優先」顧名思義就是最大的在前面
> 如果要小的在前面就變成負值

> 例如：

/// collapse-code  
```cpp title="coode"
#include<bits/stdc++.h>
using namespace std;
priority_queue<int>pq_1;
priority_queue<int>pq_2;
int main(){
    istringstream cin("8 7 9");
    
    for(int i=0;i<3;i++){
        int x;
        cin>>x;
        pq_1.push(x);
        pq_2.push(-x);     //負號處裡
    }

    while(!pq_1.empty()){
        cout<<pq_1.top();
        pq_1.pop();
    }
    cout<<"\n";
    while(!pq_2.empty()){
        cout<<-pq_2.top();  //負號處裡
        pq_2.pop();
    }
}
```
///

或是使用greater

/// collapse-code  
```cpp  
#include<bits/stdc++.h>
using namespace std;

priority_queue<int> pq_1; // 默認從大到小排列
priority_queue<int, vector<int>, greater<int>> pq_2; // 使用 greater<int> 從小到大排列

int main(){
    istringstream cin("8 7 9");
    
    for(int i = 0; i < 3; i++){
        int x;
        cin >> x;
        pq_1.push(x);
        pq_2.push(x); // 不需要手動處理負號
    }

    while(!pq_1.empty()){
        cout << pq_1.top();
        pq_1.pop();
    }
    cout << "\n";

    while(!pq_2.empty()){
        cout << pq_2.top(); // 不需要手動處理負號
        pq_2.pop();
    }
}

```
///
/// html | div.result
```
987
789
```
///

> 可以看到輸出第一行為大到小  
> 輸出第二行為小到大


