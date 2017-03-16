def fib(n):
    '''
    element1 = 1          # n=1
    element2 = element1   # n=2
    element3 = element1+element2 # n=3
    element(n) = elementn(n-2)+element(n-1)     # n=n
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
                                #i=1, prev=0, current=1,
                                #i=2, prev=1, current=1, 
                                #i=3, aa=prev, prev = current, current=prev+aa   
                               
 
        
