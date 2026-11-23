price = float(input("enter the price: \t\t\t$"))
province = input("which province tax do you want?: \t")

if province == 'ontario':
    print ("the tax is: 13%")
    total = price * 1.13
elif province == 'alberta':   
    print ("the tax is: 5%") 
    total = price * 1.05
elif province == 'british columbia':
    print ("the tax is: 12%")
    total = price * 1.12
elif province == 'manitoba':
    print ("the tax is: 12%")
    total = price * 1.12
elif province == 'saskatchewan':
    print ("the tax is: 11%")
    total = price * 1.11
elif province == 'quebec':
        print ("the tax is: 14.975%")
        total = price * 1.14975


print("your total cost is: \t\t\t", total, ("\n\nthank you for using our service!"))