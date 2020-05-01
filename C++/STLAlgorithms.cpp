#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>

//http://www.cplusplus.com/reference/algorithm/

using namespace std;

int main(){
    int arr[] = {10, 20, 5, 23, 42, 15};
    int n = sizeof(arr)/sizeof(arr[0]);
    vector<int> vec(arr, arr + n);

    sort(vec.begin(), vec.end());
    bool b = binary_search(vec.begin(), vec.end(), 55);

    if (b == true){
        cout << "Found!" << endl;
    }
    else {
        cout << "Not Found." << endl;
    }
    
    for (int i=0; i < n; i++) {
        cout << vec[i] << " ";
    }
    return 0;
}