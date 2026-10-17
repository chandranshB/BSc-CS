/*
 * Question 07 - Check if a character is lowercase, uppercase, digit, or special character
 */

#include <stdio.h>

int main() {
    char ch;

    printf("Enter a character: ");
    scanf(" %c", &ch);

    if (ch >= 'a' && ch <= 'z')
        printf("'%c' is a lowercase letter.\n", ch);
    else if (ch >= 'A' && ch <= 'Z')
        printf("'%c' is an uppercase letter.\n", ch);
    else if (ch >= '0' && ch <= '9')  // Fixed: was (ch >= 0 && ch <= 9) which compares ASCII values incorrectly
        printf("'%c' is a digit.\n", ch);
    else
        printf("'%c' is a special character.\n", ch);

    return 0;
}
