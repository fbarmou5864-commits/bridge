#--------------FUNCTIONS------------------------
def variabels():
    return ("""
    Definition: A variable is a named location used to store information that a program can access and change.
    
    Rules for naming the variabels
    - Must start with a letter (a-z, A-Z) or an underscore _.
    - Can contain letters, numbers, and underscores.
    - Case-sensitive (age, Age, and AGE are different variables).
    - Cannot use Python reserved keywords (e.g., if, for, while).

    Examples:
    first_name = "John"
    ----------
    total_cost = 100.50
    ----------
    # THE UNDERLINED IS A VARIABLE
    """)
def string():
    return("""
     Definition: A string is a sequence of characters enclosed in quotes. Strings can contain letters, numbers, symbols, and spaces.
        Strings should be be created using either single (' ') or double (" ") quote like "Hi" or 'Hi'
    
        Exampels:
        total_cost = 100.50  ------> this not a string
        total_cost = "100.50" -----> this is a string
        """)
def repetition_loobs():
    return("""
    What are Loops?
    Definition: Loops allow you to repeat a block of code multiple times, reducing the need for writing repetitive code manually.
    ------------------------------------
    1. The for Loop
    Definition: The for loop iterates over a sequence (like a list, tuple, or string) or other iterable objects, executing the block of code inside it for each item.

    Syntax:
    for variable in sequence:
    # Code to repeat

    Example: Looping through a list:
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
    print(fruit)

    Looping through a range of numbers:
    for i in range(5):
    print(i)  # Outputs 0, 1, 2, 3, 4
    ------------------------------------
    The while Loop
    Definition: The while loop repeatedly executes a block of code as long as a given condition is true.

    Syntax:
    while condition:
    # Code to repeat

    Example: Counting down from 5:
    count = 5
    while count > 0:
    print(count)
    count -= 1   
    ------------------------------------
    The range() Function
    Definition: The range() function generates a sequence of numbers, often used to specify the number of iterations in a for loop.

    Syntax:
    range(start, stop, step)
    Examples:

    range(5): Generates 0, 1, 2, 3, 4
    range(1, 6): Generates 1, 2, 3, 4, 5
    range(0, 10, 2): Generates 0, 2, 4, 6, 8
    ------------------------------------

    """)
def If_Statements():
    return ("""
Definition: If statements are used to make decisions in your code. They allow the execution of certain blocks of code based on whether a condition is true or false.

Syntax:
if condition:
    # Code to execute if condition is true

Example: Checking if a number is positive:
number = 10
if number > 0:
    print("The number is positive")

Elif Statement
Definition: Stands for "else if" and allows you to check multiple conditions. If the initial condition is false, the program checks the elif conditions.

Syntax:
if condition1:
    # Code to execute if condition1 is true
elif condition2:
    # Code to execute if condition 1 is false and condition2 is true
else:
    # Code to execute if all conditions are false

Example: Checking the grade of a student:
score = 85
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D")

Nested If Statements
Definition: If statements within another if statement. Useful for checking multiple conditions.

Example: Checking if a number is positive and even:
number = 8
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even")
    else:
        print("The number is positive but odd")
else:
    print("The number is not positive")
""")
def Function():
    return ("""
Definition: Functions are reusable blocks of code that perform a specific task. They help to modularize and organize code, making it more readable and maintainable.

Syntax:

def function_name(parameters):
    # Code to execute
    return value

Example: A function that adds two numbers:
def add(a, b):
    return a + b
result = add(5, 3)
print(result)  # Outputs 8

Function Parameters
Definition: Parameters are variables that are passed to a function to customize its behavior.

Types of Parameters:
Required Parameters: Must be provided when calling the function.
Default Parameters: Have a default value if no argument is provided.
Keyword Parameters: Passed by explicitly specifying the parameter name.
Variable-Length Parameters: Allow the function to accept a variable number of arguments.

Examples:
# Default parameter
def greet(name="Guest"):
    return f"Hello, {name}"
print(greet())        # Outputs "Hello, Guest"
print(greet("Alice")) # Outputs "Hello, Alice"

# Variable-length parameters
def add_numbers(*numbers):
    return sum(numbers)
print(add_numbers(1, 2, 3, 4))  # Outputs 10

 Returning Values
Definition: Functions can return values using the return statement. This allows functions to produce output that can be used elsewhere in the program.

Example: A function that returns the square of a number:
def square(number):
    return number * number
result = square(4)
print(result)  # Outputs 16


Returning values:
Definition: Returning a value from a function allows you to pass data back from the function to the caller. This is achieved using the return statement.

Syntax:
def function_name(parameters):
    # Code to execute
    return value

Example: A function that adds two numbers and returns the result:
def add(a, b):
    return a + b
result = add(5, 3)
print(result)  # Outputs 8

Returning Multiple Values
Definition: A function can return multiple values by returning them as a tuple.

Example: A function that returns the sum and product of two numbers:
def calculate(a, b):
    return a + b, a * b
sum_result, product_result = calculate(5, 3)
print(sum_result)      # Outputs 8
print(product_result)  # Outputs 15

Returning None
Definition: If a function does not have a return statement, or if it explicitly returns None, the function returns None by default.

Example: A function that returns nothing:
def greet(name):
    print(f"Hello, {name}")
result = greet("Alice")
print(result)  # Outputs None
""")
def Data_types():
    return("""
A data type describes the kind of information stored in a variable.
Different types of information are stored and used in different ways.

Some common Python data types include:

Integer
An integer is a whole number.

Examples:
age = 16
score = 100
number_of_students = 25

Float
A float is a number containing a decimal.

Examples:
price = 9.99
temperature = 21.5

String
A string is a collection of characters surrounded by quotation marks.

Examples:
name = "Alex"
school = "Central High School"

Boolean
A Boolean value can have one of two possible values
True
False

Examples:
game_over = False
logged_in = True

The data type determines what operations can be performed on a value.
For example:
5 + 3
produces:
8
However:
"5" + "3"
produces:
53
This happens because "5" and "3" are strings, not numbers.

Understanding data types is important because computers need to know how information should be stored and processed.
A data type describes the type of information stored in a variable, such as a number, decimal, text, or True/False value.
""")
#-----------------------------------------------
print("welcome to the computer_science vocab!   ")
while True:
    choice = input("""
    what would you like to learn?
    a) Variabels   
    b) Strings
    c) Repetition & Loops
    d) If Statments
    e) Functions
    f) Data Types
    q) Quit
    """)

    if choice == "a":
        print (variabels())
    elif choice == "b":
        print(string())
    elif choice == "c":
        print(repetition_loobs())
    elif choice == "d":
        print(If_Statements())
    elif choice == "e":
        print(Function())
    elif choice == "f":
        print(Data_types())
    elif choice == "q":
        print("THANK YOU!")
    else:
        print("Invalid choice. Please select a, b, c, d, e, f, q")

    again = input("Would you like to learn again? (y/n): ")
    if again == "n":
            print("Thank you!")
            break