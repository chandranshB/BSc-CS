/*
 * Question 45 (Switch) - Menu-driven matrix addition and subtraction
 */

#include <stdio.h>

#define MAX 10

void readMatrix(int r, int c, int m[MAX][MAX]) {
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++) {
            printf("  [%d][%d]: ", i, j);
            scanf("%d", &m[i][j]);
        }
}

void printMatrix(int r, int c, int m[MAX][MAX]) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++)
            printf("%4d", m[i][j]);
        printf("\n");
    }
}

int main() {
    int choice, r1, c1, r2, c2;
    int m1[MAX][MAX], m2[MAX][MAX], res[MAX][MAX];

    do {
        printf("\nMatrix Operations\n");
        printf("1. Addition\n");
        printf("2. Subtraction\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        if (choice == 1 || choice == 2) {
            printf("Matrix 1 dimensions (rows cols): ");
            scanf("%d %d", &r1, &c1);
            printf("Enter Matrix 1:\n");
            readMatrix(r1, c1, m1);

            printf("Matrix 2 dimensions (rows cols): ");
            scanf("%d %d", &r2, &c2);
            printf("Enter Matrix 2:\n");
            readMatrix(r2, c2, m2);

            if (r1 != r2 || c1 != c2) {
                printf("Matrices must have the same dimensions.\n");
                break;
            }
        }

        switch (choice) {
            case 1:
                for (int i = 0; i < r1; i++)
                    for (int j = 0; j < c1; j++)
                        res[i][j] = m1[i][j] + m2[i][j];
                printf("Result:\n");
                printMatrix(r1, c1, res);
                break;
            case 2:
                for (int i = 0; i < r1; i++)
                    for (int j = 0; j < c1; j++)
                        res[i][j] = m1[i][j] - m2[i][j];
                printf("Result:\n");
                printMatrix(r1, c1, res);
                break;
            case 3:
                printf("Exit.\n");
                break;
            default:
                printf("Invalid choice.\n");
        }
    } while (choice != 3);

    return 0;
}
