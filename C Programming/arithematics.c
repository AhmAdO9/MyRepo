#include<stdio.h>
#include<math.h>

int main(){
    int a  = 4;
    int b = 8;
    printf("The value of a + b is: %d\n", a + b);
    printf("The value of a - b is: %d\n", a - b);
    printf("The value of a * b is: %d\n", a * b);
    printf("The value of a / b is: %f\n", a / b);       
    printf("The value of a / b is: %f\n", pow(2,3));
    int num;
    scanf("%d", &num);
    printf("%d", num%97);
    return 0;
}
