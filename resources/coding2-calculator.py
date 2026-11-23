number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
opperation = input("Enter the opperation: ")

if opperation == '+':
    total = number1 + number2
elif opperation == '-':
 total = number1 - number2
elif opperation == '*':
  total = number1 * number2
elif opperation == '/':
   total = number1/number2
else:
   print("You did not enter an operation")

print("Your total is", total)
