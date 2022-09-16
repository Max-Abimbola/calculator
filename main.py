"""
- Get a window working:  DONE
- create buttons 0-9 + - / * : DONE
- change size of window 
- create screen 
- set buttons to display symbols
- set = button to read the problem on screen, calculate result annd then display result
- change icon to calculator
"""

import tkinter as tk 
from tkinter import ttk

root = tk.Tk()

root.title("Calculator")

root.geometry("323x334")

#number buttons

zero = ttk.Button(root, text= "0")

one = ttk.Button(root, text= "1")



two = ttk.Button(root, text= "2")


three = ttk.Button(root, text= "3")


four = ttk.Button(root, text= "4")


five = ttk.Button(root, text= "5")


six = ttk.Button(root, text= "6")


seven = ttk.Button(root, text= "7")
seven.grid(row=0,column=2)

eight = ttk.Button(root, text= "8")
eight.grid(row=0,column=3)

nine = ttk.Button(root, text= "9")


plus = ttk.Button(root,text="+")


plus = ttk.Button(root,text="-")

plus = ttk.Button(root,text="÷")

plus = ttk.Button(root,text="X")

clear = ttk.Button(root,text="CLR")

equals = ttk.Button(root,text="=")

#screen

screen = tk.Button(root, text="fdsfgdfg")
screen.grid(row=0,column=0)

root.resizable(False,False)
root.mainloop()




