#include <stdio.h>
void main()
{
    int a, b, c;
    printf("enter the first number a is :\n");
    scanf("%d", &a);
    printf("enter the second number b is: \n");
    scanf("%d", &b);
    printf("enter the third number c is: \n");
    scanf("%d", &c);
    
    if(a>b)
    {
        if(a>c)
        {
            printf("the greater number is %d\n", a);
        }
        else 
        {
            printf("the greater number is %d\n", c);
        }
    }
    if(b>c)
    {
         printf("the greater number is %d\n", b);
    }
    else
    {
         printf("the greater number is %d\n", c);
    }

}

   
