from turtle import Screen, ontimer
from keyboardturtle import KeyboardTurtle
from clickableturtle import ClickableTurtle
from movingturtle import MovingTurtle
from wall import Wall
from textturtle import TextTurtle

def moving_objects():
  for object in moving_list:
    object.move_self()
  ontimer(moving_objects, 1)


moving_list = []

text = TextTurtle()
text.write_text("DON'T RUN INTO THE WALLS", -140, 110)
# set up instance of the screen
window = Screen()
screen_width = 600
screen_height = 400
window.setup(screen_width, screen_height)

#list setup
wall_list = []

# set up clickable instance
button = ClickableTurtle()

#set up players
player_1 = KeyboardTurtle(window, walls = wall_list)
player_2 = KeyboardTurtle(window, "w", "d", "a", "s", walls = wall_list)
player_3 = KeyboardTurtle(window, "8", "6", "4", "2", walls = wall_list)
player_4 = ClickableTurtle(window)

w1 = Wall(100,0, 1,5)
w2 = Wall(-100,0,1,5)
wall_list.append(w1)

wall_list.append(Wall(0,100,5,1))


player_1.goto(120,0)
player_3.goto(120,50)

# set target of other player(our collison check) to the opposite player
player_1.other_player = player_2
player_2.other_player = player_1
player_3.other_player = player_4
player_4.other_player = player_3

moveT = MovingTurtle(screen_width)
moving_list.append(moveT)

moving_list.append(MovingTurtle(screen_width))



# This is needed to listen for inputs
window.listen()
window.mainloop()
moving_objects()

# be CAREFUL. We aren't controlling the screen draws in this program, so NO while True loops

#TODO:  Check the classes and complete TODOs
#push to github repo.
#link repo to assignment