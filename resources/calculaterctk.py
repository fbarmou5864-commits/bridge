import customtkinter as ctk
#import StringCalculator as calc

app = ctk.CTk()
app.title("Calculater")
app.geometry("300x600")

cal_frame = ctk.CTkFrame(app)
cal_frame.pack(padx=20, pady=20)

screen = ctk.StringVar(value="")
opperation = ctk.CTkEntry(cal_frame,textvariable=screen)
opperation.pack(pady=20)

isVisible = False

nmbr_frame = ctk.CTkFrame(app)
nmbr_frame.pack(padx=10, pady=10)

all_history = ctk.CTkTextbox(app)
all_history.pack()
all_history.pack_forget()

def cleartext():
    screen.set("")

def backspace():
    a = opperation.get()
    a = a[:-1]
    screen.set(a)

def ansr():
    e = opperation.get()
    all_history.insert("end",e)
    result = eval(e) # calculate
    all_history.insert("end","=")
    all_history.insert("end", f"{result}\n") # add to history
    screen.set(result) # show answer

cal_button1 = ctk.CTkButton(nmbr_frame, text="C", width=40, command=cleartext)
cal_button1.grid(row=0, column=0, padx=5, pady=5)

cal_button2 = ctk.CTkButton(nmbr_frame, text="⌫", width=40,command = backspace)
cal_button2.grid(row=4, column=0, padx=5, pady=5)

cal_button3 = ctk.CTkButton(nmbr_frame, text=")", width=40, command=lambda:opperation.insert("end", ")"))
cal_button3.grid(row=0, column=2, padx=5, pady=5)

cal_button4 = ctk.CTkButton(nmbr_frame, text="÷", width=40, command=lambda:opperation.insert("end", "/"))
cal_button4.grid(row=0, column=3, padx=5, pady=5)

cal_button5 = ctk.CTkButton(nmbr_frame, text="7", width=40, command=lambda:opperation.insert("end", "7"))
cal_button5.grid(row=1, column=0, padx=5, pady=5)

cal_button6 = ctk.CTkButton(nmbr_frame, text="8", width=40, command=lambda:opperation.insert("end", "8"))
cal_button6.grid(row=1, column=1, padx=5, pady=5)

cal_button6 = ctk.CTkButton(nmbr_frame, text="9", width=40, command=lambda:opperation.insert("end", "9"))
cal_button6.grid(row=1, column=2, padx=5, pady=5)

cal_button6 = ctk.CTkButton(nmbr_frame, text="x", width=40, command=lambda:opperation.insert("end", "*"))
cal_button6.grid(row=1, column=3, padx=5, pady=5)

cal_button6 = ctk.CTkButton(nmbr_frame, text="4", width=40, command=lambda:opperation.insert("end", "4"))
cal_button6.grid(row=2, column=0, padx=5, pady=5)

cal_button6 = ctk.CTkButton(nmbr_frame, text="5", width=40, command=lambda:opperation.insert("end", "5"))
cal_button6.grid(row=2, column=1, padx=5, pady=5)

cal_button6 = ctk.CTkButton(nmbr_frame, text="6", width=40, command=lambda:opperation.insert("end", "6"))
cal_button6.grid(row=2, column=2, padx=5, pady=5)

cal_button6 = ctk.CTkButton(nmbr_frame, text="-", width=40, command=lambda:opperation.insert("end", "-"))
cal_button6.grid(row=2, column=3, padx=5, pady=5)

cal_button6 = ctk.CTkButton(nmbr_frame, text="1", width=40, command=lambda:opperation.insert("end", "1"))
cal_button6.grid(row=3, column=0, padx=5, pady=5)

cal_button6 = ctk.CTkButton(nmbr_frame, text="2", width=40, command=lambda:opperation.insert("end", "2"))
cal_button6.grid(row=3, column=1, padx=5, pady=5)

cal_button6 = ctk.CTkButton(nmbr_frame, text="3", width=40, command=lambda:opperation.insert("end", "3"))
cal_button6.grid(row=3, column=2, padx=5, pady=5)

cal_button6 = ctk.CTkButton(nmbr_frame, text="+", width=40, command=lambda:opperation.insert("end", "+"))
cal_button6.grid(row=3, column=3, padx=5, pady=5)

cal_button6 = ctk.CTkButton(nmbr_frame, text="(", width=40, command=lambda:opperation.insert("end", "("))
cal_button6.grid(row=0, column=1, padx=5, pady=5)

cal_button6 = ctk.CTkButton(nmbr_frame, text="0", width=40, command=lambda:opperation.insert("end", "0"))
cal_button6.grid(row=4, column=1, padx=5, pady=5)

cal_button6 = ctk.CTkButton(nmbr_frame, text=".", width=40, command=lambda:opperation.insert("end", "."))
cal_button6.grid(row=4, column=2, padx=5, pady=5)

cal_button6 = ctk.CTkButton(nmbr_frame, text="=", width=40, command=ansr)
cal_button6.grid(row=4, column=3, padx=5, pady=5)


def showhistory():
    global isVisible
    if isVisible == False:
        all_history.pack()
        isVisible = True
    else:
        all_history.pack_forget()
        isVisible = False



cal_button7 = ctk.CTkButton (app, text="🕒", width=40, command=showhistory)
cal_button7.pack(padx=5, pady=5)

app.mainloop()