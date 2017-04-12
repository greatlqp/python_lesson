import fibo

def summ(a, b):         
    if a >= b:
        return b
    else:
        return a+summ(a+1,b)

print(summ(3,9))
     