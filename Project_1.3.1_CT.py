#import module statements 
import turtle as t
import tkinter as tk
import leaderboard as lb

#assign variable values and set window dimensions
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
pokeballs = ["pokeball.gif"]
for i in range(len(pokeballs)):
  wn.addshape(pokeballs.pop())

#initialize turtle for player and basic methods
player = t.Turtle()
player.penup()
wn.addshape("ash ketchup.gif")
player.shape("ash ketchup.gif")
player.penup()
player.speed(0)
player.goto(0, -120)
player.speed(5)

#initialize turtle for pokeball
thrown_pokeball = t.Turtle()
thrown_pokeball.hideturtle()
thrown_pokeball.shape("pokeball.gif")
thrown_pokeball.penup()

#leaderboard setup and user input
leaderboard_file_name = "leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name: ")
wn.listen()

#add pokemon as shapes 
pokemon = ["bulbasaur.gif", "pikachu.gif", "charizard.gif", "squirtle.gif", "mew.gif", "gengar.gif", "gyrados.gif", "snorlax.gif", "eevee.gif", "jigglypuff.gif"]
for i in range(len(pokemon)):
	wn.addshape(pokemon.pop())

#initialize turtle and methods for pokemon 1
bulbasaur = t.Turtle()
bulbasaur.hideturtle()
bulbasaur.penup()
bulbasaur.shape("bulbasaur.gif")
bulbasaur.goto(-90, 170)
bulbasaur.showturtle()

#initialize turtle and methods for pokemon 2
pikachu = t.Turtle()
pikachu.hideturtle()
pikachu.penup()
pikachu.goto(-30, 170)
pikachu.shape("pikachu.gif")
pikachu.showturtle()

#initialize turtle and methods for pokemon 3
charizard = t.Turtle()
charizard.hideturtle()
charizard.penup()
charizard.goto(30, 170)
charizard.shape("charizard.gif")
charizard.showturtle()

#initialize turtle and methods for pokemon 4
squirtle = t.Turtle()
squirtle.hideturtle()
squirtle.penup()
squirtle.goto(-60, 140)
squirtle.shape("squirtle.gif")
squirtle.showturtle()

#initialize turtle and methods for pokemon 5
mew = t.Turtle()
mew.hideturtle()
mew.penup()
mew.goto(0, 140)
mew.shape("mew.gif")
mew.showturtle()

#initialize turtle and methods for pokemon 6
gengar = t.Turtle()
gengar.hideturtle()
gengar.penup()
gengar.goto(60, 140)
gengar.shape("gengar.gif")
gengar.showturtle()

#initialize turtle and methods for pokemon 7
gyrados = t.Turtle()
gyrados.hideturtle()
gyrados.penup()
gyrados.goto(90, 170)
gyrados.shape("gyrados.gif")
gyrados.showturtle()

#initialize turtle and methods for pokemon 8
snorlax = t.Turtle()
snorlax.hideturtle()
snorlax.penup()
snorlax.goto(-5, 210)
snorlax.shape("snorlax.gif")
snorlax.showturtle()

#initialize turtle and methods for pokemon 9
eevee = t.Turtle()
eevee.hideturtle()
eevee.penup()
eevee.goto(35, 115)
eevee.shape("eevee.gif")
eevee.showturtle()

#initialize turtle and methods for pokemon 10
jigglypuff = t.Turtle()
jigglypuff.hideturtle()
jigglypuff.penup()
jigglypuff.goto(-30, 110)
jigglypuff.shape("jigglypuff.gif")
jigglypuff.showturtle()

#initialize letter drawer turtle for pokemon 1
b_letter_drawer = t.Turtle()
b_letter_drawer.hideturtle()
b_letter_drawer.penup()
b_letter_drawer.goto(-95, 165)
b_letter_drawer.pendown()
b_letter_drawer.write("B", font=("Arial", 15, "bold"))

#initialize letter drawer turtle for pokemon 2
p_letter_drawer = t.Turtle()
p_letter_drawer.hideturtle()
p_letter_drawer.penup()
p_letter_drawer.goto(-35, 165)
p_letter_drawer.pendown()
p_letter_drawer.write("P", font=("Arial", 15, "bold"))

#initialize letter drawer turtle for pokemon 3
c_letter_drawer = t.Turtle()
c_letter_drawer.hideturtle()
c_letter_drawer.penup()
c_letter_drawer.goto(25, 165)
c_letter_drawer.pendown()
c_letter_drawer.write("C", font=("Arial", 15, "bold"))

