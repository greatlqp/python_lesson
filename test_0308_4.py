'''
guess = raw_input('guess my name: ')
while guess != 'Mary':
    print('try again, lol')
    guess = raw_input('guess my name: ')
print('congrats') 
'''
while True:
    guess = raw_input('guess my name: ')
    if guess != 'Mary':
        print('try agian, lol')
        #break # out of "while-loop"
        continue
    #else:
        #print('try again, lol')
    print('congrats')

