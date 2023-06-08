#include<stdio.h>
#include<stdlib.h>
#include<math.h>
// int add(int a, int b);
void swap(int *a, int *b);
// int add(int a, int b){
//     int c;
//     c = a + b;
//     return c; 
// }
int main(){
    int x = 4, y = 7;
    printf("value of a + b is: %d, %d\n", x, y);
    swap(&x, &y);
    printf("value of a + b is: %d, %d\n", x, y );
    return 0;
}

void swap(int *a, int *b){
    int temp;
    *a = 2;
    *b = 5;
    
     

}
