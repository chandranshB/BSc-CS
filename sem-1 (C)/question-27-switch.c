/*
 * Question 26 (Switch) - Find the maximum of two numbers using switch
 */

#include <stdio.h>

int main() {
    int num1, num2;

    printf("Enter two numbers: ");
    scanf("%d %d", &num1, &num2);

    // (num1 > num2) evaluates to 1 (true) or 0 (false)
    switch (num1 > num2) {
        case 1:
            printf("Maximum: %d\n", num1);
            break;
        case 0:
            if (num1 == num2)
                printf("Both numbers are equal: %d\n", num1);
            else
                printf("Maximum: %d\n", num2);
            break;
    }

    return 0;
}
