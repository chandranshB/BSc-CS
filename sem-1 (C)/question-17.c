/*
 * Question 17 - Check whether a number is an Armstrong number
 *
 * An Armstrong number equals the sum of the cubes of its digits.
 * Example: 153 = 1^3 + 5^3 + 3^3 = 153
 */

#include <stdio.h>

int main() {
    int num, orignum, digit, sum = 0;

    printf("Enter a number: ");
    scanf("%d", &num);

    orignum = num;
    while (num > 0) {
        digit = num % 10;
        sum = sum + digit * digit * digit;  // Fixed: missing semicolon after digit = num % 10
        num = num / 10;
    }

    if (sum == orignum)
        printf("%d is an Armstrong number.\n", orignum);
    else
        printf("%d is not an Armstrong number.\n", orignum);

    return 0;
}
