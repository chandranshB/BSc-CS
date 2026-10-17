/*
 * Question 13 - Find the youngest among 3 people given their ages
 */

#include <stdio.h>

int main() {
    int a, b, c;

    printf("Enter the ages of 3 people: ");
    scanf("%d %d %d", &a, &b, &c);  // Fixed: removed commas from format string

    if (a <= b && a <= c)
        printf("Person 1 (age %d) is the youngest.\n", a);
    else if (b <= a && b <= c)
        printf("Person 2 (age %d) is the youngest.\n", b);
    else
        printf("Person 3 (age %d) is the youngest.\n", c);

    return 0;
}
