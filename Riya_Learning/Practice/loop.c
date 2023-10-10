#include <stdio.h>

int main() {
    // Write C code here
    //unsigned char  i=5;
    char  i=5;
    for( ;i; )
    {
        //printf("[%d] [%d]\n",i++, ++i);
        printf("[%d]\n",i++);
        
    }
    printf("======>>>>>%d\n",i);

    return 0;
}
