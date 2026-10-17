/*
 * Question 16 - Classify a triangle as equilateral, isosceles, or scalene
 */

#include <stdio.h>

int main() {
    int a, b, c;

    printf("Enter the three sides of a triangle: ");
    scanf("%d %d %d", &a, &b, &c);  // Fixed: removed commas from format string

    if (a == b && b == c)
        printf("The triangle is Equilateral.\n");
    else if (a == b || b == c || a == c)
        printf("The triangle is Isosceles.\n");
    else
        printf("The triangle is Scalene.\n");

    return 0;
}
