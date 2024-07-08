from tkinter import *
from random import  randint
from tkinter import messagebox

window=Tk()
window.title('Password Generator')
window.geometry("500x300")
window.resizable(0,0)
window.iconbitmap(r'F:\School\Py Projects\Strong Password Generator\icon\icon.ico')

def new_rand():
    #clear the entry first
    pw_entry.delete(0,END)
    if not my_entry.get():
        messagebox.showwarning ("WARNING!", "Please enter password length!")
        return reset_button

    else:
        # get PW length and convert to int
        pw_length = int(my_entry.get())

        # var to hold the password
        my_password = ''

        # Loop through for password length
        for x in range(pw_length):
            my_password += chr(randint(33, 126))

            # output password
            pw_entry.insert(0, my_password)




def clipper():
    if not pw_entry.get() or not my_entry.get():
        messagebox.showwarning ("WARNING!", "You have not filled all required fields")
    else:
    #clear clipboard
        window.clipboard_clear()
    #copy now
        window.clipboard_append(pw_entry.get())
        messagebox.showwarning("Success!", "Password copied successfully")

def reset():
    if not pw_entry.get() or not my_entry.get():
        messagebox.showwarning ("WARNING!", "Nothing to reset")
    else:
        pw_entry.delete(0,END)
        my_entry.delete(0, END)
        messagebox.showwarning("Success!", "Password reset successfully")


lf =LabelFrame(window, text="How Many Characters?")
lf.pack(pady=20)

#create entry box
my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

#create entry box for returned password
pw_entry =Entry(window, text="", font=("Helvetica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

#create a frame for buttons
my_frame = Frame(window)
my_frame.pack(pady=20)

#create buttons
my_button= Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button =Button(my_frame, text="Copy to Clip Board", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

reset_button =Button(my_frame, text="Reset Password", command=reset)
reset_button.grid(row=0, column=3, padx=10)



window.mainloop()
