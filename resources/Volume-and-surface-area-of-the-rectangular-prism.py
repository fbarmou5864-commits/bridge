asked = (input("Do you want to find the surface_area or volume of the rectangular prism?\t\t\t"))

if asked == 'surface_area':
    number_form = (input("Does the length or width or hight have decimals?  yes or no\t\t\t\t"))


    if number_form == 'yes':
        L = float(input("Enter the length: \t\t\t"))
        W = float(input("Enter the width: \t\t\t"))
        H = float(input("Enter the hight: \t\t\t"))
        surface_area = float(2*L*W + 2*L*H + 2*W*H)
        print ("The surface ares is\t\t\t", surface_area)



    elif number_form == 'no':
        L = int(input("Enter the length: \t\t\t"))
        W = int(input("Enter the width: \t\t\t"))
        H = int(input("Enter the hight: \t\t\t"))
        surface_area = int(2*L*W + 2*L*H + 2*W*H)
        print ("The surface ares is\t\t\t", surface_area)


elif asked == 'volume': 
    number_form = (input("Does the length or width or hight have decimals?  yes or no\t\t\t\t"))

    if number_form == 'yes':
        L = float(input("Enter the length: \t\t\t"))
        W = float(input("Enter the width: \t\t\t"))
        H = float(input("Enter the hight: \t\t\t"))
        volume = (float(L*W*H))
        print ("The volume is\t\t\t", volume)

    elif number_form == 'no':
        L = int(input("Enter the length: \t\t\t"))
        W = int(input("Enter the width: \t\t\t"))
        H = int(input("Enter the hight: \t\t\t"))
        volume = (int(L*W*H))
        print ("The volume is\t\t\t", volume)

print("Thank you for using our survise")

