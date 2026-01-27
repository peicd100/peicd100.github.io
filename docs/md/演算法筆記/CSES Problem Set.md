# CSES Problem Set

網址： https://cses.fi/problemset/
(Sort By Number of Solvers)


## Introductory Problems

### Weird Algorithm

/// collapse-code  
```cpp  
#include<bits/stdc++.h>
using namespace std;
#define int long long 
signed main(){
    // istringstream cin("3");
    int n;
    cin>>n;
    while(n!=1){
        cout<<n<<" ";
        if(n&1){//odd
            n=n*3+1;
        }
        else{
            n/=2;
        }
    }
    cout<<1;
}
```
///


### Missing Number

/// collapse-code  
```cpp  
#include<bits/stdc++.h>
using namespace std;
#define int long long 
#define N 200000
#define nn "\n"
int v[N];
signed main(){
    // istringstream cin("5 \
2 3 1 5");
    int n;
    cin>>n;
    for(int i=0;i<n-1;i++){
        int x;
        cin>>x;
        v[x]=1;
    }

    for(int i=1;i<=n;i++){
        if(v[i]!=1){
            cout<<i;
            return 0;
        }
    }
}
```
///


### Repetitions

/// collapse-code  
```cpp  
#include<bits/stdc++.h>
using namespace std;
int main(){
    string s;
    cin>>s;
    int ans=1,ma=1;
    for(int i=0;i<s.size()-1;i++){
        if(s[i]==s[i+1]){
            ans++;
        }
        else{
            ans=1;
        }
        ma=max(ma,ans);
    }
    cout<<ma;
}
```
///


### Increasing Array

/// collapse-code  
```cpp  
#include<bits/stdc++.h>
using namespace std;
#define int long long
signed main(){
    int n;
    cin>>n;
    vector<int>v(n);
    for(int i=0;i<n;i++){
        cin>>v[i];
    }

    int ans=0;

    for(int i=1;i<n;i++){
        if(v[i-1]>v[i]){
            ans+=v[i-1]-v[i];
            v[i]=v[i-1];
        }
    }
    cout<<ans;
}
```
///


### Permutations
/// collapse-code  
```cpp  
#include<bits/stdc++.h>
using namespace std;
#define int long long
signed main(){
    int n;
    cin>>n;
    if(n<=1){
        cout<<n;
    }
    else if(n<=3){
        cout<<"NO SOLUTION";
    }
    else{
        for(int i=2;i<=n;i+=2){
            cout<<i<<" ";
        }
        for(int i=1;i<=n;i+=2){
            cout<<i<<" ";
        }
    }
}
```
///

### Number Spiral
/// collapse-code  
```cpp  
#include <bits/stdc++.h>
using namespace std;
#define int long long
#define nn "\n"
signed main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int w;
    cin>>w;
    while(w--){
        int x,y;
        cin>>x>>y;
        int m=max(x,y);
        int ans= m*m-m+1;
        if(m&1){//even   down
            if(x==y){
                cout<<ans<<nn;
            }
            else if(x<y){
                cout<<ans+(y-x)<<nn;
            }
            else{
                cout<<ans-(x-y)<<nn;
            }
        }
        else{
            
            if(x==y){
                cout<<ans<<nn;
            }
            else if(x<y){
                cout<<ans-(y-x)<<nn;
            }
            else{
                cout<<ans+(x-y)<<nn;
            }
        }
    }
    
}
```
///


## Sorting and Searching


### Distinct Numbers


/// collapse-code  
```cpp  
#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    set<int>s;
    for(int i=0;i<n;i++){
        int x;
        cin>>x;
        s.insert(x);
    }
    cout<<s.size();
}
```
///

### Apartments


/// collapse-code  
```cpp  
#include <bits/stdc++.h>
using namespace std;
#define all(x) x.begin(), x.end()
int main() {
    int n, m, k;
    cin >> n >> m >> k;
    vector<int> a(n), b(m);
    for (int &x : a) cin >> x;
    for (int &x : b) cin >> x;
    sort(all(a));
    sort(all(b));
    int ans = 0, it = 0;
    for (int x : a) {
        while (it < m && b[it] < x - k) it++;
        if (it < m && b[it] <= x + k) {
            ans++;
            it++;
        }
    }
    cout << ans;
    return 0;
}
```
///

### Ferris Wheel
/// collapse-code  
```cpp  
#include <bits/stdc++.h>
using namespace std;

#define all(x) v.begin(),v.end()

int main(){
    int  n,m;
    cin>>n>>m;
    vector<int>v(n);
    for(int &i:v)cin>>i;

    int r=n-1;

    sort(all(v));
    reverse(all(v));
    int ans=0;
    for(int i=0;i<n;i++){
        if(v[i]+v[r]<=m){
            ans++;
            r--;
        }
        else{
            ans++;
        }
        if(i>=r){
            break;
        }
    }
    cout<<ans;
}
```
///

## Dynamic Programming

/// collapse-code  
```cpp  
#include <bits/stdc++.h>
using namespace std;

#define all(x) v.begin(),v.end()

int main(){
    int  n,m;
    cin>>n>>m;
    vector<int>v(n);
    for(int &i:v)cin>>i;

    int r=n-1;

    sort(all(v));
    reverse(all(v));
    int ans=0;
    for(int i=0;i<n;i++){
        if(v[i]+v[r]<=m){
            ans++;
            r--;
        }
        else{
            ans++;
        }
        if(i>=r){
            break;
        }
    }
    cout<<ans;
}
```
///


## Graph Algorithms

## Range Queries

## Tree Algorithms


## Mathematics


## String Algorithms


## Geometry


## Advanced Techniques


## Additional Problems


