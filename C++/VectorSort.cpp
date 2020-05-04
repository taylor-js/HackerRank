#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<int> vec;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */

    int input = 0;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> input;
        vec.push_back(input);
    }
    sort(vec.begin(), vec.end());
    int len;
    int begin,end;
    int s = sizeof(vec)/sizeof(vec[0]);
    cin >> begin >> end;
    for (int index = 0; index < s; index++){
        
    }
    cout << s;
    erase(begin);
    return 0;
}
