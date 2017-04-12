s = [1,1,1,0,1,0,1]
def findMaxConsecutiveOnes(s):
    num=[]
    Max = 0
    n=len(s)
    for i in range(0,n):        #i=0,1,2
        if s[i]==1:             #
            num.append(s[i])    #
            Max = len(num)
            print(i,len(num),Max)        # i=4,num=1|i=6,num=1
        else:
            if len(num)>Max:
                return Max
                print(i,Max)    # i=3,Max=3,num=3|i=5,Max=3,num=1
            else:
                num=[]

print(findMaxConsecutiveOnes(s))

'''
i=0,num=[1],Max=1
i=1,num=[1,1],len(num)>Max=1    -> Max=len(num)=2
i=2,num=[1,1,1],len(num)>Max=2  -> Max=len(num)=3
i=3,num=[]
i=4,num=[1],len(num)<Max
i=5,num=[]
i=6,num[1],len(num)<Max
'''
