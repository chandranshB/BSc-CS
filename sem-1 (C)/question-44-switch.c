/*
 * Question 43 (Switch) - Menu-driven program: factorial, Fibonacci, prime check
 *
 * Fixed: removed unused 'running' variable and cleaned up structure
 */

#include <stdio.h>
#include <math.h>

long long factorial(int n) {
    long long fact = 1;
    for (int i = 1; i <= n; i++)
        fact *= i;
    return fact;
}

void fibonacci(int n) {
    int t1 = 0, t2 = 1, next;
    if (n >= 1) printf("%d ", t1);
    if (n >= 2) printf("%d ", t2);
    for (int i = 3; i <= n; i++) {
        next = t1 + t2;
        printf("%d ", next);
        t1 = t2;
        t2 = next;
    }
    printf("\n");
}

int isPrime(int n) {
    if (n <= 1) return 0;
    for (int i = 2; i <= (int)sqrt((double)n); i++)
        if (n % i == 0) return 0;
    return 1;
}

int main() {
    int choice, num;

    printf("Math Menu\n");
    printf("1. Factorial\n");
    printf("2. Fibonacci Series\n");
    printf("3. Prime Check\n");
    printf("4. Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("Enter a non-negative integer: ");
            scanf("%d", &num);
            if (num < 0)
                printf("Factorial is not defined for negative numbers.\n");
            else
                printf("Factorial of %d = %lld\n", num, factorial(num));
            break;
        case 2:
            printf("Enter number of terms: ");
            scanf("%d", &num);
            if (num <= 0)
                printf("Number of terms must be positive.\n");
            else {
                printf("Fibonacci: ");
                fibonacci(num);
            }
            break;
        case 3:
            printf("Enter a number: ");
            scanf("%d", &num);
            printf("%d is %sa prime number.\n", num, isPrime(num) ? "" : "not ");
            break;
        case 4:
            printf("Exit.\n");
            break;
        default:
            printf("Invalid choice.\n");
    }

    return 0;
}
