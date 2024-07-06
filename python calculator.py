# Tk: This is the main window of the Tkinter application.
# Entry: This is a widget that allows the user to enter a single line of text.
# Button: This widget is used to create a button that the user can click.
# StringVar: This is a Tkinter variable class that provides a way to manage the value of a widget, such as text in an Entry widget.

from tkinter import Tk,Entry, Button , StringVar

class Calculator:
    def __init__(self,master):
        master.title("Calculator")
        master.geometry("357x420+0+0")
        master.config(bg="gray")
        master.resizable(False,False) 

    def show(self,value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value=''
        self.equation.set(self.entry_value)

    def solve(self):
        result=eval(self.entry_value)
        self.equation.set(result)        

root=Tk()
Calculator=Calculator(root)
root.mainloop()