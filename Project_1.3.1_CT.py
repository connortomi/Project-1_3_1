#import statements 
import turtle as t
import tkinter as tk
from playsound import playsound

#initialize turtle for player and the pokeball
thrown_pokeball = t.Turtle()
player = t.Turtle()
player.penup()

#assign variable values and set font for timer and score
score = 0
timer = 20
timer_up = False
counter_interval = 1000
width = 288
height = 512

#create window and turtles
wn = t.Screen()
wn.screensize(width, height)
wn.setup(width, height)
wn.bgpic("pokebackground.gif")
wn.addshape("pikachu.gif")
wn.addshape("ash ketchup.gif")
player.shape("ash ketchup.gif")
player.penup()
player.speed(0)
player.goto(0, -120)
player.speed(5)

#leaderboard setup 
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name: ")
wn.listen()

#add pokemon as shapes 
pokemon = ["bulbasaur.gif", "pikachu.gif", "charizard.gif", "squirtle.gif", "mew.gif", "gengar.gif", "gyrados.gif", "snorlax.gif", "eevee.gif"]
for i in range(len(pokemon)):
	wn.addshape(pokemon.pop())

"""
#initialize pokemon turtles 
bulbasaur = t.Turtle()
bulbasaur.shape("bulbasaur.gif")
pikachu = t.Turtle()
pikachu.shape("pikachu.gif")
charizard = t.Turtle()
charizard.shape("charizard.gif")
squirtle = t.Turtle()
squirtle.shape("squirtle.gif")
mew = t.Turtle()
mew.shape("mew.gif")
gengar = t.Turtle()
gengar.shape("gengar.gif")
gyrados = t.Turtle()
gyrados.shape("gyrados.gif")
snorlax = t.Turtle()
snorlax.shape("snorlax.gif")
eevee = t.Turtle()
eevee.shape("eevee.gif")
"""

#initialize turtles (for score, timer, and game start), hide and set speed 
score_drawer = t.Turtle()
score_drawer.hideturtle()
score_drawer.speed(0)
score_drawer.penup()
score_drawer.goto(0, 0)
timer_drawer = t.Turtle()
timer_drawer.hideturtle()
timer_drawer.speed(0)
timer_drawer.penup()
timer_drawer.goto(0, 0)
game_starting_button = t.Turtle()
game_starting_button.penup()
game_starting_button.hideturtle()
game_starting_button.speed(0)

#add pokeball images as shapes
pokeballs = ["pokeball.gif", "pokeball2.gif", "pokeball3.gif", "pokeball4.gif"]
for i in range(len(pokeballs)):
  wn.addshape(pokeballs.pop())
y = int(input("Choose a number 1-4 for Pokeball choice: "))
if y < 1 or y > 4:
  print("Invalid input! Please try again!")

#movement functions for player (def as function so conditional values are easier)
def right():
  player.speed(0)
  player.forward(10)
  player.speed(5)

def left():
  player.speed(0)
  player.backward(10)
  player.speed(5)

def player_movement():
  wn.onkeypress(right, "d")
  wn.onkeypress(left, "a")

player_movement() == True

wn.mainloop()