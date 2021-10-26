from turtle import Turtle


class TextTurtle (Turtle):    
  def __init__(self, starting_x=0, starting_y=0):        
    Turtle.__init__(self)        
    self.starting_x = starting_x        
    self.starting_y = starting_y                
    
    # General setup        
    self.color("green")        
    self.penup()
    self.hideturtle()        
    # self.shape("turtle")        
    # self.goto(self.starting_x, self.starting_y)            
  def write_text(self, text, x, y):        
    self.goto(x,y)
    self.write(text, move=False, align='center', font=('Arial', 14, 'bold'))