/*
 * Question 02 - Find the grade of a student based on marks in 5 subjects
 */

#include <stdio.h>

int main() {
    int a, b, c, d, e, perct;

    printf("Enter marks for 5 subjects: ");
    scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);  // Fixed: removed commas from format string

    perct = (a + b + c + d + e) / 5;

    if (perct >= 90)
        printf("Grade: A\n");
    else if (perct >= 80)
        printf("Grade: B\n");
    else if (perct >= 70)
        printf("Grade: C\n");
    else
        printf("Grade: D\n");

    return 0;
}
