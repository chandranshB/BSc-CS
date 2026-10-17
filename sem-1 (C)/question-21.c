/*
 * Question 21 - Find the roots of a quadratic equation (ax^2 + bx + c = 0)
 *
 * Cases:
 *   discriminant > 0  -> two distinct real roots
 *   discriminant == 0 -> one repeated real root
 *   discriminant < 0  -> two complex (imaginary) roots
 */

#include <stdio.h>
#include <math.h>

int main() {
    float a, b, c;
    float discriminant, root1, root2, realPart, imagPart;

    printf("Enter coefficients a, b, c for ax^2 + bx + c = 0: ");
    scanf("%f %f %f", &a, &b, &c);

    discriminant = b * b - 4 * a * c;

    if (discriminant > 0) {
        root1 = (-b + sqrt(discriminant)) / (2 * a);
        root2 = (-b - sqrt(discriminant)) / (2 * a);
        printf("Two distinct real roots: %.2f and %.2f\n", root1, root2);
    } else if (discriminant == 0) {
        root1 = -b / (2 * a);
        printf("One repeated real root: %.2f\n", root1);  // Fixed: printf was outside the if block
    } else {
        realPart = -b / (2 * a);
        imagPart = sqrt(-discriminant) / (2 * a);
        printf("Complex roots: %.2f + %.2fi  and  %.2f - %.2fi\n", realPart, imagPart, realPart, imagPart);
    }

    return 0;
}
