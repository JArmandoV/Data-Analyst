import turtle
from turtle import *
from turtle import Screen
from freegames import vector
    
def emptySquare():
    pass  # TODO
    
def filledSquare():
  pass  # TODO
  
while True:
    screen = Screen()
    answer = screen.textinput("Next Game","1 - Square:")
    if (answer is None):
        break
    elif (answer == '1'):
        emptySquare()
    elif (answer == '2'):
        filledSquare()
 
