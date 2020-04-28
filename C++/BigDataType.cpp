#include <stdio.h>
#include <iostream>

int main() {
    int my_int;
    long my_long;
    char my_char;
    float my_float;
    double my_double;
    scanf("%d %ld %c %f %lf", &my_int, &my_long, &my_char, &my_float, &my_double);

    printf("%d", my_int);
    printf("\n");
    printf("%ld", my_long);
    printf("\n");
    printf("%c", my_char);
    printf("\n");
    printf("%.3f", my_float);
    printf("\n");
    printf("%.9lf", my_double);

    return 0;
}