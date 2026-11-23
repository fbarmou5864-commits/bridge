import customtkinter

def b1():
    print("1")

def b2():
    print("2")

def b3():
    print("3")
def b4():
    print("4")
def b5():
    print("5")
def b6():
    print("6")
def b7():
    print("7")
def b8():
    print("8")
def b9():
    print("9")
def b10():
    print("10")
app = customtkinter.CTk()
app.geometry("700x700")

button = customtkinter.CTkButton(app, text="1", command=b1)
button.pack(padx=10, pady=10)

button = customtkinter.CTkButton(app, text="2", command=b2)
button.pack(padx=10, pady=10)

button = customtkinter.CTkButton(app, text="3", command=b3)
button.pack(padx=10, pady=10)

button = customtkinter.CTkButton(app, text="4", fg_color="red", command=b4)
button.pack(padx=10, pady=10)

button = customtkinter.CTkButton(app, text="5", command=b5)
button.pack(padx=10, pady=10)

button = customtkinter.CTkButton(app, text="6", command=b6)
button.pack(padx=10, pady=10)

button = customtkinter.CTkButton(app, text="7", command=b7)
button.pack(padx=10, pady=10)

button = customtkinter.CTkButton(app, text="8", command=b8)
button.pack(padx=10, pady=10)

button = customtkinter.CTkButton(app, text="9", command=b9)
button.pack(padx=10, pady=10)

button = customtkinter.CTkButton(app, text="10", command=b10)
button.pack(padx=10, pady=10)

app.mainloop()