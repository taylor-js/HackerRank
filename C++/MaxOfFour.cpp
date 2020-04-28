#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_four(int a, int b, int c, int d){
    int v[4] = { a, b, c, d };
    int max = v[0];
    for (int i = 1; i < 4; ++i){
        if (v[i] > max){
            max = v[i];
        }
    }
    return max;
}
int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}