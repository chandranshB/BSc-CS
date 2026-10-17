/*
 * Question 53 (Loops) - Count the number of digits in a number
 */

#include <stdio.h>

int main() {
    int num, count = 0;

    printf("Enter a number: ");
    scanf("%d", &num);

    if (num == 0) {
        count = 1;
    } else {
        int temp = num;
        while (temp != 0) {
            temp /= 10;
            count++;
        }
    }

    printf("Number of digits in %d: %d\n", num, count);
    return 0;
}
