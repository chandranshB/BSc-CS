/*
 * Question 42 (Switch) - Menu-driven pattern printer (square, triangle, pyramid)
 *
 * Fixed: mismatched braces that caused the switch to be unreachable
 */

#include <stdio.h>

void printSquare(int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++)
            printf("* ");
        printf("\n");
    }
}

void printTriangle(int size) {
    for (int i = 1; i <= size; i++) {
        for (int j = 1; j <= i; j++)
            printf("* ");
        printf("\n");
    }
}

void printPyramid(int size) {
    for (int i = 1; i <= size; i++) {
        for (int sp = 1; sp <= size - i; sp++)
            printf("  ");
        for (int j = 1; j <= 2 * i - 1; j++)
            printf("* ");
        printf("\n");
    }
}

int main() {
    int choice, size;

    printf("Pattern Printer\n");
    printf("1. Square\n");
    printf("2. Right-Angled Triangle\n");
    printf("3. Pyramid\n");
    printf("4. Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    if (choice >= 1 && choice <= 3) {
        printf("Enter size: ");
        scanf("%d", &size);
    }

    switch (choice) {
        case 1: printSquare(size);   break;
        case 2: printTriangle(size); break;
        case 3: printPyramid(size);  break;
        case 4: printf("Exit.\n");   break;
        default: printf("Invalid choice.\n");
    }

    return 0;
}
