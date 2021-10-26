from turtle import Turtle, Screen

class ClickableTurtle(Turtle):
  # our 'wrapper' class of the Turtle class
  def __init__(self, 
               name = "button", 
               x = 0 , 
               y = -100):
    # Runs Keyboard Turtle Constructor as well as the Turtle Constructor
    Turtle.__init__(self)
    
    # Sets up incoming variables
    self.name = name
    self.x = x
    self.y = y
    self.window = Screen()

    #set turtle starting states
    self.shape("square")
    self.shapesize(1,3,1)
    self.color("tan")
    self.penup()
    self.setx(self.x)
    self.sety(self.y)
    self.draw_title(self.name, self.x, self.y)
    self.window.onscreenclick(None)
    self.onclick(self.click)

  # Draws the button name above the button
  def draw_title(self, text, x, y):
    self.goto(self.x, self.y + 17)
    self.write(text, move=False, align='center', font=('Arial', 10, 'normal'))
    self.goto(self.x, self.y)
  


  # tells what happens when button is clicked
  def click(self, x, y):
    # This is Placeholder:  What should this button do?
    print ("Click")
    player_4.forward()
    
    

  # TODO:  
  # 1) Change the button color 
  # 2) make the click method do something else
