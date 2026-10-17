/*
 * Question 46 (Switch) - ATM simulation (exit-controlled menu)
 */

#include <stdio.h>

int main() {
    long int balance = 10000;
    int choice;
    long int amount;
    char cont = 'y';

    do {
        printf("\n*** ATM Service ***\n");
        printf("1. Check Balance\n");
        printf("2. Withdraw Cash\n");
        printf("3. Deposit Cash\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Current balance: %ld\n", balance);
                break;
            case 2:
                printf("Enter amount to withdraw: ");
                scanf("%ld", &amount);
                if (amount % 100 != 0)
                    printf("Amount must be a multiple of 100.\n");
                else if (amount > balance)
                    printf("Insufficient balance.\n");
                else {
                    balance -= amount;
                    printf("Withdrawn. Remaining balance: %ld\n", balance);
                }
                break;
            case 3:
                printf("Enter amount to deposit: ");
                scanf("%ld", &amount);
                balance += amount;
                printf("Deposited. New balance: %ld\n", balance);
                break;
            case 4:
                printf("Thank you for using our ATM.\n");
                cont = 'n';
                break;
            default:
                printf("Invalid choice.\n");
        }

        if (cont == 'y') {
            printf("Another transaction? (y/n): ");
            while (getchar() != '\n');
            scanf("%c", &cont);
        }

    } while (cont == 'y' || cont == 'Y');

    return 0;
}
