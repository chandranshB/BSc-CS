/*
 * Question 34 (Switch) - Menu-driven program to calculate volume of cube, cuboid, or sphere
 */

#include <stdio.h>
#include <math.h>

int main() {
    int choice;
    double volume;

    printf("Calculate Volume\n");
    printf("1. Cube\n");
    printf("2. Cuboid\n");
    printf("3. Sphere\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1: {
            double side;
            printf("Enter side length: ");
            scanf("%lf", &side);
            volume = side * side * side;
            printf("Volume of Cube: %.2lf\n", volume);
            break;
        }
        case 2: {
            double l, b, h;
            printf("Enter length, breadth, height: ");
            scanf("%lf %lf %lf", &l, &b, &h);
            volume = l * b * h;
            printf("Volume of Cuboid: %.2lf\n", volume);
            break;
        }
        case 3: {
            double radius;
            printf("Enter radius: ");
            scanf("%lf", &radius);
            volume = (4.0 / 3.0) * M_PI * pow(radius, 3);
            printf("Volume of Sphere: %.2lf\n", volume);
            break;
        }
        default:
            printf("Invalid choice.\n");
    }

    return 0;
}
