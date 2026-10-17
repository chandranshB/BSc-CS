/*
 * Question 41 (Switch) - Menu-driven triangle type checker
 *
 * Fixed: missing scanf for side inputs and missing semicolon after printf
 */

#include <stdio.h>

int main() {
    int choice;

    printf("Triangle Type Checker\n");
    printf("1. Check Triangle Type\n");
    printf("2. Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1: {
            int a, b, c;
            printf("Enter the lengths of three sides: ");
            scanf("%d %d %d", &a, &b, &c);  // Fixed: was missing scanf entirely

            if (a + b > c && a + c > b && b + c > a) {
                if (a == b && b == c)
                    printf("Equilateral triangle.\n");
                else if (a == b || b == c || a == c)
                    printf("Isosceles triangle.\n");
                else
                    printf("Scalene triangle.\n");
            } else {
                printf("Invalid sides (triangle inequality not satisfied).\n");
            }
            break;
        }
        case 2:
            printf("Exit.\n");
            break;
        default:
            printf("Invalid choice.\n");
    }

    return 0;
}
