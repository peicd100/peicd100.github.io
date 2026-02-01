# 排列生成permutation窮舉

[資料來源](https://yuihuang.com/cpp-algorithm-next-permutation/)

/// html | div.i

有三個函數可使用

支援陣列資料結構 ( 記憶體位置連續儲存 )
如：

- `int v[N]`
- `vector<int> v`


///

## is_permutation( )


> is_permutation( 陣列A開頭指針 , 陣列A結尾指針 , 陣列B );




> 判斷陣列 B 是否為陣列 A 轉換順序後的結果
> 也可把它看成集合比對器(集合不看順序)  
> 如果A集合包含於B集合，就回傳true，否則回傳false  
> 也就是在判斷a是否為b的子集合  
> 如下：  

我們可假想他的函數是這樣寫的
```cpp
bool is_permutation( 陣列A開頭指針 , 陣列A結尾指針 , 陣列B ){
    
    if (A集合包含於B集合) {
      return true;
    }
    
    reurn false;
    
}
```





### 舉例：
=== "完全相同，回傳true"

    ```cpp  
    #include <bits/stdc++.h>
    using namespace std;

    int main(){
        char c[]("123");
        char v[]("123");
        cout<<is_permutation(c,c+3,v);
        
    }
    ```
    /// html | div.result
    ```
    1
    ```
    ///


=== "重新排列，回傳true"

    ```cpp  
    #include <bits/stdc++.h>
    using namespace std;

    int main(){
        char c[]("123");
        char v[]("312");
        cout<<is_permutation(c,c+3,v);
        
    }
    ```
    /// html | div.result
    ```
    1
    ```
    ///


=== "為子集合，回傳true"

    ```cpp  
    #include <bits/stdc++.h>
    using namespace std;

    int main(){
        char c[]("123");
        char v[]("1234");
        cout<<is_permutation(c,c+3,v);

    }
    ```
    /// html | div.result
    ```
    1
    ```
    ///


=== "並非子集合，回傳false"

    ```cpp  
    #include <bits/stdc++.h>
    using namespace std;

    int main(){
        char c[]("123");
        char v[]("133");
        cout<<is_permutation(c,c+3,v);

    }
    ```
    /// html | div.result
    ```
    0
    ```
    ///



## prev_permutation( )

> prev_permutation( 陣列開頭指針 , 陣列結尾指針 );


> 找出前一個字典序排列，找到回傳true，沒找到回傳false

```cpp  
#include <bits/stdc++.h>
using namespace std;

int main(){
    char c[]("321");
    while(prev_permutation(c,c+3)){
        cout<<c<<"\n";
    }
}
```
/// html | div.result
```
312
231
213
132
123
```
///



## next_permutation( )



> next_permutation( 陣列開頭指針 , 陣列結尾指針 );


> 找出前一個字典序排列，找到回傳true，沒找到回傳false

```cpp  
#include <bits/stdc++.h>
using namespace std;

int main(){
    char c[]("123");
    while(next_permutation(c,c+3)){
        cout<<c<<"\n";
    }
}
```
/// html | div.result
```
132
213
231
312
321
```
///

## 製作窮舉

```cpp  
#include <bits/stdc++.h>
using namespace std;
int main(){
    char c[]("12345");
    while(next_permutation(c,c+strlen(c))){
        cout<<c<<";";
    }
}
```

/// html | div.result
```
12354;12435;12453;12534;12543;13245;13254;13425;13452;13524;13542;14235;14253;14325;14352;14523;14532;15234;15243;15324;15342;15423;15432;21345;21354;21435;21453;21534;21543;23145;23154;23415;23451;23514;23541;24135;24153;24315;24351;24513;24531;25134;25143;25314;25341;25413;25431;31245;31254;31425;31452;31524;31542;32145;32154;32415;32451;32514;32541;34125;34152;34215;34251;34512;34521;35124;35142;35214;35241;35412;35421;41235;41253;41325;41352;41523;41532;42135;42153;42315;42351;42513;42531;43125;43152;43215;43251;43512;43521;45123;45132;45213;45231;45312;45321;51234;51243;51324;51342;51423;51432;52134;52143;52314;52341;52413;52431;53124;53142;53214;53241;53412;53421;54123;54132;54213;54231;54312;54321;
```
///