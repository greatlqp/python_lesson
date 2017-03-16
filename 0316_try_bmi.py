try:
    H = raw_input('pls input your height(cm)')
    W = raw_input('pls input your weight(kg)')
    H = float(H)/100
    W = float(W)
    BMI = W/H**2
    print(BMI)
except Exception as e:
    print('pls try again')
    print(e)
