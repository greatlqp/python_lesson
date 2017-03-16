try:
    x = int(raw_input("Please enter a number: "))
except Exception as e:
    print("Oops!  That was no valid number.  Try again...")
finally:
    print('complete a guess')
