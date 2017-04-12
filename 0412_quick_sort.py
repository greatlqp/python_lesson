# quick_sort(a)
s = [5.5,3,22,10]


def quick_sort(s):              # s=[5.5,3]
    bigger,less=[],[]
    n = len(s)
    pivot=s[-1]                 #pivot=3
    for i in range(0,n-1):      #i=0 range(0,1)
        print(i, n, s)          #i=0,n=2,s=[5.5,3]
        if s[i]>pivot:
            bigger.append(s[i]) # bigger = [5.5]
        else:
            less.append(s[i])   # less= []
    print(bigger,less)
    if bigger: # not null
        bigger = quick_sort(bigger) # return 不能使用, 會停在Line15
    if less:
        less = quick_sort(less)
    return bigger+[pivot]+less  # pivot=22,bigger=[],less=[]

print (s)
s = quick_sort(s)
print (s)

''' pivot=10,bigger=[22],less=[5.5,3]
#1.bigger |s=[22]
pivot=22,bigger=[],less=[]
return[22] to bigger
#1.bigger =[22]

#2.less   |s=[5.5,3]
pivot=3,bigger=[5.5],less=[]
    #2-1. bigger
    pivot=5.5,bigger=[],less=[]
    return[5.5] to bigger
#2. less =
    return[5.5,3]
return [bigger,pivot,less] '''
