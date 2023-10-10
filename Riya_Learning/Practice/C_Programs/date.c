#include <stdio.h>

#pragma pack(1)

struct Date
{
    char day:5;
    int month:4;
    short int year:14;
};

int main()
{
    printf("size of Date = %ld\n", sizeof(struct Date));
    return 0;
}
