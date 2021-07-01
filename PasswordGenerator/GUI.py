import tkinter as tk
import os
import random
from tkinter.constants import DISABLED, W
from tkinter.filedialog import asksaveasfile, askopenfilename


chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+[];:,.<>/?'
passwords_savepath = "D://Passwords.txt"
f = open(passwords_savepath, "a")


def show_entry_fields():
    print("Website: %s\nPassword Length: %s\nNumber of Passwords %s" %
          (e1.get(), e2.get(), e3.get()))


def generator():
    passwords = ''
    generated = 'Password Generated!'
    my_label = tk.Label(root, text=generated)
    my_label.grid(row=4, column=1)

    show_entry_fields()

    passnum = int(e3.get())
    passlen = int(e2.get())
    webname = e1.get()

    for pwd in range(passnum):
        for i in range(passlen):
            passwords += random.choice(chars)
        f.write("Website: " + webname + "\nPassword: " + passwords + "\n")
    if passnum != 1:
        b1.configure(state="disabled")
    elif passnum == 1:
        b1.configure(state="normal")
        e4.configure(state="normal")
        e4.insert(0, passwords)
        e4.configure(state="disabled")


def countdown(time):
    if time == -1:
        root.destroy()
    else:
        if time == 0:
            countdown_label.configure(text="Shutting Down")
        else:
            countdown_label.configure(text="Time remaining: %d seconds" % time)

        root.after(1000, countdown, time-1)


def copy_to_clipboard():
    field_value = e4.get()  # get field value from event
    root.clipboard_clear()  # clear clipboard content
    root.clipboard_append(field_value)    # append new value to clipboard


def ask_savepath():
    files = [('All Files', '*.*'), ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes=files, defaultextension=files)


def open_file():
    file_location = os.path.dirname(os.path.abspath(passwords_savepath))
    os.startfile(file_location)


root = tk.Tk()
countdown_label = tk.Label(root, width=30)
tk.Label(root, text="Website").grid(row=0)
tk.Label(root, text="Password Length").grid(row=1)
tk.Label(root, text="Number of Passwords").grid(row=2)
tk.Label(root, text="Password").grid(row=3)


e1 = tk.Entry(root)
e2 = tk.Entry(root)
e3 = tk.Entry(root)
e4 = tk.Entry(root, state="disabled")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)


tk.Button(root, text='Generate', command=generator).grid(
    row=4, column=0, sticky=tk.W, pady=4)

b1 = tk.Button(root, text="COPY", command=copy_to_clipboard)
b1.grid(row=3, column=2)

tk.Button(root, text='Chose Save Location',
          command=ask_savepath, state="disabled").grid(row=4, column=1)

tk.Button(root, text='Open File Location',
          command=open_file).grid(row=4, column=2)
# tk.Button(root, text='Quit', command=root.quit).grid(
#     row=3, column=0, sticky=tk.W, pady=4, padx=10)

root.mainloop()
