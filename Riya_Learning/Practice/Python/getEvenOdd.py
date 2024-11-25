# def getEvenOdd(l):
#     even = [e for e in l if e%2==0]
#     odd = [e for e in l if e%2!=0]
#     return even ,odd

# l=[10,2,3,4,5,20]
# even,odd = getEvenOdd(l)
# print (even)   
# print(odd)

def inSorted(l):
    for i in range(1, len(l)):
        if l[i] < l[i - 1]:  # Check if the current item is less than the previous item
            return False
    return True  # Return True only after checking all elements

l = [2, 3, 9, 5, 6, 7]
print(inSorted(l))  # Output: True

print(sorted(l))