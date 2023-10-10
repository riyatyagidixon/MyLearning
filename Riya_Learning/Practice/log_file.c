#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdlib.h>

int main()
{
    FILE *fp = NULL;
    fp = fopen("mylog.txt", "w+");

    if(fp == NULL)
    { 
        printf("file not found\n" );
        return -1;
    }
    while(1)
    {
       // sleep(1);
        fprintf(fp, "Riya is hereeeeeeeee\n");
        printf("Riya is hereeee\n");  
    }
    fseek(fp, 0L, SEEK_END);
    printf("%ld", ftell(fp));

    fclose(fp);
    return 0; 
        
    char file[] = {"mylog.txt"};
    long int result = findfileSize(file);
    if(result != -1)
    printf("Size of the file is %ld", result);
    
    
}
