/*
 * Question 33 (Switch) - Menu-driven program to calculate area of circle, rectangle, or triangle
 */

#include <stdio.h>
#include <math.h>

int main() {
    int choice;
    float area;

    printf("Calculate Area\n");
    printf("1. Circle\n");
    printf("2. Rectangle\n");
    printf("3. Triangle\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1: {
            float radius;
            printf("Enter radius: ");
            scanf("%f", &radius);
            area = M_PI * radius * radius;
            printf("Area of Circle: %.2f\n", area);
            break;
        }
        case 2: {
            float length, width;
            printf("Enter length and width: ");
            scanf("%f %f", &length, &width);
            area = length * width;
            printf("Area of Rectangle: %.2f\n", area);
            break;
        }
        case 3: {
            float base, height;
            printf("Enter base and height: ");
            scanf("%f %f", &base, &height);
            area = 0.5f * base * height;
            printf("Area of Triangle: %.2f\n", area);
            break;
        }
        default:
            printf("Invalid choice.\n");
    }

    return 0;
}
