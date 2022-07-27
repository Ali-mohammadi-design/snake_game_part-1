from turtle import Screen, Turtle
import time
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
#screen.tracer(0) turns of the automatic update of the screen
x=0
timy_list=[]
position=[]
for t in range(3):
  timy=Turtle()
  timy.penup()
  timy_list.append(timy)
  timy.shape("square")
  timy.color("white")
  timy.goto(x,0)
  x=x-20
  print(timy.position())
  position.append(timy.position())
screen.update()
#screen.update() would update the screen right away
#time.sleep(x) would create a delay for the program for x seceonds 
repeat=True
v=1
position1=[0,0,0]
while repeat:
  position1[0]=timy_list[0].position()
  timy_list[0].forward(20)
  timy_list[0].left(90)
  screen.listen()
  
  for a in range(1,3):
   position1[a]=timy_list[a].position()
   timy_list[a].goto(position1[a-1])
   print(timy_list[a].position())
    
  time.sleep(1)
  screen.update()
  

  
  
  
screen.exitonclick()