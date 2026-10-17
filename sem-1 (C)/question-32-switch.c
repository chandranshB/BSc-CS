/*
 * Question 31 (Switch) - Check whether a character is a vowel or consonant
 */

#include <stdio.h>

int main() {
    char ch;

    printf("Enter an alphabet: ");
    scanf(" %c", &ch);

    // Convert to lowercase for a single switch check
    if (ch >= 'A' && ch <= 'Z')
        ch = ch + 32;

    if (ch >= 'a' && ch <= 'z') {
        switch (ch) {
            case 'a': case 'e': case 'i': case 'o': case 'u':
                printf("'%c' is a vowel.\n", ch);
                break;
            default:
                printf("'%c' is a consonant.\n", ch);
        }
    } else {
        printf("'%c' is not an alphabet.\n", ch);
    }

    return 0;
}
