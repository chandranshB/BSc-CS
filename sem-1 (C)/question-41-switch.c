/*
 * Question 40 (Switch) - Menu-driven simple and compound interest calculator
 */

#include <stdio.h>
#include <math.h>

int main() {
    int choice;
    float principal, rate, time;

    printf("Interest Calculator\n");
    printf("1. Simple Interest\n");
    printf("2. Compound Interest\n");
    printf("3. Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("Enter Principal, Rate%%, Time: ");
            scanf("%f %f %f", &principal, &rate, &time);
            printf("Simple Interest = %.2f\n", (principal * rate * time) / 100);
            break;
        case 2:
            printf("Enter Principal, Rate%%, Time: ");
            scanf("%f %f %f", &principal, &rate, &time);
            printf("Compound Interest = %.2f\n",
                   principal * pow(1 + rate / 100, time) - principal);
            break;
        case 3:
            printf("Exit.\n");
            break;
        default:
            printf("Invalid choice.\n");
    }

    return 0;
}
