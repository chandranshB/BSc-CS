/*
 * Question 12 - Check whether a person is eligible to drive
 */

#include <stdio.h>

int main() {
    int age;

    printf("Enter your age: ");
    scanf("%d", &age);

    if (age >= 16)
        printf("You are eligible to drive.\n");
    else
        printf("You are not eligible to drive.\n");

    return 0;
}
