def fib(n):  #1,1,2,3
    if n>2:
        return fib(n-2)+fib(n-1)                 
    else:
        return 1
print(fib(4))

