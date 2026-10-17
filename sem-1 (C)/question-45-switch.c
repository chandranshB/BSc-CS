/*
 * Question 44 (Switch) - Menu-driven program to reverse a string or a number
 */

#include <stdio.h>

int my_strlen(char *s) {
    int len = 0;
    while (*s++) len++;
    return len;
}

void reverse_string(char *str) {
    int i = 0, j = my_strlen(str) - 1;
    char temp;
    while (i < j) {
        temp = str[i]; str[i] = str[j]; str[j] = temp;
        i++; j--;
    }
}

long int reverse_number(long int num) {
    long int rev = 0;
    while (num != 0) {
        rev = rev * 10 + num % 10;
        num /= 10;
    }
    return rev;
}

int main() {
    int choice;
    char str[100];
    long int num;

    do {
        printf("\nReverse Menu\n");
        printf("1. Reverse a String\n");
        printf("2. Reverse a Number\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        while (getchar() != '\n');  // flush input buffer

        switch (choice) {
            case 1: {
                printf("Enter a string: ");
                int i = 0;
                char c;
                while ((c = getchar()) != '\n' && i < 99)
                    str[i++] = c;
                str[i] = '\0';
                reverse_string(str);
                printf("Reversed: %s\n", str);
                break;
            }
            case 2:
                printf("Enter a number: ");
                scanf("%ld", &num);
                printf("Reversed: %ld\n", reverse_number(num));
                break;
            case 3:
                printf("Exit.\n");
                break;
            default:
                printf("Invalid choice.\n");
        }
    } while (choice != 3);

    return 0;
}
