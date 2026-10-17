/*
 * Question 59 (Loops) - Check whether a number is prime
 *
 * Optimised: loop up to sqrt(num) instead of num/2
 */

#include <stdio.h>
#include <math.h>

int main() {
    int num, isPrime = 1;

    printf("Enter a positive integer: ");
    scanf("%d", &num);

    if (num <= 1) {
        isPrime = 0;
    } else {
        for (int i = 2; i <= (int)sqrt((double)num); i++) {
            if (num % i == 0) {
                isPrime = 0;
                break;
            }
        }
    }

    printf("%d is %sa prime number.\n", num, isPrime ? "" : "not ");
    return 0;
}
