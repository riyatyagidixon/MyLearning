def fun(n):
    if n==0:
        return    
    print(n)
    fun(n-1)
    print(n)

n= int(input("enter n: "))
fun(n)