#include<stdio.h>
int main()
{
    int age;
    printf("Enter the age : ");
    scanf("%d", &age);
    (age<=18)?(printf("eligible for voting\n")):(printf("not eligible for voting\n"));
    
    return 0;
}
