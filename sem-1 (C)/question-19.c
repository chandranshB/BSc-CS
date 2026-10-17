/*
 * Question 19 - Check whether a year is a leap year
 *
 * A year is a leap year if:
 *   - Divisible by 4 AND not divisible by 100, OR
 *   - Divisible by 400
 */

#include <stdio.h>

int main() {
    int year;

    printf("Enter a year: ");
    scanf("%d", &year);

    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
        printf("%d is a leap year.\n", year);
    else
        printf("%d is not a leap year.\n", year);

    return 0;
}
