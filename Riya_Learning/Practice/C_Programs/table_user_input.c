#include<stdio.h>

int main()
{
    int num, i ;
    printf("Enter the number upto uh wants to see the table:\n");
    scanf("%d", &num);
    for(int j=1; j<=num; j++)
    {
    for(i=1; i<=10; i++)
    {
        printf("%d * %d = %d\n", j, i, (j*i));
    }
    printf("\n");
    }
    return 0;
    }
