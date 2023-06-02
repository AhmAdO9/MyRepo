// #include<stdio.h>
// #include<stdlib.h>

// int main()
// {
    // int a;
    // int vipPass;
    // printf("write a number:");
    // scanf("%d %d", &a, &vipPass);
    // if((a <20 && a > 12) || (vipPass == 1))
    // {
    //     printf("hello");
    // }
    // else
    // {
    //     printf("Noooooo");
    // }
    // int a, b, c, d;
    // printf("numbers: ");
    // scanf("%d %d %d %d", &a, &b, &c, &d);
    // if (a > b && a > c && a > d)
    // {
    //     printf("greater of all is a %d", a);
    // }
    // else if (b > c && b > d)
    // {
    //         printf("greater of all is b %d", b);
    // }
    // else if (c > d)
    // {
    //     printf("greater of all is c %d", c);
    // }
    // else{
    //     printf("greater of all is d %d", d);
    // }
    


//     return 0;
// }

// #include<stdio.h>
// #include<stdlib.h>

// int main(){
//     char ch;
//     printf("write a letter: ");
//     scanf("%c", &ch);
//     if (ch >= 97 && ch <= 127 )
//     {
//         printf("it's a lower case");

//     }
//     else{
//         printf("it's not a lower case");
//     }

//     return 0;
// }

#include<stdio.h>
#include<stdlib.h>

int main(){
    int a = 0;
    while(a > 100)
    {   
    
        printf("%d\n", a*'$');
        a++;
        
    }
    
    return 0;
}