# fibo.py
def fib(n): # 1,1,2,3,5,8
    a,b=0,1
    while b<n: # n=10  | b=13 > n=10 => break
        print (b) # b=1,1,2,3,5,8
        #1  |1  |2  |3  |...|8
        a,b=b,a+b
        #1,1|1,2|2,3|3,5|...|8,13|
    print ()

def fib2(n):
    result = []
    a,b=0,1
    while b<n:   #n=10  #b=1|2      |3      |5
        result.append(b)#[1]|[1,2]  |[1,2,3]|[1,2,3,5]
        a,b=b,a+b       #1,1|2,3    |3,5    |5,8
        #return result   # final, can't put in while-loop
    return result
