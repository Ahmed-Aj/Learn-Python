def ReadNumber(text):
    read = False
    while not read:
        try:
            number = int(input(text))
        except ValueError:
            print("Error: You have to enter a number.")
        else:
            read = True
    return number


def addition():
    num1 = ReadNumber("Enter a number(integer): ")
    num2 = ReadNumber("Enter another number(integer): ")
    print("The result is: ", num1 + num2)


def subtraction():
    num1 = ReadNumber("Enter a number(integer): ")
    num2 = ReadNumber("Enter another number(integer): ")
    print("The result is: ", num1 - num2)


def multiplication():
    num1 = ReadNumber("Enter a number(integer): ")
    num2 = ReadNumber("Enter another number(integer): ")
    print("The result is: ", num1 * num2)


def division():
    num1 = ReadNumber("Enter a number(integer): ")
    num2 = ReadNumber("Enter another number(integer): ")
    try:
        result = num1/num2
    except ZeroDivisionError:
        print("Zero division is not allowed")
    else:
        print("The result is: ", result)


def calculator():
    end = False
    while not end:
        option = ReadNumber("Option:")
        if option == 1:
            addition()
        elif option == 2:
            subtraction()
        elif option == 3:
            multiplication()
        elif option == 4:
            division()
        elif option == 5:
            print("Good bye!!")
            end = True


print(""""
    ******************
        Calculator 
    ******************
    """)

print("Menu: \n"
      " 1) Addition\n "
      "2) Subtraction\n "
      "3) Multiplication\n "
      "4) Division\n "
      "5) Exit\n ")
calculator()
