s = [1,1,1,0,1,0,1]
def findMaxConsecutiveOnes(s):









'''
i=0,num=[1],Max=1
i=1,num=[1,1],len(num)>Max=1    -> Max=len(num)=2
i=2,num=[1,1,1],len(num)>Max=2  -> Max=len(num)=3
i=3,num=[]
i=4,num=[1],len(num)<Max
i=5,num=[]
i=6,num[1],len(num)<Max
'''
