/*
 * Question 08 - Find the absolute value of a number
 */

#include <stdio.h>

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    // Fixed: was using undefined variable 'a', should use 'num'
    if (num < 0)
        printf("The absolute value of %d is %d.\n", num, -num);
    else
        printf("The absolute value of %d is %d.\n", num, num);

    return 0;
}
