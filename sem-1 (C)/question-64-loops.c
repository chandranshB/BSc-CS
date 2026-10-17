/*
 * Question 64 (Loops) - Print Geometric Progression (G.P.) series
 */

#include <stdio.h>

int main() {
    int a, r, n, current;

    printf("Enter first term: ");
    scanf("%d", &a);
    printf("Enter common ratio: ");
    scanf("%d", &r);
    printf("Enter number of terms: ");
    scanf("%d", &n);

    printf("G.P. Series: ");
    current = a;
    for (int i = 0; i < n; i++) {
        printf("%d ", current);
        current *= r;
    }
    printf("\n");

    return 0;
}
