/*
 * Question 20 - Check whether a number is prime
 *
 * Optimised: loop only up to sqrt(num) instead of num-1
 */

#include <stdio.h>
#include <math.h>

int main() {
    int num, i, isPrime = 1;

    printf("Enter a number: ");
    scanf("%d", &num);

    if (num <= 1) {
        isPrime = 0;
    } else {
        for (i = 2; i <= (int)sqrt((double)num); i++) {  // Optimised: sqrt reduces iterations
            if (num % i == 0) {
                isPrime = 0;
                break;
            }
        }
    }

    if (isPrime)
        printf("%d is a prime number.\n", num);
    else
        printf("%d is not a prime number.\n", num);

    return 0;
}
