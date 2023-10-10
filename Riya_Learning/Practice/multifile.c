#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>

int main()
{
    //FILE *files[numfiles];
    FILE *files[10];
    //for (int i = 0; i < numfiles; i++)
    for (int i = 0; i < 10; i++)
    {
        char filename[100];
        sprintf(filename, "file_%d.txt", i);
        files[i] = fopen(filename, "w");
        //printf("%d\n", i); //just to see print statement
    }
return 0;
}
