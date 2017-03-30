# test.py
summ = []
while True:
    string = input()
    if string!='quit':
        summ.append(int(string))
        #except ValueError as e:
        #print(e)
    else:  
        break

if summ:
    print('sum={},mean={}'.format(sum(summ),sum(summ)/len(summ))) #format string 
