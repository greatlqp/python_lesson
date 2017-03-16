def fib(n):     # n=3
    # if n<=2, f=1
    if n<=2:
        return 1
    # if n>3..., f=f(n-2)+f(n-1)
    else:
        return fib(n-2)+fib(n-1)
print(fib(3))

    
'''
    start, stop, step = 1, n, 1 
    prev, current=0, 1    
    for i in range(start, stop, step): #n=2, rane(1,2)=[1]
        #prev, current = current, pre+current
        aa = prev 
        prev = current 
        current = prev+aa
        print prev, current
    return current
print(fib(3))
'''
                                #i=1, prev=0, current=1,
                                #i=2, prev=1, current=1, 
                                #i=3, aa=prev, prev = current, current=prev+aa   
                               
 
        
