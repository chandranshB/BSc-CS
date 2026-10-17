/*
 * Question 27 (Switch) - Find the maximum of three numbers using nested switch
 */

#include <stdio.h>

int main() {
    int num1, num2, num3;

    printf("Enter three integers: ");
    scanf("%d %d %d", &num1, &num2, &num3);

    // Outer switch: is num1 > num2?
    switch (num1 > num2) {
        case 1:  // num1 > num2, now compare num1 vs num3
            switch (num1 > num3) {
                case 1:
                    printf("Maximum: %d\n", num1);
                    break;
                case 0:
                    printf("Maximum: %d\n", num3);
                    break;
            }
            break;
        case 0:  // num2 >= num1, now compare num2 vs num3
            switch (num2 > num3) {
                case 1:
                    printf("Maximum: %d\n", num2);
                    break;
                case 0:
                    printf("Maximum: %d\n", num3);
                    break;
            }
            break;
    }

    return 0;
}
