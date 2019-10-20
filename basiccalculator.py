# Feligbasic szamologep. Keszitette: DrogonDeveloper. Verzioja: 1.1. A jovoben varhato a magyarositasa ennek a projektnek, mivel elsonek angol nyelven irtam meg.
def all():
    print("\nWelcome to my basic calculator, which will be my first bigger project in Python 3.\nThere might be bugs. If you find any of thoose, please contact me.\nTo start please write a word from the possibilities, sum;sub;mul;div;fdiv;mod;exp.\nIf you don't know what do sum,sub,mul,div,fdiv,mod and exp words stand for, please write \"help\" in the chat.")
    def credits():
        print("This was made by DrogonDeveloper. Thank you for using my program.\nI spent approximately 4 hours to make this. This was my first bigger project.\nI will propably make changes in the future versions, who knows :/ . Thanks again.")
    operation = input()
    def summation():    #summation starts from here
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
            print("Would you like to quit, or continue?")
            endingchoice = input()
            if endingchoice == "quit":
                credits()
            elif endingchoice == "continue":
                all()
        except ValueError:
            print("There is an error. You might distyped something. You could write only numbers here.")
    def substraction():    #substraction starts from here
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
            print("Would you like to quit, or continue?")
            endingchoice = input()
            if endingchoice == "quit":
                credits()
            elif endingchoice == "continue":
                all()
        except ValueError:
            print("There is an error. You might distyped something. You could write only numbers here.")
    def multiplication():    #multiplication starts from here
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
            print("Would you like to quit, or continue?")
            endingchoice = input()
            if endingchoice == "quit":
                credits()
            elif endingchoice == "continue":
                all()
        except ValueError:
            print("There is an error. You might distyped something. You could write only numbers here.")
    def division():    #division starts from here
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
            print("Would you like to quit, or continue?")
            endingchoice = input()
            if endingchoice == "quit":
                credits()
            elif endingchoice == "continue":
                all()
        except ValueError:
            print("There is an error. You might distyped something. You could write only numbers here.")
    def floor_division():   #Floor Division starts from here
        print("Your chosen operation is Floor Division")
        print("To start the floor division please enter your dividend.")
        try:
            firstnumber = input()
            if float(firstnumber) % 1 > 0:
                firstnumber = float(firstnumber)
            elif float(firstnumber) % 1 == 0:
                firstnumber = int(firstnumber)
            print("To continue the floor division please enter your divider.")
            secondnumber = input()
            if float(secondnumber) % 1 > 0:
                secondnumber = float(secondnumber)
            elif float(secondnumber) % 1 == 0:
                secondnumber = int(secondnumber)
            amount = float(firstnumber)//float(secondnumber)
            if float(amount) % 1 == 0:
                amount = int(amount)
            print(str(firstnumber) + " // " + str(secondnumber) + " = " + str(amount))
            print("Would you like to quit, or continue?")
            endingchoice = input()
            if endingchoice == "quit":
                credits()
            elif endingchoice == "continue":
                all()
        except ValueError:
            print("There is an error. You might distyped something. You could write only numbers here.")
    def exponentiation():    #exponentiation starts from here
        print("Your chosen operation is Exponentiation")
        print("To start the exponentiation please enter your base.")
        try:
            firstnumber = input()
            if float(firstnumber) % 1 > 0:
                firstnumber = float(firstnumber)
            elif float(firstnumber) % 1 == 0:
                firstnumber = int(firstnumber)
            print("To continue the exponentiation please enter your exponent.")
            secondnumber = input()
            try:
                    amount = float(firstnumber)**float(secondnumber)
                    if float(secondnumber) % 1 > 0:
                        secondnumber = float(secondnumber)
                    elif float(secondnumber) % 1 == 0:
                        secondnumber = int(secondnumber)
                    print(str(firstnumber) + " ** " + str(secondnumber) + " = " + str(amount))
                    print("Would you like to quit, or continue?")
                    endingchoice = input()
                    if endingchoice == "quit":
                        credits()
                    elif endingchoice == "continue":
                        all()
            except OverflowError:
                print("Your number is too big. Please try a smaller number.")
                print("Would you like to quit, or continue?")
                endingchoice = input()
                if endingchoice == "quit":
                    credits()
                elif endingchoice == "continue":
                    all()
        except ValueError:
            print("There is an error. You might distyped something. You could write only numbers here.")
    def modulus():    #modulus starts from here
        print("Your chosen operation is Modulus")
        print("To start the exponentiation please enter your first number.")
        try:
            firstnumber = input()
            if float(firstnumber) % 1 > 0:
                firstnumber = float(firstnumber)
            elif float(firstnumber) % 1 == 0:
                firstnumber = int(firstnumber)
            print("To continue the exponentiation please enter your second number.")
            secondnumber = input()
            if float(secondnumber) % 1 > 0:
                secondnumber = float(secondnumber)
            elif float(secondnumber) % 1 == 0:
                secondnumber = int(secondnumber)
            amount = float(firstnumber) % float(secondnumber)
            if float(amount) % 1 == 0:
                amount = int(amount)
            print(str(firstnumber) + " % " + str(secondnumber) + " = " + str(amount))
            print("Would you like to quit, or continue?")
            endingchoice = input()
            if endingchoice == "quit":
                credits()
            elif endingchoice == "continue":
                all()
        except ValueError:
            print("There is an error. You might distyped something. You could write only numbers here.")
    def help():      #help starts from here
        print("Sum = Summation")
        print("Sub = Subtraction")
        print("Mul = Multiplication")
        print("Div = Division")
        print("Fdiv = Floor Division")
        print("Mod = Modulus")
        print("Exp = Exponentiation\n")
        print("Would you like to quit, or continue?")
        endingchoice = input()
        if endingchoice == "quit":
            credits()
        elif endingchoice == "continue":
            all()
    if operation == "sum":
        summation()
    elif operation == "sub":
        substraction()
    elif operation == "mul":
        multiplication()
    elif operation == "div":
        division()
    elif operation == "fdiv":
        floor_division()
    elif operation == "exp":
        exponentiation()
    elif operation == "mod":
        modulus()
    elif operation == "help":
        help()
all()

