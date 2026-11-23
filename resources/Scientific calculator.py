number1 = float(input("Enter the a number: \t\t"))
opperation = input("choose the opperation: \noption 1: + \noption 2: - \noption 3: * \noption 4: / \noption 5: x^2 \noption 6: x^y:\n ")


if opperation == '1':
    number2 = float(input("Enter the second number: \t\t"))
    total = number1 + number2

elif opperation == '2':
   number2 = float(input("Enter the second number: \t\t"))
   total = number1 - number2

elif opperation == '3':
   number2 = float(input("Enter the second number: \t\t"))
   total = number1 * number2

elif opperation == '4':
   number2 = float(input("Enter the second number: \t\t"))
   total = number1/number2

elif opperation == '5':
   total = number1 * number1

elif opperation == '6':
   e = input("choose your exponent: \t\t")
   total = float(number1) **float(e)

else:
   print("You did not enter an operation")


print("the problem =\t\t\t", number1, opperation, number2, '=', total)
print("Your total is\t\t\t", total)