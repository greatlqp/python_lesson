# Q. raw_input a,b,c -> sum(a,b,c)

def summ():
    a=int(input("a: "))
    z=0
    while a !=0:        # a!=0
        z += a
        a=int(input("a: "))
    return z
        ## return         # sum(a)=a(1)+a(2)
print(summ())
