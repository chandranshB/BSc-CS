/*
 * Question 55 (Loops) - Find the product of digits of a number
 */

#include <stdio.h>

int main() {
    int num, product = 1;

    printf("Enter a number: ");
    scanf("%d", &num);

    while (num != 0) {
        product *= num % 10;
        num /= 10;
    }

    printf("Product of digits: %d\n", product);
    return 0;
}
