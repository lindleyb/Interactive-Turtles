from turtle import Turtle

class KeyboardTurtle(Turtle):
  # our 'wrapper' class of the Turtle class
  def __init__(self, 
               window,  
               straight = "Up", 
               turn_right = "Right", 
               turn_left = "Left",
               backward = "Down",
               other_player = None):
    # Runs Keyboard Turtle Constructor as well as the Turtle Constructor
    Turtle.__init__(self)
    
    # Sets up incoming variables
    self.window = window
    self.straight = straight
    self.turn_right = turn_right
    self.turn_left = turn_left
    self.backward = backward
    self.other_player = other_player

    #set turtle starting states
    self.shape("turtle")
    self.color("green")
    self.penup()

    # Sets up keyboard command examples
    self.window.onkey(self.go_right, self.turn_right)
    self.window.onkey(self.go_forward, self.straight)
    self.window.onkey(self.go_left, self.turn_left)
    self.window.onkey(self.go_backward, self.backward)

    #sets up controlling variables (y not implemented)
    self.movement_speed = 5
    self.turn_speed = 45
    self.collision_distance = 20

  # Movement Methods
  def go_forward(self):
    self.forward(self.movement_speed)
    if self.check_collision(self.other_player):
      print("crash")
      quit()
      
  def go_right(self):
    self.right(self.turn_speed)
  
  def go_left(self):
    self.left(self.turn_speed)

  def go_backward(self):
    self.backward(self.movement_speed)


  # Useful Methods

  # This checks if object collides with another object.  
  # Right now it checks against the other player, but 
  # it doesn't NEED to.  It can check against any
  # other turtle object

  def check_collision(self, obj_to_check):
    distance_x = obj_to_check.xcor() - self.xcor()
    distance_x = abs(distance_x)

    distance_y = obj_to_check.ycor() - self.ycor()
    distance_y = abs(distance_y)

    if distance_x < self.collision_distance and distance_y < self.collision_distance:
      return True
    else:
      return False


    # TODO: finish setting up the inputs (left and down)
    
