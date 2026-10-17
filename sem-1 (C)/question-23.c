/*
 * Question 23 - Check whether a number is a palindrome
 *
 * A palindrome reads the same forwards and backwards (e.g. 121, 1331).
 */

#include <stdio.h>

int main() {
    int num, orignum, digit, rev = 0;

    printf("Enter a number: ");
    scanf("%d", &num);

    orignum = num;
    while (num > 0) {
        digit = num % 10;
        rev = rev * 10 + digit;
        num = num / 10;
    }

    if (orignum == rev)
        printf("%d is a palindrome.\n", orignum);  // Fixed: was printing 'num' (which is 0 after loop)
    else
        printf("%d is not a palindrome.\n", orignum);

    return 0;
}
