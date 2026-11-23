import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.title("Name")
app.geometry("400x300")

# Create a label
Name = customtkinter.CTkLabel(app, text="Enter your name: ")
Name.pack(pady = 20)

name = customtkinter.CTkEntry(app)
name.pack(pady=20)

def on_button_click():
    n = name.get()
    msg = "Hello" + " " + n
    Name.configure(text=msg)


button = customtkinter.CTkButton(app, text="Done", command=on_button_click)
button.pack(pady= 20)



app.mainloop()