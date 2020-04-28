#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

void print(int arr[], int n){
    for (int i = 0; i < n; ++i){
        cout << arr[i] << " ";
    }
}
void reverse_nums(int nums) {
    int pivot;
    if(*str == '\0')
        return;
    else {
        reverse(str + 1);
        cout << *str;
    }
}
int main() {
    int sizeofarray;
    cin >> sizeofarray;
    int a[sizeofarray];
    
    for (int i = 0; i < sizeofarray; ++i)
    {
        cin >> a[i];
    }
    reverse(a,0,sizeofarray);
    print(a);
    return 0;
}