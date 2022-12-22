#import Calculator
import math
constant = 1
inverse_constant = 1
def exp(x,y):
    return(math.pow(x,y))
def sqrt(x):
    try:
       return(math.sqrt(x))
    except:
        print('Input should be positive(greater than 0)')
def sin(x):
    n = ((x*(math.pi))/180)
    return(math.sin(n*constant))
def cos(x):
    n = ((x*(math.pi))/180)
    return(math.cos(n*constant))
def tan(x):
    try:
       n = ((x*(math.pi))/180)
       return(math.tan(n*constant))
    except:
       print('Value tending to infinity!!!')
def ln(x):
    try:
        return(math.log(x))
    except:
        print('Invalid input')
def ln1(x):
    try:
        return(math.log10(x))
    except:
        print('Invalid input')
def sqr(x):
    return(math.pow(x,2))
def cube(x):
    return(math.pow(x,3))
import tkinter
class CalculatorUsingGUI:
    def click(self,num):
        global expression
        self.expression = self.expression + str(num)
        self.equation.set(self.expression)
    def exit1(self):
        self.parent.destroy()
    def clear(self): 
        global expression 
        self.expression = "" 
        self.equation.set("")
    def btn_clear1(self):
        self.expression = self.expression[:-1]
        self.equation.set(self.expression)
    def equalClick(self):
        try:
            self.sum_up = str(eval(self.expression))
            self.equation.set(self.sum_up)
            self.expression = self.sum_up
        except:
            self.equation.set("Invalid Input")
            self.expression = ""
    def __init__(self,parent):
        self.parent = parent
        self.expression = " "
        self.sum_up = ""
        self.frame = tkinter.Frame(parent)
        self.frame.pack()
        self.equation = tkinter.StringVar()
        self.equation.set("0")
        self.label = tkinter.Label(self.frame,textvariable = self.equation,font = "calibri 25",height = 3,bg = 'silver')
        self.label.pack()
        self.frame1 = tkinter.Frame(self.parent)
        self.frame1.pack()
        self.button = tkinter.Button(self.frame1,text = '9',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click(9))
        self.button.grid(row = 1,column = 0)
        self.button = tkinter.Button(self.frame1,text = '8',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click(8))
        self.button.grid(row = 1,column = 1)
        self.button = tkinter.Button(self.frame1,text = '7',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click(7))
        self.button.grid(row = 1,column = 2)
        self.button = tkinter.Button(self.frame1,text = '*',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click("*"))
        self.button.grid(row = 1,column = 3)
        self.button = tkinter.Button(self.frame1,text = '4',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click(4))
        self.button.grid(row = 2,column = 0)
        self.button = tkinter.Button(self.frame1,text = '5',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click(5))
        self.button.grid(row = 2,column = 1)
        self.button = tkinter.Button(self.frame1,text = '6',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click(6))
        self.button.grid(row = 2,column = 2)
        self.button = tkinter.Button(self.frame1,text = '/',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click("/"))
        self.button.grid(row = 2,column = 3)
        self.button = tkinter.Button(self.frame1,text = '1',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click(1))
        self.button.grid(row = 3,column = 0)
        self.button = tkinter.Button(self.frame1,text = '2',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click(2))
        self.button.grid(row = 3,column = 1)
        self.button = tkinter.Button(self.frame1,text = '3',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click(3))
        self.button.grid(row = 3,column = 2)
        self.button = tkinter.Button(self.frame1,text = '+',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click("+"))
        self.button.grid(row = 3,column = 3)
        self.button = tkinter.Button(self.frame1,text = '0',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click(0))
        self.button.grid(row = 4,column = 0)
        self.button = tkinter.Button(self.frame1,text = '.',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click("."))
        self.button.grid(row = 4,column = 1)
        self.button = tkinter.Button(self.frame1,text = '-',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click("-"))
        self.button.grid(row = 4,column = 2)
        self.button = tkinter.Button(self.frame1,text = 'ln',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click("ln("))
        self.button.grid(row = 4,column = 3)
        self.button = tkinter.Button(self.frame1,text = '%',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click("%"))
        self.button.grid(row = 5,column = 0)
        self.button = tkinter.Button(self.frame1,text = 'exp',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click("exp("))
        self.button.grid(row = 5,column = 1)
        self.button = tkinter.Button(self.frame1,text = 'sqrt',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click("sqrt("))
        self.button.grid(row = 5,column = 2)
        self.button = tkinter.Button(self.frame1,text = 'clear',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = self.clear)
        self.button.grid(row = 8,column = 0)
        self.button = tkinter.Button(self.frame1,text = 'sin',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click("sin("))
        self.button.grid(row = 6,column = 0)
        self.button = tkinter.Button(self.frame1,text = 'cos',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click("cos("))
        self.button.grid(row = 6,column = 1)
        self.button = tkinter.Button(self.frame1,text = 'tan',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click("tan("))
        self.button.grid(row = 6,column = 2)
        self.button = tkinter.Button(self.frame1,text = 'quit',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = self.exit1)
        self.button.grid(row = 8,column = 1)
        self.button = tkinter.Button(self.frame1,text = '(',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click("("))
        self.button.grid(row = 5,column = 3)
        self.button = tkinter.Button(self.frame1,text = ')',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda: self.click(")"))
        self.button.grid(row = 6,column = 3)
        self.button = tkinter.Button(self.frame1,text = '=',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = self.equalClick)
        self.button.grid(row = 8,column = 2)
        self.button = tkinter.Button(self.frame1,text = 'del',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = self.btn_clear1)
        self.button.grid(row = 8,column = 3)
        self.button = tkinter.Button(self.frame1,text = 'sqr',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda:self.click("sqr("))
        self.button.grid(row = 7,column = 0)
        self.button = tkinter.Button(self.frame1,text = ',',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda:self.click(","))
        self.button.grid(row = 7,column = 1)
        self.button = tkinter.Button(self.frame1,text = 'cube',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda:self.click("cube("))
        self.button.grid(row = 7,column = 2)
        self.button = tkinter.Button(self.frame1,text = 'log',font = "calibri 14",height = 2,width = 8,bg="black",fg="white",command = lambda:self.click("ln1("))
        self.button.grid(row = 7,column = 3)
if __name__ == '__main__':
    window = tkinter.Tk()
    myapp = CalculatorUsingGUI(window)
    window.title('Scientific Calculator')
    window.geometry("359x630")
    window.mainloop()

