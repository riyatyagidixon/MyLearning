#include <stdio.h>
void main()
{
    int num;
    int *myNum = &num;
    char myWord;
    char *myword = &myWord;

   /* printf("the size of num is %lu\n", num);
    printf("the size of myNum is %lu\n", myNum);
    printf("the size of myWord is %lu\n", myWord);*/
    int a = sizeof(myNum);
    int b = sizeof(myword);
    printf("size of int pointer %d\n", a);
    printf("size of char pointer %d\n", b);

}
