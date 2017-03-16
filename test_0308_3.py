while True:
    sex = raw_input('pls sex: ')
    height = raw_input('pls height: ')
    height = float(height) / 100 
    weight = raw_input('pls weight: ')
    weight = float(weight) 
    bmi = weight / height**2
    '''
    if sex == 'male':
        if bmi >= 25:
            print('heavy')
        elif 25 > bmi >= 22:
            print('healthy')
        else:
            print('thin')
    elif sex == 'female':
        if bmi >= 24:
            print('heavy')
        elif 24 > bmi >= 20:
            print('healthy')
        else:
            print('thin')
    else:
        pass
    '''
    if sex == 'male' and bmi >= 25:
        print('heavy')
    elif sex == 'male' and 25 > bmi >= 22:
        print('healthy')
    elif sex == 'male' and 22 > bmi:
        print('thin')
    elif sex == 'female' and bmi >= 24:
        print('heavy')
    elif sex == 'female' and 24 > bmi >= 20:
        print('healthy')
    elif sex == 'female' and 20 > bmi:
        print('thin')
    else:
        pass
    status = raw_input('go or stop')
    if status == 'go':
        continue
    else:
        break
