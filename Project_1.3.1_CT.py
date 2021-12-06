#import turtle, sound, and tkinter libraries
import turtle as t 
import tkinter as tk
from playsound import playsound

#variables
width = 288
height = 512
timer = 30

#create window and turtles
wn = t.Screen()
wn.screensize(width, height)
wn.setup(width, height)
wn.bgpic("pokebackground.gif")
wn.addshape("pikachu.gif")
wn.addshape("ash ketchup.gif")
player = t.Turtle()
pokeball = t.Turtle()
pikachu = t.Turtle()
player.shape("ash ketchup.gif")
player.penup()
player.setposition(0, -120)

wn.mainloop()
