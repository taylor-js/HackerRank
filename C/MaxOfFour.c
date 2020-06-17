#include <stdio.h>

int maximum_of_len_four_array(int a, int b, int c, int d)
{
    int len_four_array[4] = {a, b, c, d};
    int iter;
    int max_pivot = len_four_array[0];
    for(iter = 0; iter < 4; iter++)
        if(max_pivot < len_four_array[iter])
            max_pivot = len_four_array[iter];
    return max_pivot;
}

int main()
{
    int maximum_value;
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    maximum_value = maximum_of_len_four_array(a, b, c, d);
    printf("%d", maximum_value);
    return 0;
}