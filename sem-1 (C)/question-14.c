/*
 * Question 14 - Find the oldest among 3 people given their ages
 */

#include <stdio.h>

int main() {
    int a, b, c;

    printf("Enter the ages of 3 people: ");
    scanf("%d %d %d", &a, &b, &c);  // Fixed: removed commas from format string

    if (a >= b && a >= c)
        printf("Person 1 (age %d) is the oldest.\n", a);
    else if (b >= a && b >= c)
        printf("Person 2 (age %d) is the oldest.\n", b);
    else
        printf("Person 3 (age %d) is the oldest.\n", c);

    return 0;
}
