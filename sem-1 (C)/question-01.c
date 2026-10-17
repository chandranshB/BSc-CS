/*
 * Question 01 - Check if a number is positive, negative, or zero
 */

#include <stdio.h>

int main() {
    int a;

    printf("Enter a number: ");
    scanf("%d", &a);

    if (a > 0)
        printf("The number is positive.\n");
    else if (a == 0)   // Fixed: was (a = 0) which is assignment, not comparison
        printf("The number is zero.\n");
    else
        printf("The number is negative.\n");

    return 0;
}
