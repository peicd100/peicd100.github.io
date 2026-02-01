# map

map 是儲存 pair
map 依照 pair 的 first 進行排序
所以 pair 的 first 要是可以排序的東西，像是 int 、 pair 、 tuple 、自己寫的 operator< 結構


## 重點

1.只要執行 `mp[x]` 就會新增一個鑑為 x 的pair   
2.要判斷是否有鑑值存在於 map 中要用 mp.find(x)   
3.假設用 mp.find({"a",1}) 找 mp 裡面有沒有 「鑑：a，值：1」 ，只要鑑有a，就會回傳true，如下程式碼
```cpp title="程式碼"
#include <bits/stdc++.h>
using namespace std;
map<string,int> mp;
int main() {
    mp["a"]=3;
    if(mp.find({"a",1})!=mp.end()){
        cout<<"有"<<"\n";
    }
    else{
        cout<<"沒有"<<"\n";
    }
}
```
```cpp title="輸出"
有
```
4.要正確找 mp 裡面有沒有 「鑑：a，值：1」 就要進一步判斷second是否符合，如下
```cpp title="程式碼"
#include <bits/stdc++.h>
using namespace std;
map<string,int> mp;
int main() {
    mp["a"]=3;
    auto it=mp.find({"a",1});
    if(it!=mp.end() && it->second==1){
        cout<<"有"<<"\n";
    }
    else{
        cout<<"沒有"<<"\n";
    }
    
    if(it!=mp.end() && it->second==3){
        cout<<"有"<<"\n";
    }
    else{
        cout<<"沒有"<<"\n";
    }
}
```
```cpp title="輸出"
沒有
有
```


## 主要特點
1. **鍵值對存儲**：`map` 以鍵值對的形式存儲數據，每個鍵對應一個值。
2. **鍵的唯一性**：在一個 `map` 中，每個鍵都是唯一的。如果插入一個已有的鍵，其對應的值將被更新。
3. **自動排序**：`map` 中的元素會根據鍵自動排序，默認是按升序排列。
4. **高效查找**：`map` 提供高效的查找、插入和刪除操作，時間複雜度為 O(log n)。

## 基本用法

以下是一些基本操作的示例：

1. **宣告與初始化**
    ```cpp
    {% raw %}
    #include <iostream>
    #include <map>
    using namespace std;

    int main() {
        map<int, string> myMap; // 宣告一個空的 map，鍵為 int，值為 string
        myMap[1] = "Apple";
        myMap[2] = "Banana";
        myMap[3] = "Cherry";

        // 使用 initializer list 初始化
        map<int, string> anotherMap = {{1, "Apple"}, {2, "Banana"}, {3, "Cherry"}};

        return 0;
    }
    {% endraw %}
    ```

2. **插入元素**
    ```cpp
    myMap.insert({4, "Date"});
    myMap[5] = "Elderberry"; // 也可以使用 [] 操作符
    ```

3. **訪問元素**
    ```cpp
    cout << myMap[1] << endl; // 輸出 "Apple"
    cout << myMap.at(2) << endl; // 輸出 "Banana"
    ```

4. **遍歷元素**
    ```cpp
    for (const auto& pair : myMap) {
        cout << pair.first << ": " << pair.second << endl;
    }
    ```

5. **查找元素(判斷索引是否存在於map中)**
   ```cpp
   auto it = myMap.find(2); // 查找鍵為 2 的元素
   if (it != myMap.end()) {
       cout << "Found: " << it->second << endl; // 輸出 "Found: Banana"
   } else {
       cout << "Not found" << endl;
   }
   ```

6. **刪除元素**
   ```cpp
   myMap.erase(3); // 刪除鍵為 3 的元素
   ```
7. **尋找元素**
   ```cpp
    #include<bits/stdc++.h>
    using namespace std;
    int main(){
        map<char,int>mp={{'c',1},{'a',2}};
        if(mp.find('c')!=mp.end()){
            cout<<"find";
        }
    }
   ```
   
8. **更改內容**

    ```cpp
    #include <map>
    using namespace std;

    int main() {
        map<int, string> myMap;
        myMap[1] = "Apple";
        myMap[2] = "Banana";
        myMap[3] = "Cherry";

        // 修改 map 中的值
        for (auto& pair : myMap) {
            pair.second = "Modified " + pair.second;
        }

        // 輸出修改後的 map
        for (const auto& pair : myMap) {
            cout << pair.first << ": " << pair.second << endl;
        }

        return 0;
    }

    ```

    注意！！
    key不能更改


## map的key放置自訂struct



> 想要在key放置兩個數字，可以自己創struct，但是需要寫排序函式
> 不想要寫函式就要使用pair來當key，只是要記得first/second

/// details | 題目
<img src="https://hackmd.io/_uploads/r1O8JmSxa.png" alt="image" />
///




/// collapse-code  
```cpp  
#include<bits/stdc++.h>
using namespace std;

struct Point {
    int x, y;
};

bool operator<(const Point &a, const Point &b) {
    if (a.x == b.x) {
        return a.y < b.y;
    }
    return a.x < b.x;
}

int main(){
    int w;
    cin>>w;
    while(w--){
        int n;
        cin>>n;
        map<Point,int> mp;
        for(int i=0;i<n;i++){
            Point p;
            cin>>p.x>>p.y;
            if(p.x<p.y){
                mp[{p.x,p.y}]++;
            }
            else{
                mp[{p.y,p.x}]++;
            }
        }
        int ans=0;
        for(auto i:mp){
            if(i.second==2){
                ans++;
            }
        }
        cout<<ans<<"\n";
    }
}
```
///