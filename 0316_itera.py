def fib(n):   # 1,1,2,3,5,8,...n
    if n > 2:
        prev, current=1, 1
        for i in range(1, n+1, 1): # n=1,f=1 ; n=2,f=1 ; n=3,f=prev+cur
            aa=prev
            prev=current
            current=aa+prev    
            print(prev, current)
        return current
    else:
        return 1
print(fib(5))
