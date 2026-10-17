/*
 * Question 57 (Loops) - Check whether a number is an Armstrong number
 *
 * Fixed: missing semicolon after digit = num % 10
 */

#include <stdio.h>

int main() {
    int num, orignum, digit, sum = 0;

    printf("Enter a number: ");
    scanf("%d", &num);

    orignum = num;
    while (num > 0) {
        digit = num % 10;
        sum += digit * digit * digit;
        num /= 10;
    }

    if (sum == orignum)
        printf("%d is an Armstrong number.\n", orignum);
    else
        printf("%d is not an Armstrong number.\n", orignum);

    return 0;
}
