#include<iostream>
using namespace std;

int main()
{
    int n;
	cin >> n;
	int arr[n];
    int temp;

    int i = 0;
    int j = n - 1;

	for(int c1 = 0; c1 < n; c1++)
	{
		cin >> arr[c1];
	}
    while (i < n / 2){
        temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;

        i++;
        j--;
    }

	for(int c2 = 0; c2 < n; c2++)
	{
		cout << arr[c2] << " ";
	}

	return 0;
}

