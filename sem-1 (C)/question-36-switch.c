/*
 * Question 35 (Switch) - Check whether a number is even or odd using switch
 */

#include <stdio.h>

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    // num % 2 gives 0 (even), 1 or -1 (odd)
    switch (num % 2) {
        case 0:
            printf("%d is Even.\n", num);
            break;
        case 1:
        case -1:
            printf("%d is Odd.\n", num);
            break;
    }

    return 0;
}
