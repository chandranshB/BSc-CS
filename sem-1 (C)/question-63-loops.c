/*
 * Question 63 (Loops) - Print Arithmetic Progression (A.P.) series
 */

#include <stdio.h>

int main() {
    int firstTerm, diff, n, current;

    printf("Enter first term: ");
    scanf("%d", &firstTerm);
    printf("Enter common difference: ");
    scanf("%d", &diff);
    printf("Enter number of terms: ");
    scanf("%d", &n);

    printf("A.P. Series: ");
    current = firstTerm;
    for (int i = 0; i < n; i++) {
        printf("%d ", current);
        current += diff;
    }
    printf("\n");

    return 0;
}
