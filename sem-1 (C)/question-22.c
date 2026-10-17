/*
 * Question 22 - Calculate profit or loss percentage
 */

#include <stdio.h>

int main() {
    float CP, SP;

    printf("Enter Cost Price: ");
    scanf("%f", &CP);
    printf("Enter Selling Price: ");
    scanf("%f", &SP);

    if (SP > CP) {
        float profit = SP - CP;
        float profitPct = (profit / CP) * 100;
        printf("Profit: %.2f\n", profit);
        printf("Profit Percentage: %.2f%%\n", profitPct);
    } else if (CP > SP) {
        float loss = CP - SP;
        float lossPct = (loss / CP) * 100;
        printf("Loss: %.2f\n", loss);
        printf("Loss Percentage: %.2f%%\n", lossPct);
    } else {
        printf("No Profit, No Loss.\n");
    }

    return 0;
}
