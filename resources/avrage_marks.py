import math
name = (input("What is your name? \n"))
mark1 = float(input("Enter the first period mark: \n"))
mark2 = float(input("Enter the second period mark: \n"))
mark3 = float(input("Enter the third period mark: \n"))
mark4 = float(input("Enter the forth period mark: \n"))
final_mark = (mark1 + mark2 + mark3 + mark4) / 4
if final_mark > 80:
    student = ("honor")
elif final_mark == 80:
    student = ("honor")
elif final_mark < 80: 
    student = ("not honor")

final_mark = round(final_mark,2)

if final_mark > 96.67:
    letter_grade = ("A+")
elif final_mark == 96.67:
    letter_grade = ("A+")
elif final_mark > 93.33:
    letter_grade = ("A")
elif final_mark == 93.33:
    letter_grade = ("A")
elif final_mark > 90.0:
    letter_grade = ("A-")
elif final_mark == 90.0:
    letter_grade = ("A-")
elif final_mark > 86.67:
    letter_grade = ("B+")
elif final_mark == 86.67:
    letter_grade = ("B+")
elif final_mark > 83.33:
    letter_grade = ("B")
elif final_mark == 83.33:
    letter_grade = ("B")
elif final_mark > 80.0:
    letter_grade = ("B-")
elif final_mark == 80.0:
    letter_grade = ("B-")
elif final_mark > 76.67:
    letter_grade = ("C+")
elif final_mark == 76.67:
    letter_grade = ("C+")
elif final_mark > 70.0:
    letter_grade = ("C")
elif final_mark == 70.0:
    letter_grade = ("C")
elif final_mark > 60.0:
    letter_grade = ("D")
elif final_mark == 60.0:
    letter_grade = ("D")
elif final_mark > 0.0:
    letter_grade = ("F")
elif final_mark == 0.0:
    letter_grade = ("F")

print("Hi", name, "\n---------------\n", "your period 1 mark is: ", mark1, "\n---------------\n", "your period 2 mark is: ", mark2, "\n---------------\n", "your period 3 mark is: ", mark3, "\n---------------\n", "your period 4 mark is: ", mark4, "\n---------------\n", "your final mark is: ", final_mark, "%", "\n---------------\n", "you are a", student, "\n---------------\n", "you got a", letter_grade, "\n---------------\n", "Thank You For Using Our Suervice!" )