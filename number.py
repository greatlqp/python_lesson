# gcd.py
def gcd(a,b):           #a=42,b=75  |75,42
    if b !=0:           #b=75       |42
        return gcd(b,a%b)#gcd(75,42)|gcd(42,33)|gcd(3,0)
    else:               #b=0
        return a        #gcd(3,0)=3.... return a

# lcd.py
def lcd(a,b):
    return a*b/gcd(a,b)
