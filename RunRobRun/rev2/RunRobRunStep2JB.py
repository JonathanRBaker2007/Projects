#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

def turn_right():
  robot.speed(0)
  robot.rt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
# other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample for loop:
'''
for step in range(3): # forward 3
  move()
'''
while True:
    for i in range(3):
        if i==0:
            print("1")
            robot.color('darkorchid')
            robot.goto(startx,starty)
            wn.bgpic("maze1.png")
            for step in range(4):
                robot.fd(3)
                move()

            for step in range(1):
                turn_right()

            for step in range(4):
                robot.fd(3)
                move()


        if i==1:
            print("2")
            robot.goto(startx,starty)
            turn_left()
            wn.bgpic("maze2.png")
            for step in range(3):
                robot.fd(3)
                move()

            for step in range(1):
                turn_right()

            for step in range(2):
                robot.fd(3)
                move()

            
        if i==2:
            print("3")
            robot.goto(startx,starty)
            turn_left()
            wn.bgpic("maze3.png")
            for i in range(2):
                for step in range(2):
                    robot.fd(3)
                    move()
                    turn_right()
                    robot.fd(3)
                    move()
                    turn_left()
                robot.color('red')
        

#---- end robot movement 

wn.mainloop()
