from turtle import Turtle


class Wall (Turtle):
  def __init__(self, starting_x, starting_y, x_size, y_size):
    Turtle.__init__(self)
    self.starting_x = starting_x
    self.starting_y = starting_y
    self.x_size = x_size
    self.y_size = y_size

    self.color("black")
    self.penup()
    self.shape("square")
    self.shapesize(self.y_size, self.x_size)
    self.goto(self.starting_x, self.starting_y)

  def method_example(self):
    pass
