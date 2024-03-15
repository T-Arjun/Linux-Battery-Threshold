import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title("Battery Threshold")
app.geometry("400x240")

def button_function_per():
    print("performance mode")

def button_function_bal():
    print("balanced mode ")

def button_func_full():
    print("full capacity mode")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Permanent Mode", command=button_function_per)
button.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Balanced Mode", command=button_function_bal)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Full Capacity", command=button_func_full)
button.place(relx=0.5, rely=0.75, anchor=customtkinter.CENTER)

app.mainloop()