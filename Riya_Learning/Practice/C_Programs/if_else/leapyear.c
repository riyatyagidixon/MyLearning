#include <stdio.h>
void main()
{
    int year;
    printf("Enter the year\n");
    scanf("%d", &year);

    if(year % 400 == 0)
    {
        printf("this is leap year\n");
    }
    else if(year % 100 == 0)
    {
        printf("this is not a leap year\n");
    }
    else if(year % 4 == 0)
    {
        printf("this is a leap year\n");
    }
    else 
    {
        printf("this is not a leap year\n");
    }

}




        
