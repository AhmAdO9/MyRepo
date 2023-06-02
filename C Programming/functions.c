#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int sum(int a, int b);
int change(int c);
float area(float side);

float area(float side)
{   float c;
    c = pow(side,2);
    printf("%f\n", c);
    return 0;
}

int sum(int a, int b)
{
    int result;
    result = a + b;
    printf("%d\n", result);
    return 0;
}
int change(int c)
{
    c = 77;
    printf("%d\n", c);

    return 0;
}

int main()
{
    sum(2, 3);

    area(5);
    return 0;
}

// #include <stdio.h>
// #include <stdlib.h>
// void good_morning();
// void good_after_noon();
// void good_evening();
// void display();

// void good_morning()
// {
//     printf("good morning\n");
//     good_after_noon();
// }
// void good_after_noon()
// {
//     printf("good afternoon\n");
//     good_evening();
// }
// void good_evening()
// {
//     printf("good evening");
// }
// void display()
// {
//     return 0;
// }

// int main()
// {
//     good_morning();
//     display();
//     return 0;
// }