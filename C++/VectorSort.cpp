#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> vec;

int main()
{

    int input = 0;
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> input;
        vec.push_back(input);
    }
    sort(vec.begin(), vec.end());
    for (int i = 0; i < n; i++)
    {
        cout << vec[i] << " ";
    }

    return 0;
}