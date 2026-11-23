import random

#--------------CACULATER FUNCTIONS------------------
def add_them(a,b):
    return a + b
def subtract_them(a,b):
    return a - b
def multiply_them(a,b):
    return a * b
def divide_them(a,b):
    return a/b

#-------------MAIN MENU----------------------------
def main_menu():
    print("Welcome to my calculator!")
    first_number = float(input("Please enter a number between 1 and 10: "))
    second_number = float(input("Please enter another number between 1 and 10: "))

    while True:
        choice = input("""
        What would you like to do?
        a)add
        b)subtract
        c)multiply
        d)divide
        q)quit

        """)

        if choice == "a":
            answer = add_them(first_number, second_number)
            print(first_number, "+", second_number, "=", answer)
        elif choice == "b":
            answer = subtract_them(first_number, second_number)
            print(first_number, "-", second_number, "=", answer)
        elif choice == "c":
            answer = multiply_them(first_number, second_number)
            print(first_number, "x", second_number, "=", answer)
        elif choice == "d":
            answer = divide_them(first_number, second_number)
            print(first_number, "/", second_number, "=", answer)
        elif choice == "q":
            print("Thank you for using my calculater")
            break
        else:
            print("Invalid choice. Please select a, b, c, d, or q.")

        again = input("would you like to perform another calculation")
        if again == "no":
            print ("Thank you for using my calculater")
            break
#--------------------RUNNING THE PROGRAM--------------------
main_menu()