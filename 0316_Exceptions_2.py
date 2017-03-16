while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except Exception as e:
        print("Oops!  That was no valid number.  Try again...")
        print(e)
