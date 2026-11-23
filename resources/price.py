item1 = float(input("scan item:\t\t\t"))
item2 = float(input("scan item:\t\t\t"))
item3 = float(input("scan item:\t\t\t"))

subtotal = item1 + item2 + item3

province = input("which province tax do you want?: \t")

if province == 'ontario':
    print ("the tax is: 13%")
    tax = subtotal * 0.13
    total = subtotal + tax

elif province == 'alberta':   
    print ("the tax is: 5%") 
    tax = subtotal * 0.05
    total = subtotal + tax

elif province == 'british columbia':
    print ("the tax is: 12%")
    tax = subtotal * 0.12
    total = subtotal + tax

elif province == 'manitoba':
    print ("the tax is: 12%")
    tax = subtotal * 0.12
    total = subtotal + tax

elif province == 'saskatchewan':
    print ("the tax is: 11%")
    tax = subtotal * 0.11
    total = subtotal + tax

elif province == 'quebec':
        print ("the tax is: 14.975%")
        tax = subtotal * 0.14975
        total = subtotal + tax


print("your total cost is: \t\t\t", total, ("\n\nthank you for using our service!"))