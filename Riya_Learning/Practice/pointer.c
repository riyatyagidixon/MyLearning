#include<stdio.h>

int main()
{
    int a = 44;
    int *p = &a;

    printf("a = %d\n", a);
    printf("p = %p\n", p);
    printf("*p = %d\n", *p);
    printf("&p = %p\n", &p);

    char c = 'a';
    char *ptr = &c;

    printf("c = %c\n", c);
    printf("ptr = %p\n", ptr);
    printf("*ptr = %c\n", *ptr);
    printf("&ptr = %p\n", &ptr);

    return 0;
}
