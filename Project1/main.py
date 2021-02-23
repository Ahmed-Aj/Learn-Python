end = False
print("""
***********
Calculator
***********""")

print("Menu:\n"
      " 1) Sum\n "
      "2) Subtractions\n "
      "3) Division\n "
      "4) Multiplication\n "
      "5) Exit\n ")
while not end:
    opt = int(input("Option:"))
    if opt == 1:
        num1 = int(input("Enter the first the number(integer):"))
        num2 = int(input("Enter the second the number(integer):"))
        print("Result: ", num1 + num2)
    elif opt == 2:
        num1 = int(input("Enter the first the number(integer):"))
        num2 = int(input("Enter the second the number(integer):"))
        print("Result: ", num1 - num2)
    elif opt == 3:
        num1 = int(input("Enter the first the number(integer):"))
        num2 = int(input("Enter the second the number(integer):"))
        print("Result: ", num1 / num2)
    elif opt == 4:
        num1 = int(input("Enter the first the number(integer):"))
        num2 = int(input("Enter the second the number(integer):"))
        print("Result: ", num1 * num2)
    elif opt == 5:
        print("Good bye!")
        end = True
