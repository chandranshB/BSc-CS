/*
 * Question 58 (Loops) - Check whether a number is a perfect number
 *
 * A perfect number equals the sum of its proper divisors (e.g. 6 = 1+2+3).
 */

#include <stdio.h>

int main() {
    int num, sum = 0;

    printf("Enter a number: ");
    scanf("%d", &num);

    for (int i = 1; i < num; i++)
        if (num % i == 0)
            sum += i;

    if (sum == num)
        printf("%d is a perfect number.\n", num);
    else
        printf("%d is not a perfect number.\n", num);

    return 0;
}
