#include <stdio.h>

int sum(int, int);
int multi(int, int);
int sub(int, int);
float div(int, int);

enum calci
{
    ADD = 1,
    SUB,
    MUL,
    DIV
};
int main()
{
    int first, second, con, result;

    printf("Hello World\n");
    
    printf("Enter first number :\n");
    scanf("%d", &first);
    printf("Enter second number :\n");
    scanf("%d", &second);

    printf("Press 1 for addition \nPress 2 for subtraction\n");
    printf("Press 3 for multiplication \nPress 4 for division\n");
    scanf("%d", &con);

    switch(con)
    {
        case ADD:
        {
            result = sum(first , second);
            printf("sum of numbers = %d", result);
            break;
        }
        case SUB:
        {
            result = sub(first , second);
            printf("subtraction of numbers = %d" , result);
            break;
        }
        case MUL:
        {
            result = multi(first , second);
            printf("Multiplication of numbers = %d" , result);
            break;
        }
        case DIV:
        {
            float division = div(first , second);
            if(second == 0)
            {
                printf("cannot be divided by 0\n");
            }
            else
            {
                printf("Division of numbers = %f\n", division);
            }
            break;
        }
        default :
        {
            printf("Enter a valid number\n");
        }
    }
    return 0;
}





