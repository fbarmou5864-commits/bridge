import math
asked = input("Do you want to find the volume (type 1) or the circumference (type 2) of the cylinder?\t\t\t")

if asked == '1': 
    h = float(input("Enter the hight of the cylinder: \t\t\t"))
    r_d = input("Do want to use the radius or the diameter? \t\t\t")
    r_d_n = float(input("Enter the radias or diameter: \t\t\t"))
    if r_d == 'radius': 
        volume = float(r_d_n*r_d_n*h*math.pi)
    elif r_d == 'diameter':
        volume = float(r_d_n/2*r_d_n/2*h*math.pi)
    print ("The volume of the cylinder is:\t\t\t", volume)

elif asked == '2':
    h = float(input("Enter the hight of the cylinder: \t\t\t"))
    r_d = input("Do want to use the radius or the diameter? \t\t\t")
    r_d_n = float(input("Enter the radias or diameter: \t\t\t"))
    if r_d == 'radius':
        circumference = float(2*r_d_n*math.pi)
    elif r_d == 'diameter':
        circumference = float(r_d_n*math.pi)
    print ("The circumfrenece is: ", circumference)
else:
    print ("Looks like you don't want anything! thanks for visiting our website!")

print ("Thank you for using oue survice!")
