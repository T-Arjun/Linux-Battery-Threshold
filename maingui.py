import customtkinter
import subprocess
import getpass

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  
app = customtkinter.CTk()  
app.title("Battery Threshold")
app.geometry("400x240")

sudo_password = getpass.getpass("Enter sudo password: ")

def run_command(command):
    try:
        
        result = subprocess.run(['sudo', '-S'] + command.split(), input=sudo_password + '\n', text=True, capture_output=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

def button_function_per():
    run_command("bat threshold 60")

def button_function_bal():
    run_command("bat threshold 80")

def button_func_full():
    run_command("bat threshold 100")


button = customtkinter.CTkButton(master=app, text="Permanent Mode", command=button_function_per)
button.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Balanced Mode", command=button_function_bal)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Full Capacity", command=button_func_full)
button.place(relx=0.5, rely=0.75, anchor=customtkinter.CENTER)

app.mainloop()