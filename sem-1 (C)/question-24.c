/*
 * Question 24 - Check whether a number is a perfect square
 */

#include <stdio.h>
#include <math.h>

int main() {
    int num;

    printf("Enter a positive integer: ");
    scanf("%d", &num);

    if (num < 0) {
        printf("%d is not a perfect square (negative numbers don't apply).\n", num);
    } else {
        int root = (int)sqrt((double)num);  // Optimised: use sqrt instead of a loop
        if (root * root == num)
            printf("%d is a perfect square (%d x %d).\n", num, root, root);
        else
            printf("%d is not a perfect square.\n", num);
    }

    return 0;
}
