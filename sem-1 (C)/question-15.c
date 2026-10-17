/*
 * Question 15 - Check whether a triangle is valid based on its angles
 */

#include <stdio.h>

int main() {
    int A, B, C;

    printf("Enter the three angles of a triangle: ");
    scanf("%d %d %d", &A, &B, &C);  // Fixed: removed commas from format string

    if (A + B + C == 180)  // Fixed: was (= 180) assignment instead of (== 180) comparison
        printf("The triangle is valid.\n");
    else
        printf("The triangle is invalid.\n");

    return 0;
}
