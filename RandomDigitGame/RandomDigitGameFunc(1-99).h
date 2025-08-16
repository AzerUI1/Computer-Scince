#include <stdio.h>
#include <stdlib.h>
#include <time.h>

short gen_rand_num() {
    short num = (rand() % 99) + 1; 
    short user_num = 0;
    int attempts = 0;
    printf("Enter a number between 1 and 99: ");
    while (1) {
        scanf("%hd", &user_num);
        if (user_num < 1 || user_num > 99) {
            printf("Invalid input. Please enter a number between 1 and 99: ");
            continue;
        }
        attempts++;
        if (user_num < num) {
            printf("Too low! Try again: ");
        } else if (user_num > num) {
            printf("Too high! Try again: ");
        } else {
            printf("Congratulations! You guessed the number in %d attempts.\n", attempts);
            break;
        }
    }
}    