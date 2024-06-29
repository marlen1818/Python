def fib(n):
    if n == 1:
        return 1
    else:
       r = fib(n - 1)
       print(r)
       return(r)
    
    fib(34)