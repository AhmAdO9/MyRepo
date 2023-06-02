#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int number, n, guesses=0;
    srand(time(0));
    number = rand() % 100 + 1;\
    // printf("%d", number);
    do
    {
        printf("guess a number: ");
        scanf("%d", &n);
        if (n < number)
        {
            printf("a little higher\n");
        }
        else if (n > number)
        {
            printf("a little lower\n");
        }
        else if (n == number)
        {
            printf("you guessed it in %d attempts\n", guesses);
        }
        guesses++;
    }while(n != number);

    return 0;
}