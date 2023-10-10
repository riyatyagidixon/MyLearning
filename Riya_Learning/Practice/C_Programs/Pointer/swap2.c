#include <stdio.h>
void swap(int*, int*);
int main()
{
    int x, y;
    printf("enter the value of x: ");
    scanf("%d",&x);
    printf("enter the value of y:");
    scanf("%d",&y);

    int *c = &x;
    int *d = &y;

    swap(c, d);
    printf("Swap numbers : x=%d y=%d\n", x,y);
    return 0;
}
    void swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
    printf("values of a=%d anb b=%d \n", *a, *b);

}

