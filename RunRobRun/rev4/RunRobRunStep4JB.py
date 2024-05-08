#   a115_robot_maze.py
from pickletools import pybool
import turtle as trtl

welcome='''

        Welcome to my Maze!

             Commands
        -------------------
        w - up
        a - left
        s - down
        d - right

'''
print(welcome)

#----- maze and turtle config variables
screen_h = 600
screen_w = 600
startx = -265
starty = -265
turtle_scale = 1.5
interval=1000
fontSetup=("Times New Roman",20,"normal")
goodBounds=[]
badBounds=[]
#I forgot everything you said and I have no idea where to start
#I know you said something about lists





#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)

wn.addshape("pickle.gif")
#I tried multiple different files and i still could not get the assets/image.gif to actually work. It kept completely ignoring the assets part. I had it in every file

#----- init robot
robot = trtl.Turtle(shape="pickle.gif")
robot.hideturtle()
robot.color("green")
robot.pencolor("green")
robot.penup()
robot.setheading(0)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()
robot.direction="stop"

#---- TODO: change maze here
wn.bgpic("jbmaze.png")# other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
def up():
        robot.direction="up" 
def down():
        robot.direction="down"
def left():
        robot.direction="left"
def right():
        robot.direction="right"

def move():
    if robot.direction=="up":
        robot.sety(robot.ycor()+65)
        robot.direction="stop"
    elif robot.direction=="down":
        robot.sety(robot.ycor()-65)
        robot.direction="stop"
    elif robot.direction=="left":
        robot.setx(robot.xcor()-65)
        robot.direction="stop"
    elif robot.direction=="right":
        robot.setx(robot.xcor()+65)
        robot.direction="stop"



def win():
    if robot.xcor() >= 240 and robot.ycor() >= 300:
        wn.clear()
        robot.goto(0,0)
        robot.write("game over", font=fontSetup)


wn.onkeyrelease(up,"w")
wn.onkeyrelease(down,"s")
wn.onkeyrelease(left,"a")
wn.onkeyrelease(right,"d")
wn.listen()

        

#---- end robot movement 

while True:
    wn.update()
    move()
    win()
    
    
