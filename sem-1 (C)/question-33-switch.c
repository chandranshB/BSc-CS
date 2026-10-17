/*
 * Question 32 (Switch) - Check whether a character is an alphabet, digit, or special symbol
 */

#include <stdio.h>

int main() {
    char ch;
    int type;

    printf("Enter a character: ");
    scanf(" %c", &ch);

    if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'))
        type = 1;
    else if (ch >= '0' && ch <= '9')
        type = 2;
    else
        type = 3;

    switch (type) {
        case 1: printf("'%c' is an Alphabet.\n",       ch); break;
        case 2: printf("'%c' is a Digit.\n",           ch); break;
        case 3: printf("'%c' is a Special Symbol.\n",  ch); break;
    }

    return 0;
}
