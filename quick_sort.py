# quick_sort(a)
s = [5.5,3,22,10]
n = len(s)
                                    
def quick_sort(s):              # s=22 when call function.
    bigger,less=[],[]
    pivot=s[-1] # n+1 會不存在   # pivot=22   
    for i in range(0,n-1):
        if s[i]>pivot:          
            bigger.append(s[i]) # bigger=[]
        else:
            less.append(s[i])   # less=[]
    print (bigger,less)
    if bigger: # not null      
        bigger = quick_sort(bigger) # return 不能使用, 會停在Line15                   
    if less:
        less = quick_sort(less)
    return bigger+[pivot]+less  # pivot=22,bigger=[],less=[] 

