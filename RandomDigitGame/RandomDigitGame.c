#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    srand(time(NULL)); 

    printf("Welcome to the Random Digit Game!\n");
    printf("We have 3 levels for you to choose:\n");
    printf("1. Easy (1-9)\n");
    printf("2. Medium (1-99)\n");
    printf("3. Hard (1-999)\n");
    printf("Please select your level (1, 2, or 3): ");

    int level;
    scanf("%d", &level);

    if (level < 1 || level > 3) {
        printf("Invalid level. Please restart and choose 1, 2, or 3.\n");
        return 1;
    }

    printf("You selected level %d.\n", level);

    short num, user_num;
    int attempts = 0;

    switch (level) { 
        case 1:
            printf("Starting Easy Level (1-9)...\n");
            num = (rand() % 9) + 1;
            printf("Enter a number between 1 and 9: ");
            while (1) {
                scanf("%hd", &user_num);
                if (user_num < 1 || user_num > 9) {
                    printf("Invalid input. Please enter a number between 1 and 9: ");
                    continue;
                }
                attempts++;
                if (user_num < num) {
                    printf("Too low! Try again: ");
                } else if (user_num > num) {
                    printf("Too high! Try again: ");
                } else {
                    printf("Correct! You guessed it in %d attempts.\n", attempts);
                    break;
                } 
            }
            break;
        case 2:
            printf("Starting Medium Level (1-99)...\n");
            num = (rand() % 99) + 1;
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
            break;
        case 3:
            printf("Starting Hard Level (1-999)...\n");
            num = (rand() % 999) + 1;
            printf("Enter a number between 1 and 999: ");
            while (1) {
                scanf("%hd", &user_num);
                if (user_num < 1 || user_num > 999) {
                    printf("Invalid input. Please enter a number between 1 and 999: ");
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
            break;
        default:
            printf("Level not implemented yet.\n");
            break;
    }

    return 0;
} 