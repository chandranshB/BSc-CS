/*
 * Question 38 (Switch) - Menu-driven unit conversion (distance)
 */

#include <stdio.h>

int main() {
    int choice;
    double value, result;

    printf("Unit Conversion\n");
    printf("1. Kilometers to Meters\n");
    printf("2. Meters to Kilometers\n");
    printf("3. Meters to Centimeters\n");
    printf("4. Centimeters to Meters\n");
    printf("5. Kilometers to Centimeters\n");
    printf("6. Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("Enter km: "); scanf("%lf", &value);
            result = value * 1000.0;
            printf("%.2lf km = %.2lf m\n", value, result);
            break;
        case 2:
            printf("Enter m: "); scanf("%lf", &value);
            result = value / 1000.0;
            printf("%.2lf m = %.2lf km\n", value, result);
            break;
        case 3:
            printf("Enter m: "); scanf("%lf", &value);
            result = value * 100.0;
            printf("%.2lf m = %.2lf cm\n", value, result);
            break;
        case 4:
            printf("Enter cm: "); scanf("%lf", &value);
            result = value / 100.0;
            printf("%.2lf cm = %.2lf m\n", value, result);
            break;
        case 5:
            printf("Enter km: "); scanf("%lf", &value);
            result = value * 100000.0;
            printf("%.2lf km = %.2lf cm\n", value, result);
            break;
        case 6:
            printf("Exit.\n");
            break;
        default:
            printf("Invalid choice.\n");
    }

    return 0;
}
