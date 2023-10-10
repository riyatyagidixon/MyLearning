#include <stdio.h>
void main()
{
    char c;
    printf("Enter any Character:\n");
    scanf("%c", &c);

    if((c>64 && c<91) ||(c>96 && c<123))
    {
        printf("It is an alphabet\n");
    }
    else 
    {
        printf("It is not an alphabet\n");
    }

}



