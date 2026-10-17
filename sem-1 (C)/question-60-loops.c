/*
 * Question 60 (Loops) - Print all prime numbers in a given range
 *
 * Fixed: missing closing brace for the outer for loop and misplaced getch()
 */

#include <stdio.h>
#include <math.h>

int main() {
    int start, end;

    printf("Enter start of range: ");
    scanf("%d", &start);
    printf("Enter end of range: ");
    scanf("%d", &end);

    printf("Prime numbers between %d and %d: ", start, end);

    for (int num = start; num <= end; num++) {
        if (num <= 1) continue;

        int isPrime = 1;
        for (int i = 2; i <= (int)sqrt((double)num); i++) {
            if (num % i == 0) {
                isPrime = 0;
                break;
            }
        }
        if (isPrime)
            printf("%d ", num);
    }

    printf("\n");
    return 0;
}
