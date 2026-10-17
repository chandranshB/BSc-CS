/*
 * Question 56 (Loops) - Check whether a number is a palindrome
 *
 * Fixed: was printing 'num' after the loop (which becomes 0); use 'orignum' instead
 */

#include <stdio.h>

int main() {
    int num, orignum, rev = 0;

    printf("Enter a number: ");
    scanf("%d", &num);

    orignum = num;
    while (num > 0) {
        rev = rev * 10 + num % 10;
        num /= 10;
    }

    if (orignum == rev)
        printf("%d is a palindrome.\n", orignum);
    else
        printf("%d is not a palindrome.\n", orignum);

    return 0;
}
