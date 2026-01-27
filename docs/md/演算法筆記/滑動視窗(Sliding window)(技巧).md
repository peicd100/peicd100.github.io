# 滑動視窗(Sliding window)(技巧)


> 基本上是以兩個指標維護一段區間，然後逐步將這區間從前往後(從左往右)移動。維護兩個指標這一類的方法也有 人稱為雙指標法，但也包含兩個指標從兩端往中間移動(ap325)



## d031: 例題 P-3-7. 正整數序列之最接近的區間和
https://judge.tcirc.tw/ShowProblem?problemid=d031

輸入一個正整數序列  (A\[1\],A\[2\],...,A\[n\])   ，另外給了一個非負整數  K    ，請計算哪些連續區段的和最接近  K    而不超過  K   ，以及這樣的區間有幾個。

 n   不超過 20 萬，輸入數字與  K    皆不超過 10 億。
 
 
 
輸入說明  
第一行是  n   與  K   ，  
第二行  n   個整數是  A\[i\]  ，同行數字以空白間隔。  
  
  
輸出說明  
第一行輸出最接近  K    但不超過  K    的和，  
第二行輸出這樣的區間有幾個  
  
範例輸入：   
5 10     
4 3 1 7 4   
  
範例輸出：    
8   
2   


> 這題是用兩個指針一直維持一個區間，右指針不停往右移動，透過縮小/放大(移動左指針)區間來維持條件
> 
> 
> 移動右指針方法可以用類似貪心演算法的方式
> 因為只會往右一個位置，用for迴圈比較方便


/// collapse-code  
```cpp title="code"
#include <bits/stdc++.h>
using namespace std;
#define nn "\n"
int v[300000];
int main(){
  int n,m,ans=0;
  cin>>n>>m;
  for(int i=0;i<n;i++){
    cin>>v[i];
  }
  int sum=0;
  map<int,int>mp;
  for(int l=0,r=0;r<n;r++){
    sum+=v[r];
    while(sum>m){
      sum-=v[l];
      l++;
    }
    mp[sum]++;
  }
  cout<<nn<<mp.rbegin()->first;   //輸出最後一個的first
  cout<<nn<<mp.rbegin()->second;  //輸出最後一個的second
}
```
///


## [a175: P-3-8. 固定長度區間的最大區段差](https://judge.tcirc.tw/problem/d032)

內容   
對於序列的一個連續區段來說，區段差是指區段內的最大值減去區段內的最小值。   
   
有N個非負整數組成的序列seq，請計算在所有長度為L的連續區段中，最大的區段差為何。   
   
輸入說明   
第一行是N與L，第二行是序列內容，相鄰數字間以空白隔開。   
   
L≤N≤2e5，數字不超過1e9。   
   
輸出說明   
輸出所求的最大區間差。   
   
範例輸入 #1   
9 4   
1 4 3 6 9 8 5 7 1   
範例輸出 #1   
7   

### multiset解法
會有重複所以用multiset

/// collapse-code  
```cpp title="multiset"
#include<bits/stdc++.h>
using namespace std;
#define pii pair<int,int>
#define all(x) x.begin(),x.end()
#define nn "\n"
#define int long long


signed main(){
    //istringstream cin("9 4 \
1000 4 3 1 9 1 5 7 100");
    int n,m;
    cin>>n>>m;


    vector<int>v(n);

    for(int i=0;i<n;i++){
        cin>>v[i];
    }


    multiset<int>s;



    // 初始化前 m 個元素
    for (int i = 0; i < m; i++) {
        s.insert(v[i]);
    }

    int ans=-1;

    ans=max(ans,abs(*s.begin()-*s.rbegin()));

    for(int i=m;i<n;i++){
        s.insert(v[i]);
        auto it=s.find(v[i-m]);
        s.erase(it);

        ans=max(ans,abs(*s.begin()-*s.rbegin()));
    }

    cout<<ans;

}
```
///


### deque解法
<iframe width="718" height="404" src="https://www.youtube.com/embed/WP_nm-zFxMQ" title="滑動視窗queue" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>



/// collapse-code  
```cpp title="deque：from AP325"
#include<bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;
    vector<int> v(n);

    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    deque<int> madq;  // 維護最大值的雙端佇列
    deque<int> midq;  // 維護最小值的雙端隊列

    int ans = INT_MIN;

    for (int i = 0; i < n; i++) {
        // 維護最大值隊列
        if (!madq.empty() && madq.front() <= i - m) {
            madq.pop_front();
        }
        while (!madq.empty() && v[madq.back()] <= v[i]) {
            madq.pop_back();
        }
        madq.push_back(i);

        // 維護最小值隊列
        if (!midq.empty() && midq.front() <= i - m) {
            midq.pop_front();
        }
        while (!midq.empty() && v[midq.back()] >= v[i]) {
            midq.pop_back();
        }
        midq.push_back(i);

        // 當視窗的大小達到m時，計算目前的最大區段差
        if (i >= m - 1) {
            ans = max(ans, v[madq.front()] - v[midq.front()]);
        }
    }

    cout << ans << endl;

    return 0;
}

```
///


/// collapse-code  
```cpp title="deque：自己寫"
#include<bits/stdc++.h>
using namespace std;

struct st{
    int x,y; //value,index
};

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n,m,ans=INT_MIN;
    cin>>n>>m;

    deque<st>dqma;
    deque<st>dqmi;


    for(int i=0;i<n;i++){
        int x;
        cin>>x;

        if(!dqma.empty() && i-dqma.front().y>=m){
            dqma.pop_front();
        }
        while(!dqma.empty() &&dqma.back().x<x){
            dqma.pop_back();
        }
        dqma.push_back({x,i});


        if(!dqmi.empty() &&i-dqmi.front().y>=m){
            dqmi.pop_front();
        }
        while(!dqmi.empty() &&dqmi.back().x>x){
            dqmi.pop_back();
        }
        dqmi.push_back({x,i});
        
        ans=max(ans,dqma.front().x-dqmi.front().x);
    }

    cout<<ans;
    return 0;
}
```
///