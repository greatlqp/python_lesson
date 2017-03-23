def a(s):
    n=len(s)                #n=4
    for i in range(0,n-1):  # Top = 0,1,2
        for j in range(i+1,n):   # Bottom = 1,2,3
           #  print(i,j)
            if s[i] > s[j]:
                s[i],s[j]=s[j],s[i] #fix value in list
                #print(str(s[i])+" "+str(s[j]))
                #print s
def b(s):
    n=len(s)                #n=4
    for i in range(0,n-1):  # Top = 0,1,2
        for j in range(i+1,n):   # Bottom = 1,2,3
           #  print(i,j)
            if s[i] > s[j]:
                s[i],s[j]=s[j],s[i] #fix value in list
                #print(str(s[i])+" "+str(s[j]))
                #print s
print(s)
bubble_sort(s)
print(s)