#initialize letter drawer turtle for pokemon 4
s_letter_drawer = t.Turtle()
s_letter_drawer.hideturtle()
s_letter_drawer.penup()
s_letter_drawer.goto(-65, 135)
s_letter_drawer.pendown()
s_letter_drawer.write("S", font=("Arial", 15, "bold"))

#initialize letter drawer turtle for pokemon 5
m_letter_drawer = t.Turtle()
m_letter_drawer.hideturtle()
m_letter_drawer.penup()
m_letter_drawer.goto(-5, 135)
m_letter_drawer.pendown()
m_letter_drawer.write("M", font=("Arial", 15, "bold"))

#initialize letter drawer turtle for pokemon 6
g_letter_drawer = t.Turtle()
g_letter_drawer.hideturtle()
g_letter_drawer.penup()
g_letter_drawer.goto(55, 135)
g_letter_drawer.pendown()
g_letter_drawer.write("G", font=("Arial", 15, "bold"))

#initialize letter drawer turtle for pokemon 7
f_letter_drawer = t.Turtle()
f_letter_drawer.hideturtle()
f_letter_drawer.penup()
f_letter_drawer.goto(85, 165)
f_letter_drawer.pendown()
f_letter_drawer.write("F", font=("Arial", 15, "bold"))

#initialize letter drawer turtle for pokemon 8
x_letter_drawer = t.Turtle()
x_letter_drawer.hideturtle()
x_letter_drawer.penup()
x_letter_drawer.goto(-10, 195)
x_letter_drawer.pendown()
x_letter_drawer.write("X", font=("Arial", 15, "bold"))

#initialize letter drawer turtle for pokemon 9
e_letter_drawer = t.Turtle()
e_letter_drawer.hideturtle()
e_letter_drawer.penup()
e_letter_drawer.goto(30, 105)
e_letter_drawer.pendown()
e_letter_drawer.write("E", font=("Arial", 15, "bold"))

#initialize letter drawer turtle for pokemon 10
j_letter_drawer = t.Turtle()
j_letter_drawer.hideturtle()
j_letter_drawer.penup()
j_letter_drawer.goto(-35, 105)
j_letter_drawer.pendown()
j_letter_drawer.write("J", font=("Arial", 15, "bold"))

#initialize turtle for score, timer, and starting button (and setting starting positions)
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
game_starter_button.hideturtle()
game_starter_button.penup()
game_starter_button.speed(0)

#function that adds one to the score and clears the previous score (self-explanatory)
def update_score():
  score_drawer.clear()
  global score 
  score = score + 1
  score_drawer.write(score, font=2)

#movement functions that allow the player to move left and right
def right():
  player.speed(0)
  player.forward(10)
  player.speed(5)

def left():
  player.speed(0)
  player.backward(10)
  player.speed(4)

def player_movement():
  wn.onkeypress(right, "d")
  wn.onkeypress(left, "a")

#functions for whenever a letter assigned to a pokemon is pressed (ex. b for bulbasaur)
def bulbasaur_catch():
  update_score()
  player_xcor = player.xcor()
  player_ycor = player.ycor()
  b_letter_drawer.clear()
  thrown_pokeball.speed(8)
  thrown_pokeball.showturtle()
  thrown_pokeball.setposition(-90, 170)
  bulbasaur.speed(0)
  bulbasaur.hideturtle
  bulbasaur.goto(-100000, -100000)
  thrown_pokeball.hideturtle()
  thrown_pokeball.setposition(player_xcor, player_ycor)

def pikachu_catch():
  update_score()
  player_xcor = player.xcor()
  player_ycor = player.ycor()
  p_letter_drawer.clear()
  thrown_pokeball.speed(8)
  thrown_pokeball.showturtle()
  thrown_pokeball.setposition(-30, 170)
  pikachu.speed(0)
  pikachu.hideturtle
  pikachu.goto(-100000, -100000)
  thrown_pokeball.hideturtle()
  thrown_pokeball.setposition(player_xcor, player_ycor)

def charizard_catch():
  update_score()
  player_xcor = player.xcor()
  player_ycor = player.ycor()
  c_letter_drawer.clear()
  thrown_pokeball.speed(8)
  thrown_pokeball.showturtle()
  thrown_pokeball.setposition(30, 170)
  charizard.speed(0)
  charizard.hideturtle
  charizard.goto(-100000, -100000)
  thrown_pokeball.hideturtle()
  thrown_pokeball.setposition(player_xcor, player_ycor)

def squirtle_catch():
  update_score()
  player_xcor = player.xcor()
  player_ycor = player.ycor()
  s_letter_drawer.clear()
  thrown_pokeball.speed(8)
  thrown_pokeball.showturtle()
  thrown_pokeball.setposition(-60, 140)
  squirtle.speed(0)
  squirtle.hideturtle
  squirtle.goto(-100000, -100000)
  thrown_pokeball.hideturtle()
  thrown_pokeball.setposition(player_xcor, player_ycor)

