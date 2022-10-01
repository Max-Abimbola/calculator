
from audioop import mul
import tkinter as tk
from tkinter import *
from tkinter import ttk
from turtle import window_height, window_width
from math import *

#main window function
def create_window():
    root = tk.Tk()

    global expression 

    

    root.title("Calculator")

    root.geometry("430x560")

    root.configure(bg="#C79393")


    root.resizable(False,False)

    #gets the dimensions of the screen so calculator can be centered on screen
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    print("Width",windowWidth,"Height",windowHeight)
    
    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    
    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

    # "wrapper" that holds the display onto which numbers will be entered
    display_frame = Frame(root,width=420,height=72)
    display_frame.pack()

    global display

    display = Entry(display_frame)
    display.pack()
    display.configure(font=("Ariel",72))

    

    # Button "wrapper" that holds buttons so that they can be organised into specific location on window
    button_frame = Frame(root,width=400,height=428, bg="#C79393")
    button_frame.pack()

    # Creation of all the buttons that when pressed display the shown symbol onto the screen
    seven = Button(button_frame,text="7",command=lambda:pushButton("7"))
    seven.place(x=0, y=0,height=107, width=100)

    eight = Button(button_frame,text="8",command=lambda:pushButton("8"))
    eight.place(x=100, y=0,height=107, width=100)

    nine = Button(button_frame,text="9",command=lambda:pushButton("9"))
    nine.place(x=200, y=0,height=107, width=100)

    divide = Button(button_frame,text="÷",command=lambda:pushButton("/"))
    divide.place(x=300, y=0,height=107, width=100)


    four = Button(button_frame,text="4",command=lambda:pushButton("4"))
    four.place(x=0, y=107,height=107, width=100)

    five = Button(button_frame,text="5",command=lambda:pushButton("5"))
    five.place(x=100, y=107,height=107, width=100)

    six = Button(button_frame,text="6",command=lambda:pushButton("6"))
    six.place(x=200, y=107,height=107, width=100)

    multiply = Button(button_frame,text="X",command=lambda:pushButton("*"))
    multiply.place(x=300, y=107,height=107, width=100)


    one = Button(button_frame,text="1",command=lambda:pushButton("1"))
    one.place(x=0, y=214,height=107, width=100)

    two = Button(button_frame,text="2",command=lambda:pushButton("2"))
    two.place(x=100, y=214,height=107, width=100)

    three = Button(button_frame,text="3",command=lambda:pushButton("3"))
    three.place(x=200, y=214,height=107, width=100)

    plus = Button(button_frame,text="+",command=lambda:pushButton("+"))
    plus.place(x=300, y=214,height=107, width=100)


    zero = Button(button_frame,text="0",command=lambda:pushButton("0"))
    zero.place(x=0, y=321,height=107, width=100)

    clear = Button(button_frame,text="CLR",command=lambda:clsc())
    clear.place(x=100, y=321,height=107, width=100)

    equals = Button(button_frame,text="=",command=lambda:evaluate())
    equals.place(x=200, y=321,height=107, width=100)

    subtract = Button(button_frame,text="-",command=lambda:pushButton("-"))
    subtract.place(x=300, y=321,height=107, width=100)

    

    root.mainloop()

# function that puts symbol onto screen when button is pressed
def pushButton(symbol):
    display.insert(len(display.get()),symbol)

# function that evaluates the expression that has been created on screen by the user and displays it onto the screen
def evaluate():
    current_screen = display.get()
    evaluation = eval(current_screen)
    display.delete(0,"end")
    display.insert(0,evaluation)
    
# Ffnction that when called clears the calculator screen
def clsc():
    display.delete(0,"end")


    


if __name__ == "__main__":
    create_window()