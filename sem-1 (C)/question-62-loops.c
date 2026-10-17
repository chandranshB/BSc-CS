/*
 * Question 62 (Loops) - Print Fibonacci series and its sum up to N terms
 */

#include <stdio.h>

int main() {
    int n, first = 0, second = 1, next, sum = 0;

    printf("Enter number of terms: ");
    scanf("%d", &n);

    if (n <= 0) {
        printf("Please enter a positive number.\n");
        return 0;
    }

    printf("Fibonacci Series: ");
    if (n == 1) {
        printf("%d", first);
        sum = first;
    } else {
        printf("%d %d ", first, second);
        sum = first + second;
        for (int i = 2; i < n; i++) {
            next = first + second;
            printf("%d ", next);
            sum += next;
            first = second;
            second = next;
        }
    }

    printf("\nSum: %d\n", sum);
    return 0;
}