def mew_catch():
  update_score()
  player_xcor = player.xcor()
  player_ycor = player.ycor()
  m_letter_drawer.clear()
  thrown_pokeball.speed(8)
  thrown_pokeball.showturtle()
  thrown_pokeball.setposition(0, 140)
  mew.speed(0)
  mew.hideturtle
  mew.goto(-100000, -100000)
  thrown_pokeball.hideturtle()
  thrown_pokeball.setposition(player_xcor, player_ycor)

def gengar_catch():
  update_score()
  player_xcor = player.xcor()
  player_ycor = player.ycor()
  g_letter_drawer.clear()
  thrown_pokeball.speed(8)
  thrown_pokeball.showturtle()
  thrown_pokeball.setposition(60, 140)
  gengar.speed(0)
  gengar.hideturtle
  gengar.goto(-100000, -100000)
  thrown_pokeball.hideturtle()
  thrown_pokeball.setposition(player_xcor, player_ycor)

def gyrados_catch():
  update_score()
  player_xcor = player.xcor()
  player_ycor = player.ycor()
  f_letter_drawer.clear()
  thrown_pokeball.speed(8)
  thrown_pokeball.showturtle()
  thrown_pokeball.setposition(90, 170)
  gyrados.speed(0)
  gyrados.hideturtle
  gyrados.goto(-100000, -100000)
  thrown_pokeball.hideturtle()
  thrown_pokeball.setposition(player_xcor, player_ycor)

def snorlax_catch():
  update_score()
  player_xcor = player.xcor()
  player_ycor = player.ycor()
  x_letter_drawer.clear()
  thrown_pokeball.speed(8)
  thrown_pokeball.showturtle()
  thrown_pokeball.setposition(-10, 205)
  snorlax.speed(0)
  snorlax.hideturtle
  snorlax.goto(-100000, -100000)
  thrown_pokeball.hideturtle()
  thrown_pokeball.setposition(player_xcor, player_ycor)

def eevee_catch():
  update_score()
  player_xcor = player.xcor()
  player_ycor = player.ycor()
  e_letter_drawer.clear()
  thrown_pokeball.speed(8)
  thrown_pokeball.showturtle()
  thrown_pokeball.setposition(35, 115)
  eevee.speed(0)
  eevee.hideturtle
  eevee.goto(-100000, -100000)
  thrown_pokeball.hideturtle()
  thrown_pokeball.setposition(player_xcor, player_ycor)

def jigglypuff_catch():
  update_score()
  player_xcor = player.xcor()
  player_ycor = player.ycor()
  j_letter_drawer.clear()
  thrown_pokeball.speed(8)
  thrown_pokeball.showturtle()
  thrown_pokeball.setposition(-30, 110)
  jigglypuff.speed(0)
  jigglypuff.hideturtle
  jigglypuff.goto(-100000, -100000)
  thrown_pokeball.hideturtle()
  thrown_pokeball.setposition(player_xcor, player_ycor)

#main game function that holds all the keypress functions and movement function
def game_functions():
  global timer
  if timer > 0:
    player_movement()==True
    wn.onkeypress(bulbasaur_catch, "b")
    wn.onkeypress(pikachu_catch, "p")
    wn.onkeypress(charizard_catch, "c")
    wn.onkeypress(squirtle_catch, "s")
    wn.onkeypress(mew_catch, "m")
    wn.onkeypress(gengar_catch, "g")
    wn.onkeypress(gyrados_catch, "f")
    wn.onkeypress(snorlax_catch, "x")
    wn.onkeypress(eevee_catch, "e")
    wn.onkeypress(jigglypuff_catch, "j")
  else:
    player_movement()==False

#function that checks if the game is done or not, either writing how much time is left
#or that the time is up
def countdown():
  global timer, timer_up
  timer_drawer.clear()
  if timer <= 0:
    player.hideturtle()
    timer_drawer.write("Time's Up", font=2)
    timer_up = True
    manage_leaderboard()
  else:
    timer_drawer.write("Timer: " + str(timer), font=2)
    timer = timer-1
    timer_drawer.getscreen().ontimer(countdown, counter_interval)

#function that draws and manages the leaderboard (and the scores+user names)
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

#function that starts the game once the button is pressed
#and calls main game functions
def game_start(x,y):
  wn.ontimer(countdown, counter_interval)
  game_starter_button.onclick(game_functions()==True)
  game_starter_button.clear()
  game_starter_button.hideturtle()

game_starter_button.onclick(game_start)

wn.mainloop()
