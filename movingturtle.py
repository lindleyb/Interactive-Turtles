from turtle import Turtle


class MovingTurtle(Turtle):
  def __init__(self, width):
    Turtle.__init__(self)
    self.width = width

    #initial setup
    self.shape("circle")
    self.shapesize(.5, .5, 1)
    self.penup()
    

    #variables
    self.x_spd = 4

  def move_self(self):
    self.forward(self.x_spd)
    if self.at_edge():
      self.x_spd = -self.x_spd
    

  def at_edge(self):
    if self.xcor() >= self.width/2 or self.xcor() <= -self.width/2:
      return True
    else:
      return False