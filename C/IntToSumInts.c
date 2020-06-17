#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int sum_all_digits(int num)
{
    //int digit = (int)(num/pow(10, pos - 1)) % 10;
    int digit_sum = 0;
    int iter = 1;
    while (iter <= 5){
        digit_sum += (int)(num/pow(10, iter - 1)) % 10;
        iter++;
    }
    return digit_sum;
}

int main() 
{
    int n;
    //char char_array[5];
    scanf("%d", &n);
    printf("%d", (int)sum_all_digits(n));
    return 0;
}