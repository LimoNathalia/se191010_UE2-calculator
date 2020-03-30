from tkinter import *

expression = ""
 
# Function to update expressiom
# in the text entry box
def press(num):
    return
    
 
# Function to evaluate the final expression
def equalpress():
    return
 
 
# Function to clear the contents
# of text entry box
def clear():
    return
 
 
# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()
 
    # set the background colour of GUI window
    gui.configure(background="white")
    # set the title of GUI window
    gui.title("LABINF Calculator WSS2018")
    # set the configuration of GUI window
    gui.geometry("400x200")
    # StringVar() is the variable class
    equation = StringVar()
    # create the text entry box for
    expression_field = Entry(gui, textvariable=equation)
    # grid method is used for placing
    expression_field.grid(columnspan=80, ipadx=100)
    equation.set('enter your expression')
 
    # create a Buttons and place at a particular
    button1 = Button(gui, text=' 1 ', fg='black', bg='light grey',command=lambda: press(1), height=1, width=7)
    button1.grid(row=4, column=0)
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='light grey',command=lambda: press(2), height=1, width=7)
    button2.grid(row=4, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='light grey',command=lambda: press(3), height=1, width=7)
    button3.grid(row=4, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='light grey',command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='light grey',command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='light grey',command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='light grey',command=lambda: press(7), height=1, width=7)
    button7.grid(row=2, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='light grey',command=lambda: press(8), height=1, width=7)
    button8.grid(row=2, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='light grey',command=lambda: press(9), height=1, width=7)
    button9.grid(row=2, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='light grey',command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=1)

    


    

 
    plus = Button(gui, text=' + ', fg='black', bg='grey', command=lambda: press("+"), height=1, width=7)
    plus.grid(row=5, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='grey', command=lambda: press("-"), height=1, width=7)
    minus.grid(row=4, column=3)

    multiplication = Button(gui, text=' * ', fg='black', bg='grey', command=lambda: press("*"), height=1, width=7)
    multiplication.grid(row=3, column=3)

    division = Button(gui, text=' / ', fg='black', bg='grey', command=lambda: press("/"), height=1, width=7)
    division.grid(row=2, column=3)

    porcent = Button(gui, text=' % ', fg='black', bg='grey', command=lambda: press("%"), height=1, width=7)
    porcent.grid(row=1, column=2)

    point = Button(gui, text=' . ', fg='black', bg='grey', command=lambda: press("."), height=1, width=7)
    point.grid(row=5, column=0)

    parenthesis1 = Button(gui, text=' ( ', fg='black', bg='grey', command=lambda: press("("), height=1, width=7)
    parenthesis1.grid(row=1, column=0)

    parenthesis2 = Button(gui, text=' ) ', fg='black', bg='grey', command=lambda: press(")"), height=1, width=7)
    parenthesis2.grid(row=1, column=1)
 
    equal = Button(gui, text=' = ', fg='black', bg='red', command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)
 
    clear = Button(gui, text='Clear', fg='black', bg='red', command=clear, height=1, width=7)
    clear.grid(row=1, column=3)

    

    
 
    # start the GUI
    gui.mainloop()