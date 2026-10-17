/*
 * Question 51 (Loops) - Print multiplication table of a given number
 */

#include <stdio.h>

int main() {
    int a;

    printf("Enter a number: ");
    scanf("%d", &a);

    for (int i = 1; i <= 10; i++)
        printf("%d x %d = %d\n", a, i, a * i);

    return 0;
}
