def summ(a, b): # a,a+1,a+2,...,b summary  
    if a >= b:
        return b
    else:                       # a=3, b=7
        return a + summ(a+1,b)  # 3 + 3+1, 
print(summ(3,7))
