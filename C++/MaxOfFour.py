include <iostream>
include <cstdio>
include <vector>
include <algorithm>

using namespace std;

int max_of_four(int a, int b, int c, int d){
    std::vector<int> v = { a, b, c, d };

    std::sort(v.begin(), v.end());

    //for (const auto &i: v)
    //    std::cout << i << ' ';
    
    return v[sizeof(v)-1];
}
int main (){
        
    /*
    Add `int max_of_four(int a, int b, int c, int d)` here.
    */

    int main() {
        int a, b, c, d;
        scanf("%d %d %d %d", &a, &b, &c, &d);
        int ans = max_of_four(a, b, c, d);
        printf("%d", ans);
        
        return 0;
    }
    return 0;
}