import customtkinter as ctk


app = ctk.CTk()
app.title("Converter Tool")
app.geometry("600x300")

frame = ctk.CTkFrame(app)
frame.pack(padx=20, pady=20)

number = ctk.CTkEntry(frame, width = 40)
number.grid(row=0, column=0, padx=5, pady=5)

def conversion(choice):
    answer=0.0
    try:
        if choice == "from meters(m) to centimeters(cm)":
            answer = float(number.get())
            answer = answer * 100
            coverted_number.configure(text=f"{str(answer)} cm")
        elif choice == "from metres(m) to killometres(km)":
            answer = float(number.get())
            answer = answer / 1000
            coverted_number.configure(text=f"{str(answer)} km")
        elif choice == "from killometer(km) to centimeter(cm)":
            answer = float(number.get())
            answer = answer * 100000
            coverted_number.configure(text=f"{str(answer)} cm")
        elif choice == "from killometers(km) to meters(m)":
            answer = float(number.get())
            answer = answer * 1000
            coverted_number.configure(text=f"{str(answer)} m")
        elif choice == "from centimeters(cm) to meters(m)":
            answer = float(number.get())
            answer = answer / 100
            coverted_number.configure(text=f"{str(answer)} m")
        elif choice == "from centimeters(cm) to killometeres(km)":
            answer = float(number.get())
            answer = answer / 100000
            coverted_number.configure(text=f"{str(answer)} m")
    except:
        coverted_number.configure(text="error")

arrow = ctk.CTkLabel(frame, text = "⇒")
arrow.grid(row=0, column=1, padx=5, pady=5)

coverted_number = ctk.CTkLabel(frame, text = "     ", width = 40)
coverted_number.grid(row=0, column=2, padx=5, pady=5)

converter = ctk.CTkOptionMenu(frame, values=["from meters(m) to centimeters(cm)", "from metres(m) to killometres(km)", "from killometer(km) to centimeter(cm)", "from killometers(km) to meters(m)", "from centimeters(cm) to meters(m)", "from centimeters(cm) to killometeres(km)"], command=conversion)
converter.grid(row=1, column=1, padx=5, pady=5)

app.mainloop()