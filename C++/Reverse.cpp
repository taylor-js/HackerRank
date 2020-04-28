#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "Enter number of elements you want to insert: ";
    cin >> n;
    int arr[n];
    int temp;

    int i = 0;
    int j = n - 1;

    for (i = 0; i < n; i++)
    {
        cout << "Enter element " << i + 1 << ":";
        cin >> arr[i];
    }

    while (i < n / 2)
    {
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;

        i++;
        j--;
    }

    cout << "\nReverse array" << endl;

    for (i = 0; i < n; i++)
        cout << arr[i] << " ";

    return 0;
}
