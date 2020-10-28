import turtle
from turtle import *
from turtle import Screen
from freegames import vector
    
def filledCircle():
    t = turtle.Turtle()
    t.fillcolor('red')  # set the fillcolor
    t.begin_fill()  # start the filling color 
    t.circle(100)
    t.end_fill()

    
def emptyCircle():
    t=turtle.Turtle()
    t.circle(100)
  
    while True:
        screen = Screen()
        answer = screen.textinput("Next Game","1 - Square:")
        if (answer is None):
            break
        elif (answer == '1'):
            filledCircle()
        elif (answer == '2'):
            emptyCircle()
 