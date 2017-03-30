s = [5.5,3,22,10]
def bubble_sort(a):
    n = len(a)
    for i in range(0,n-1):    #0,1,2 |0,n-1
        for j in range(i+1,n):      #1,2,3 |i+1,n   
            if a[i] > a[j]:
                a[i],a[j]=a[j],a[i]
            else:
                pass
print(s)
bubble_sort(s)
print(s)   
