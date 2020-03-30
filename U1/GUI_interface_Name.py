from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def nameCallBack():
    output = entry.get()
    messagebox.showinfo (output, output)
    return

root = Tk()

content = ttk.Frame(root)
namelbl = ttk.Label(content, text="what is your name?")
entry = ttk.Entry(content)

onevar = BooleanVar()
onevar.set(True)


ok = ttk.Button(content, text="Okay", command = nameCallBack)
cancel = ttk.Button(content, text="Cancel")

content.grid(column=0, row=0)
namelbl.grid(column=3, row=0, columnspan=20)
entry.grid(column=3, row=1, columnspan=20)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

root.mainloop()