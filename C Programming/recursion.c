#include <stdio.h>
#include <stdlib.h>
void pattern(int n);





int main(){
    int n = 3;
    pattern(n);
    return 0;
}


void pattern(int n)
 {  int i;
    if (n == 1){
    printf("*\n");
    return;  
  } 
    pattern(n-1);
    for (i=0; i<2*n-1; i++)
    {
    printf("*"); 
    }
    printf("\n");

}
