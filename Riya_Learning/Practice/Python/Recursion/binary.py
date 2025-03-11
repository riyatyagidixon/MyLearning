#  This recursive function represents the binary representation of the given number

def fun(n):
    if n == 0:
        return 
    fun(n//2)
    print(n % 2)

n = int(input("Enter number: "))
fun(n)
