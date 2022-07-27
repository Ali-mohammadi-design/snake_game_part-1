class Geometry():
  
  def square(self,move,iteration):
    from turtle import Turtle,Screen
    timmy=Turtle()
    screen=Screen()
    timmy.shape("turtle")
    timmy.color("red")
    for n in range(iteration):
      timmy.forward(100)
      timmy.right(90)
      timmy.forward(100)
      timmy.right(90)
      timmy.forward(100)
      timmy.right(90)
      timmy.forward(100)
      timmy.forward(move)

    screen.exitonclick()
    
