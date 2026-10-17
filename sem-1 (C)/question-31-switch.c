/*
 * Question 30 (Switch) - Find the number of days in a given month
 *                        (accounts for leap year in February)
 */

#include <stdio.h>

int main() {
    int month, year;

    printf("Enter month number (1-12): ");
    scanf("%d", &month);

    switch (month) {
        case 1: case 3: case 5: case 7:
        case 8: case 10: case 12:
            printf("31 days\n");
            break;
        case 4: case 6: case 9: case 11:
            printf("30 days\n");
            break;
        case 2:
            printf("Enter the year: ");
            scanf("%d", &year);
            if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0))
                printf("29 days (Leap Year)\n");
            else
                printf("28 days\n");
            break;
        default:
            printf("Invalid month. Enter a number between 1 and 12.\n");
    }

    return 0;
}
