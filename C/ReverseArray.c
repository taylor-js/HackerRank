#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d", &n);
    int arr[n];
    int temp;
    int i = 0;
    int j = n - 1;
    
    for (int c1 = 0; c1 < n; c1++)
    {
        scanf("%d", &arr[c1]);
    }

    while (i < n / 2)
    {
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        i++;
        j--;
    }

    for (int c2 = 0; c2 < n; c2++)
    {
        printf("%d ", arr[c2]);
    }
    return 0;
}
