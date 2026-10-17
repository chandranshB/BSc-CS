/*
 * Question 37 (Switch) - Print multiplication table of a given number
 */

#include <stdio.h>

int main() {
    int num, choice;

    printf("Enter a number: ");
    scanf("%d", &num);
    printf("Enter 1 to print table, 0 to exit: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("Multiplication table of %d:\n", num);
            for (int i = 1; i <= 10; i++)
                printf("%d x %d = %d\n", num, i, num * i);
            break;
        case 0:
            printf("Exiting.\n");
            break;
        default:
            printf("Invalid choice. Enter 1 or 0.\n");
    }

    return 0;
}
