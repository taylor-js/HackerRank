#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, iter, *ptr, sum = 0;

    scanf("%d", &n);

    //int arr[n];
    ptr = (int*) malloc(n * sizeof(int));

    if (ptr == NULL)
    {
        exit(0);
    }

    for(iter = 0; iter < n; ++iter)
    {
        scanf("%d", ptr + iter);
        sum += *(ptr + iter);
    }
    printf("%d", sum);

    free(ptr);

    return 0;
}