import customtkinter as ctk

# Create window
app = ctk.CTk()
app.title("Login Example")
app.geometry("400x300")

#label
title_label = ctk.CTkLabel (app, text="Student Login:")
title_label.pack()

# Create frame
login_frame = ctk.CTkFrame(app)
login_frame.pack(padx=20, pady=20)

# Username
username_label = ctk.CTkLabel(login_frame, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)

username_entry = ctk.CTkEntry(login_frame)
username_entry.grid(row=0, column=1, padx=25, pady=25)

# Password
password_label = ctk.CTkLabel(login_frame, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)

password_entry = ctk.CTkEntry(login_frame, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

#checkbox
checkbox = ctk.CTkCheckBox(login_frame, text="Remmember Me")
checkbox.grid(row=2, column = 0, columnspan=2, pady= 10)

def on_button_click():
    done = "loged in"
    login_button.configure (text = done)
    login_button.configure(state="disabled")

# Button
login_button = ctk.CTkButton(login_frame, text="Login", command = on_button_click)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

app.mainloop()