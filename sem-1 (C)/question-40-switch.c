/*
 * Question 39 (Switch) - Menu-driven temperature conversion (Celsius <-> Fahrenheit)
 */

#include <stdio.h>

int main() {
    int choice;
    float temp, converted;

    printf("Temperature Conversion\n");
    printf("1. Celsius to Fahrenheit\n");
    printf("2. Fahrenheit to Celsius\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("Enter temperature in Celsius: ");
            scanf("%f", &temp);
            converted = (temp * 9.0f / 5.0f) + 32.0f;
            printf("%.2f C = %.2f F\n", temp, converted);
            break;
        case 2:
            printf("Enter temperature in Fahrenheit: ");
            scanf("%f", &temp);
            converted = (temp - 32.0f) * 5.0f / 9.0f;
            printf("%.2f F = %.2f C\n", temp, converted);
            break;
        default:
            printf("Invalid choice. Enter 1 or 2.\n");
    }

    return 0;
}
