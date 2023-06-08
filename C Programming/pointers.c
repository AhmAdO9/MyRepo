#include<stdio.h>
#include<stdlib.h>

int main(){
    int i =4;
    int *j = &i;
    int **k = &j;
    int ***l = &k;
    printf("value of i is: %u\n", &i);
    printf("value of i is: %u\n", *j);
    // printf("value of i is: %u\n", k);
    // printf("value of i is: %u\n", l);
    // printf("value of i is: %u\n", j);
    // printf("value of j is: %u", &j);
    return 0;
}