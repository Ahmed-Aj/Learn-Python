def addition():
    num1 = int(input("Enter a number(integer): "))
    num2 = int(input("Enter another number(integer): "))
    print("The result is: ", num1 + num2)


def subtraction():
    num1 = int(input("Enter a number(integer): "))
    num2 = int(input("Enter another number(integer): "))
    print("The result is: ", num1 - num2)


def multiplication():
    num1 = int(input("Enter a number(integer): "))
    num2 = int(input("Enter another number(integer): "))
    print("The result is: ", num1 * num2)


def division():
    num1 = int(input("Enter a number(integer): "))
    num2 = int(input("Enter another number(integer): "))
    print("The result is: ", num1 / num2)


def calculator():
    end = False
    while not end:
        option = int(input("Option:"))
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
