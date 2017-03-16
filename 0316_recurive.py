def f(n): # n>0,  #1,4,9,...f(n)
    if n>=2:
        return n**2+f(n-1) # n=2,  F=2*2+f(1)=5                  
    else:
        return 1
print(f(3))

