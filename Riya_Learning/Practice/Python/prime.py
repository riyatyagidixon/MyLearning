def isPrime(n):
    if n ==1:
        return False
    for i in range (2,n):
        if n%i == 0:
            return False
    return True

n = int(input("Enter n: "))
print("True") if isPrime(n) else print("False")