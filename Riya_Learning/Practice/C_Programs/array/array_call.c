#include <stdio.h>
void myfunc(int arr1[],int size1)
{
    printf("Enter array elements\n" );
    for(int i =0; i<size1; i++)
        scanf("%d", &arr1[i]);
    printf("Enter array elements\n" );
    for(int i =0; i<size1; i++)
        printf("%d\n", arr1[i]);
}
        
void main()
{
    int arr[5] = {1,3,2,4,2};
    int size = sizeof(arr)/sizeof(int);
    printf("size of array = %d\n", size);
    printf("value of arr= %p\n", arr);
    myfunc(arr,size);
    printf("Enter array elements\n" );
    for(int i =0; i<size; i++)
        printf("%d\n", arr[i]);

}

/*array used call by reference method by default*/ 
