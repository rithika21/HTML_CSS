#include<stdio.h>

int fibonacci(int n) {
    if (n == 0)
        return 0;
    else if (n == 1)
        return 0;
    else if (n == 2)
        return 1;
    else
        return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n;

    // Prompt the user to enter a number
    printf("Enter the value of n: ");
    scanf("%d", &n);

    if (n < 0) {
        printf("Enter a valid number greater than or equal to 0.\n");
    } else {
        // Call the fibonacci function and print the result
        int result = fibonacci(n);
        printf("The Fibonacci number at position %d is: %d\n", n, result);
    }

    return 0;
}
