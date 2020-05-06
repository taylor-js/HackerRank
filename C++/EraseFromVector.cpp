#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, start, end;
    cin >> n;
    vector<int> vec;
    for (int i = 0; i < n; ++i)
    {
    	cin>>start;
    	vec.push_back(start);
    }
    cin >> start;
    vec.erase(vec.begin() + start - 1);
    cin >> start >> end;
    vec.erase(vec.begin() + start - 1, vec.begin() + end - 1);
    cout << vec.size() << endl;
    for (int i = 0; i < vec.size(); ++i)
        cout << vec[i] << ' ';
    
    return 0;
}
// 6
// 1 4 6 2 8 9
// 2
// 2 4