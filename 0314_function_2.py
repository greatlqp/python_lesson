def sum(a, b):
    start, end, step = a, b, 1  # a=3, b=5
    total=0
    for i in range(start, end+1, step): # [3, 4, 5]
        total = total + i   # total = 0+3=3
                            # total = 3+4=7 
                            # total = 7+5=12  
    return total

print(sum(3,7))
