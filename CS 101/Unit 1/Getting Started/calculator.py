while True:
    a = float(input("first variable"))
    b = float(input("second variable"))
    x = input("What operation are you looking to do")
    if x == "add":
        print(a + b )
    elif x == "sub" or x == "subtract":
        print(a - b)
    elif x == "multiply": 
        print(a * b)
    elif x == "divide":
        print(a / b)
    elif x == "mod":
        print(a % b)
    z = input("do you want to keep going?")
    if z == "y":
        pass
    else:
        break