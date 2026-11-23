name = str(input("What is your name? \n"))
birth_year = int(input("Enter your birth year: \n"))
age = 2026 - birth_year
if age > 18:
    print("You are an adult")
elif age == 18: 
    print("You are an adult")
elif age < 12:
    print ("You are a kid")
elif age >12 :
    print("You are a teenager")
elif age == 12: 
    print("You are a teenager")
elif age > 50:
    print("You are an elder")
# YOU COULD USE ONE OF THESE PEINT STATMENTS:
print ("Hi", name, ", you are", age, "years old")
# print ("Hi"+ name + ", you are" + str(age) + "years old")