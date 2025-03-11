def print1toN(n):
    if n == 0:
        return 
    print1toN(n-1)
    print(n)

n = int(input("Enter number: "))
print1toN(n)