def fib(n):
    '''
    n: positive ganze Zahl
    returns: n-te Fibonacci Zahl
    '''
    if n <= 2: return 1
    a,b = 1,1
    for i in range(n-2):
        c = a+b
        a,b = b,c
 
    return c

for i in range(30,38):
    print(fib(i))