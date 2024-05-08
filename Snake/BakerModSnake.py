import turtle as t
import random as r
import time 
import winsound

delay=0.1
bodyParts=[]
score=0
fontSetup=("Times New Roman",10,"normal")
hscore=0
pause=""

wn=t.Screen()
wn.setup(width=600,height=600)
wn.bgcolor('green')
wn.title("Modded Snake")

head = t.Turtle(shape='square')
head.speed(1)
head.penup()
head.direction='stop'

food=t.Turtle(shape='circle')
food.speed(1)
food.penup()
food.teleport(100,100)
food.color('red')

dirTurtle=t.Turtle()
dirTurtle.speed(-10)
dirTurtle.penup()
dirTurtle.goto(-300,-300)
dirTurtle.pendown()

def up():
    if head.direction!="down"and pause!="true":
        head.direction="up"  
def down():
    if head.direction!="up"and pause!="true":
        head.direction="down"
def left():
    if head.direction!="right"and pause!="true":
        head.direction="left"
def right():
    if head.direction!="left"and pause!="true":
        head.direction="right"

def move():
    if head.direction=="up" and pause!="true":
        head.sety(head.ycor()+20)
        head.color(r.random(),
                r.random(),
                r.random())
    if head.direction=="down" and pause!="true":
        head.sety(head.ycor()-20)
        head.color(r.random(),
                r.random(),
                r.random())
    if head.direction=="left"and pause!="true":
        head.setx(head.xcor()-20)
        head.color(r.random(),
                r.random(),
                r.random())
    if head.direction=="right"and pause!="true":
        head.setx(head.xcor()+20)
        head.color(r.random(),
                r.random(),
                r.random())
    
def moveBodyParts():
     if pause!="true":
        for i in range(len(bodyParts)-1,0,-1):
                newX=bodyParts[i-1].xcor()
                newY=bodyParts[i-1].ycor()
                bodyParts[i].goto(newX,newY)

        if len(bodyParts)>0 and pause!="true":
            newX=head.xcor()
            newY=head.ycor()
            bodyParts[0].goto(newX,newY)
        
position=""
def pauseIt():
    global pause
    global position
    position=head.direction
    head.direction="stop"
    pause="true"
    dirTurtle.penup()
    dirTurtle.goto(-50,100)
    dirTurtle.pendown()
    dirTurtle.write("Press anywhere to continue...",font=fontSetup)
    
def unpause(x,y):
    global pause
    global position
    head.direction=position
    dirTurtle.clear()
    dirTurtle.penup()
    dirTurtle.goto(-300,-300)
    dirTurtle.pendown()
    dirTurtle.write(directions,font=fontSetup)
    pause=""

wn.onkeypress(up,"w")
wn.onkeypress(down,"s")
wn.onkeypress(left,"a")
wn.onkeypress(right,"d")
wn.onkeypress(pauseIt,"p")
wn.onclick(unpause)
wn.listen()

directions='''

    w---Up
    s---Down
    a---Left
    d---Right
    p---Pause

'''
print(directions)
dirTurtle.write(directions,font=fontSetup)
if pause !="true":
    while True:
        wn.update()
        #TODO: Check for wall collision
            #up                 #down               #left               #right
        if head.ycor()>290 or head.ycor()<-290 or head.xcor()<-290 or head.xcor()>290:
            winsound.PlaySound("blip.wav",winsound.SND_FILENAME)
            head.color('red')
            for i in range(len(bodyParts)):
                bodyParts[i].hideturtle()
            bodyParts=[]
            time.sleep(1)
            head.goto(0,0)
            head.color('black')
            head.direction = "stop"
            
        #TODO: Check for food collision
        if head.distance(food) < 20:
            winsound.PlaySound("blip.wav",winsound.SND_FILENAME)
            delay-=.01
            head.color(r.random(),
                        r.random(),
                        r.random())
            # Move the food to a random spot
            x = r.randint(-290, 290)
            y = r.randint(-290, 290)
            food.teleport(x,y)
            bodyPart = t.Turtle(shape="square")
            bodyPart.speed(0)
            bodyPart.penup()
            bodyPart.color('black')
            bodyPart.fillcolor('gray')
            bodyParts.append(bodyPart)
        #TODO: Move the body parts
        moveBodyParts()
        #TODO: Move the head forward
        move()
        
        if delay<=0:
            head.speed(0)
            delay=.1
            
        #TODO: Check for body collision
        for eachBodyPart in bodyParts:
            if head.distance(eachBodyPart)<10:
                    winsound.PlaySound("blip.wav",winsound.SND_FILENAME)
                    head.color('red')
                    for i in range(len(bodyParts)):
                        bodyParts[i].hideturtle()
                    bodyParts=[]
                    time.sleep(1)
                    head.goto(0,0)
                    head.color('black')
                    head.direction = "stop"
        time.sleep(delay)