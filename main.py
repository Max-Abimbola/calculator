#Function that creates the window DONE
#Create buttons
#Create the text display
#Program the buttons

import tkinter as tk
from tkinter import *
from tkinter import ttk
from turtle import window_height, window_width


def create_window():
    root = tk.Tk()

    global expression 

    expression = " "

    root.title("Calculator")

    root.geometry("400x500")
    #Creating display

    display_frame = Frame(root,width=400,height=72,bg="green")
    display_frame.pack()

    global display

    display = Entry(display_frame)
    display.pack()
    display.configure(font=("Ariel",72))

    

    #Creating buttons
    button_frame = Frame(root,width=400,height=428,bg="blue")
    button_frame.pack()

    one = Button(button_frame,text="hello world",command=lambda:pushButton("1 + 1",expression))
    one.place(x=0, y=0,height=107, width=100)

    equals = Button(button_frame,text="=",command=lambda:pushButton("=",expression))
    equals.place(x=100, y=0,height=107, width=100)

    print(expression)

    

    root.mainloop()

def pushButton(symbol,expression):
    if symbol == "=":
        print(eval(expression))
        print(expression)
        display.insert(0,(eval(expression)))
        return
    else:
        display.insert(0,symbol)
        expression += symbol
        return


    


if __name__ == "__main__":
    create_window()