while True:
    try:
        x = int(raw_input("Please enter a number: "))
    except:
        print("Oops!  That was no valid number.  Try again...")
    else:
        print('good')
