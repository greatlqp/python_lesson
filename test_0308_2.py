'''
height = raw_input('pls input your height(cm)')
weight = raw_input('pls input your weight(kg)')
height = float(height)/100
w = float(w)
bmi = w/h**2
print(bmi)
if bmi > 30:
    print('you are heavy')
elif 30 >= bmi > 18:
    print('you are healthy')
else:
    print('you are thin')
'''
username = raw_input('pls type username: ')
age = raw_input('pls type your age: ')
age = int(age) # 'str' format to 'inter'
if username == 'Mary' and age == 60:
    print('I hate you')
    print('who')

'''
elif username == 'Lucy' and age == 20:
    print('I love you')
else:
    print('Who are you?')
'''        
