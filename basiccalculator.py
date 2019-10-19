# Feligbasic szamologep. Keszitette: Drogon. Verzioja: 1.0
print("")
print("Welcome to my basic calculator, which will be my first bigger project in Python 3.\nThere might be bugs. If you find any of thoose, please contact me.\nTo start please write a word from the possibilities, sum;sub;mul;div.\nIf you don't know what do sum,sub,mul and div words stand for, please write \"help\" in the chat.")
operation = input()
if operation == "sum":    #summation starts from here
    print("Your chosen operation is summation")
    print("To start the summation please enter your first number.")
    try:
        firstnumber = input()
        if float(firstnumber) % 1 > 0:
            firstnumber = float(firstnumber)
        elif float(firstnumber) % 1 == 0:
            firstnumber = int(firstnumber)
        print("To continue the summation please enter another number.")
        secondnumber = input()
        if float(secondnumber) % 1 > 0:
            secondnumber = float(secondnumber)
        elif float(secondnumber) % 1 == 0:
            secondnumber = int(secondnumber)
        amount = float(firstnumber)+float(secondnumber)
        if float(amount) % 1 == 0:
            amount = int(amount)
        print(str(firstnumber) + " + " + str(secondnumber) + " = " + str(amount))
    except ValueError:
        print("There is an error. You might distyped something. You could write only numbers here.")
elif operation == "sub":    #substraction starts from here
    print("Your chosen operation is subtraction")
    print("To start the subtraction please enter your minuend.")
    try:
        firstnumber = input()
        if float(firstnumber) % 1 > 0:
            firstnumber = float(firstnumber)
        elif float(firstnumber) % 1 == 0:
            firstnumber = int(firstnumber)
        print("To continue the subtraction please enter your subtrahend.")
        secondnumber = input()
        if float(secondnumber) % 1 > 0:
            secondnumber = float(secondnumber)
        elif float(secondnumber) % 1 == 0:
            secondnumber = int(secondnumber)
        amount = float(firstnumber) - float(secondnumber)
        if float(amount) % 1 == 0:
            amount = int(amount)
        print(str(firstnumber) + " - " + str(secondnumber) + " = " + str(amount))
    except ValueError:
        print("There is an error. You might distyped something. You could write only numbers here.")
elif operation == "mul":    #multiplication starts from here
    print("Your chosen operation is multiplication")
    print("To start the multiplication please enter your multiplicand.")
    try:
        firstnumber = input()
        if float(firstnumber) % 1 > 0:
            firstnumber = float(firstnumber)
        elif float(firstnumber) % 1 == 0:
            firstnumber = int(firstnumber)
        print("To continue the multiplication please enter your multiplier.")
        secondnumber = input()
        if float(secondnumber) % 1 > 0:
            secondnumber = float(secondnumber)
        elif float(secondnumber) % 1 == 0:
            secondnumber = int(secondnumber)
        amount = float(firstnumber)*float(secondnumber)
        if float(amount) % 1 == 0:
            amount = int(amount)
        print(str(firstnumber) + " * " + str(secondnumber) + " = " + str(amount))
    except ValueError:
        print("There is an error. You might distyped something. You could write only numbers here.")
elif operation == "div":    #division starts from here
    print("Your chosen operation is division")
    print("To start the division please enter your dividend.")
    try:
        firstnumber = input()
        if float(firstnumber) % 1 > 0:
            firstnumber = float(firstnumber)
        elif float(firstnumber) % 1 == 0:
            firstnumber = int(firstnumber)
        print("To continue the multiplication please enter your divider.")
        secondnumber = input()
        if float(secondnumber) % 1 > 0:
            secondnumber = float(secondnumber)
        elif float(secondnumber) % 1 == 0:
            secondnumber = int(secondnumber)
        amount = float(firstnumber)/float(secondnumber)
        if float(amount) % 1 == 0:
            amount = int(amount)
        print(str(firstnumber) + " / " + str(secondnumber) + " = " + str(amount))
    except ValueError:
        print("There is an error. You might distyped something. You could write only numbers here.")
elif operation == "help":
    print("Sum = Summation")
    print("Sub = Subtraction")
    print("Mul = Multiplication")
    print("Div = Division")
else:
    print("There is an error. You might mistyped something. Please check your operation. (At the moment there are only 4 pre-programmed operations.)")

