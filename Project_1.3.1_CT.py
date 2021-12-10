#import statements 
import turtle as t
import tkinter as tk
import leaderboard as lb
from playsound import _playsoundWin, playsound

#assign variable values and set font for timer and score
score = 0
timer = 5
timer_up = False
counter_interval = 1000
width = 288
height = 512

#create window and set background
wn = t.Screen()
wn.screensize(width, height)
wn.setup(width, height)
wn.bgpic("pokebackground.gif")

#add pokeball images as shapes
pokeballs = ["pokeball.gif", "pokeball2.gif", "pokeball3.gif", "pokeball4.gif"]
for i in range(len(pokeballs)):
  wn.addshape(pokeballs.pop())

#initialize turtle for player and the pokeball
thrown_pokeball = t.Turtle()
thrown_pokeball.hideturtle()
thrown_pokeball.shape("pokeball.gif")
thrown_pokeball.turtlesize(30)
thrown_pokeball.penup()
player = t.Turtle()
player.penup()
wn.addshape("ash ketchup.gif")
player.shape("ash ketchup.gif")
player.penup()
player.speed(0)
player.goto(0, -120)
player.speed(5)

#leaderboard setup 
leaderboard_file_name = "leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name: ")
wn.listen()

#add pokemon as shapes 
pokemon = ["bulbasaur.gif", "pikachu.gif", "charizard.gif", "squirtle.gif", "mew.gif", "gengar.gif", "gyrados.gif", "snorlax.gif", "eevee.gif", "jigglypuff.gif"]
for i in range(len(pokemon)):
	wn.addshape(pokemon.pop())
"""
y = int(input("Choose a number 1-4 for Pokeball choice: "))
if y < 1 or y > 4:
  print("Invalid input! Please try again!")
else:
  """

#initialize pokemon turtles 
bulbasaur = t.Turtle()
bulbasaur.penup()
bulbasaur.shape("bulbasaur.gif")
bulbasaur.goto(-90, 170)
pikachu = t.Turtle()
pikachu.penup()
pikachu.goto(-30, 170)
pikachu.shape("pikachu.gif")
charizard = t.Turtle()
charizard.penup()
charizard.goto(30, 170)
charizard.shape("charizard.gif")
squirtle = t.Turtle()
squirtle.penup()
squirtle.goto(-60, 140)
squirtle.shape("squirtle.gif")
mew = t.Turtle()
mew.penup()
mew.goto(0, 140)
mew.shape("mew.gif")
gengar = t.Turtle()
gengar.penup()
gengar.goto(60, 140)
gengar.shape("gengar.gif")
gyrados = t.Turtle()
gyrados.penup()
gyrados.goto(90, 170)
gyrados.shape("gyrados.gif")
snorlax = t.Turtle()
snorlax.penup()
snorlax.goto(-5, 210)
snorlax.shape("snorlax.gif")
eevee = t.Turtle()
eevee.penup()
eevee.goto(35, 115)
eevee.shape("eevee.gif")
jigglypuff = t.Turtle()
jigglypuff.penup()
jigglypuff.goto(-30, 110)
jigglypuff.shape("jigglypuff.gif")

#initialize turtles (for score, timer, and game start), hide and set speed 
score_drawer = t.Turtle()
score_drawer.hideturtle()
score_drawer.speed(0)
score_drawer.penup()
score_drawer.goto(-130, 220)
timer_drawer = t.Turtle()
timer_drawer.hideturtle()
timer_drawer.speed(0)
timer_drawer.penup()
timer_drawer.goto(45, 220)
game_starter_button = t.Turtle()
game_starter_button.penup()
game_starter_button.hideturtle()
game_starter_button.speed(0)

#movement functions for player (def as function so conditional values are easier)
def update_score():
  score_drawer.clear()
  global score 
  score = score + 1
  score_drawer.write(score, font=2)

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

def throw_pokeball():
  playsound("throw_sound.mp3", False)
  thrown_pokeball.setposition(player.xcor(), player.ycor())
  thrown_pokeball.speed(0)
  thrown_pokeball.showturtle()
  thrown_pokeball.left(90)
  thrown_pokeball.speed(8)
  thrown_pokeball.forward(350)
  thrown_pokeball.speed(0)
  thrown_pokeball.right(90)
  thrown_pokeball.hideturtle()
  thrown_pokeball.setposition(player.xcor(), player.ycor())

def bulbasaur_hit():
  bulbasaur.hideturtle
  bulbasaur.speed(0)
  bulbasaur.goto(-11100, 3000)
  update_score()

def throw():
  wn.onkeypress(throw_pokeball, "space")

def game_functions():
      global timer
      if timer > 0:
        player_movement()==True
        throw()==True
      else:
        throw()==False
        throw_pokeball()==False
        player_movement()==False
        player.hideturtle()

def countdown():
  global timer, timer_up
  timer_drawer.clear()
  if timer <= 0:
    timer_drawer.write("Time's Up", font=2)
    timer_up = True
    manage_leaderboard()
  else:
    timer_drawer.write("Timer: " + str(timer), font=2)
    timer = timer-1
    timer_drawer.getscreen().ontimer(countdown, counter_interval)

#leaderboard function
def manage_leaderboard():
  global leader_scores_list
  global leader_names_list
  global score
  global player

  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, player, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, player, score)

#setup the button to start the game
#prompt the user to click the button to start the game
game_starter_button.goto(-120,50)
game_starter_button.write("Press here to start", font=2)
game_starter_button.goto(70, 50)
game_starter_button.showturtle()
game_starter_button.color("red")
game_starter_button.shape("circle")

def game_start(x,y):
    wn.ontimer(countdown, counter_interval)
    game_starter_button.onclick(game_functions()==True)
    game_starter_button.clear()
    game_starter_button.hideturtle()

game_starter_button.onclick(game_start)

wn.mainloop()
