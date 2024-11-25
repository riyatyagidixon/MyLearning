def triangle(s):
    s=9
    #Complete the code given below
    #Replace ..... by your own code
    for i in range(s):
        if i == s:
            print("*" *s)
            
        elif i == 1:
            print(' ' * (s - i) + '*')
            
        else:
            print(' ' * (s - i) + '*' + ' ' * (i - 2) + '*')