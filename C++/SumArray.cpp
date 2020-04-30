#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <iostream>  
#include <numeric>

using namespace std;

int calculateTotalScore(int a[], int n)  
{ 
    int initial_sum  = 0;  
    return accumulate(a, a + n, initial_sum); 
}

int main(){
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << calculateTotalScore(arr, n);
    return 0;
}