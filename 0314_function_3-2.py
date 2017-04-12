import time

def fib(n):         # 1,1,2,3,5,8,13
    if n<=2:        # 1,1
        return 1    # -> return 1
    else:
        return fib(n-2)+fib(n-1) # f(n)=Prev+current=f(n-2)+f(n-1)
                                 #      -> f(n-2)=f(n-4)+f(n-3)
                                 #      -> f(n-1)=f(n-3)+f(n-2)

a = time.process_time()
print(fib(3))
b = time.process_time()
print(b-a)
