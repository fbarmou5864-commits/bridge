import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.title("GUI with Button and Label")
app.geometry("4000x3000")

# Create a label
label = customtkinter.CTkLabel(app, text="Hello, CustomTkinter!")
label.grid(3)

fire = customtkinter.CTkLabel(app, text = "FIRE DRILL")
fire.grid(1)
# Define what happens when button is clicked
def on_button_click():
    label.configure(text="Button Clicked!")

# Create a button
button = customtkinter.CTkButton(app, text="Click Me", command=on_button_click)
button.grid(5)

app.mainloop()