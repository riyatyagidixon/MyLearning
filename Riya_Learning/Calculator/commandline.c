#include <stdio.h>

int main(int argc, char *argv[])
{
    printf("argc = %d\n", argc);
    
    for(int i=0; i<argc; i++)
    {
        printf("argv[%d] = %s\n", i, argv[i]);
        printf("argv[%d] = %s\n", 2000, argv[2000]);
    }
    return 0;
}

