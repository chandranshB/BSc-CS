/*
 * Question 10 - Find the grade of a student based on marks (using switch)
 *
 * Note: This is a switch-based version of question-02.
 * Dividing percentage by 10 maps scores to switch cases cleanly.
 */

#include <stdio.h>

int main() {
    int a, b, c, d, e, perct;

    printf("Enter marks for 5 subjects: ");
    scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);

    perct = (a + b + c + d + e) / 5;

    switch (perct / 10) {
        case 10:
        case 9:
            printf("Grade: A\n");
            break;
        case 8:
            printf("Grade: B\n");
            break;
        case 7:
            printf("Grade: C\n");
            break;
        default:
            printf("Grade: D\n");
    }

    return 0;
}
