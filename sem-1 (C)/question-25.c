/*
 * Question 25 - Calculate electricity bill based on units consumed
 *
 * Slab rates:
 *   0  - 50  units : Rs. 3.50 per unit
 *   51 - 150 units : Rs. 4.00 per unit
 *  151 - 250 units : Rs. 5.20 per unit
 *  251+     units  : Rs. 6.50 per unit
 */

#include <stdio.h>

int main() {
    float units, bill = 0.0;

    printf("Enter total units consumed: ");
    scanf("%f", &units);

    if (units < 0) {
        printf("Invalid input. Units cannot be negative.\n");
    } else if (units <= 50) {
        bill = units * 3.50;
    } else if (units <= 150) {
        bill = (50 * 3.50) + ((units - 50) * 4.00);
    } else if (units <= 250) {
        bill = (50 * 3.50) + (100 * 4.00) + ((units - 150) * 5.20);
    } else {
        bill = (50 * 3.50) + (100 * 4.00) + (100 * 5.20) + ((units - 250) * 6.50);
    }

    if (units >= 0)
        printf("Electricity Bill: %.2f Rupees\n", bill);

    return 0;
}
