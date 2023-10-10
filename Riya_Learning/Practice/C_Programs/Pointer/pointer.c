#include <stdio.h>
#include <stdlib.h>
int main()
{
    int a = 10;
    printf("value of a = %d\n", a);
    printf("value of address of a = %p\n", &a);
   
    int *b = &a;
    printf("value of b = %p\n", b);
    printf("value at address store at b = %d\n", *b);
    *b = 50;
    printf("value of a = %d\n", a);
    int **x = &b;
    printf("address of b = %p\n", &b); 
    printf("address of b = %p\n", x);
    printf("address of a = %p\n", *x); 
    printf("value at a = %d\n", **x);

    return 0;
} 
