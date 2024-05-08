import turtle as t
import random as r
import time 


delay=0.1
bodyParts=[]
bodyParts1=[]
score=0
fontSetup=("Times New Roman",20,"normal")
hscore=0

wn=t.Screen()
wn.setup(width=600,height=600)
wn.bgcolor('green')

head = t.Turtle(shape='square')
head.speed(1)
head.penup()
head.goto(-50,0)
head.direction='stop'

head1 = t.Turtle(shape='square')
head1.speed(1)
head1.penup()
head1.goto(50,0)
head1.direction='stop'

food=t.Turtle(shape='circle')
food.speed(1)
food.penup()
food.teleport(100,100)
food.color('red')

def up():
    if head.direction!="down":
        head.direction="up"  
def down():
    if head.direction!="up":
        head.direction="down"
def left():
    if head.direction!="right":
        head.direction="left"
def right():
    if head.direction!="left":
        head.direction="right"

def move():
    if head.direction=="up":
        head.sety(head.ycor()+20)
    if head.direction=="down":
        head.sety(head.ycor()-20)
    if head.direction=="left":
        head.setx(head.xcor()-20)
    if head.direction=="right":
        head.setx(head.xcor()+20)
    
def moveBodyParts():
    for i in range(len(bodyParts)-1,0,-1):
        newX=bodyParts[i-1].xcor()
        newY=bodyParts[i-1].ycor()
        bodyParts[i].goto(newX,newY)

    if len(bodyParts)>0:
        newX=head.xcor()
        newY=head.ycor()
        bodyParts[0].goto(newX,newY)
        
def up1():
    if head1.direction!="down":
        head1.direction="up"  
def down1():
    if head1.direction!="up":
        head1.direction="down"
def left1():
    if head1.direction!="right":
        head1.direction="left"
def right1():
    if head1.direction!="left":
        head1.direction="right"

def move1():
    if head1.direction=="up":
        head1.sety(head1.ycor()+20)
    if head1.direction=="down":
        head1.sety(head1.ycor()-20)
    if head1.direction=="left":
        head1.setx(head1.xcor()-20)
    if head1.direction=="right":
        head1.setx(head1.xcor()+20)
    
def moveBodyParts1():
    for i in range(len(bodyParts1)-1,0,-1):
        newX=bodyParts1[i-1].xcor()
        newY=bodyParts1[i-1].ycor()
        bodyParts1[i].goto(newX,newY)

    if len(bodyParts1)>0:
        newX=head1.xcor()
        newY=head1.ycor()
        bodyParts1[0].goto(newX,newY)



wn.onkeypress(up,"w")
wn.onkeypress(down,"s")
wn.onkeypress(left,"a")
wn.onkeypress(right,"d")
wn.onkeypress(up1,"Up")
wn.onkeypress(down1,"Down")
wn.onkeypress(left1,"Left")
wn.onkeypress(right1,"Right")
wn.listen()

while True:
    wn.update()
    #TODO: Check for wall collision
        #up                 #down               #left               #right
    if head.ycor()>290 or head.ycor()<-290 or head.xcor()<-290 or head.xcor()>290:
        head.color('red')
        for i in range(len(bodyParts)):
            bodyParts[i].hideturtle()
        bodyParts=[]
        head.goto(-50,0)
        head.color('black')
        head.direction = "stop"
        
    if head1.ycor()>290 or head1.ycor()<-290 or head1.xcor()<-290 or head1.xcor()>290:
        head1.color('red')
        for i in range(len(bodyParts1)):
            bodyParts1[i].hideturtle()
        bodyParts1=[]
        head1.goto(50,0)
        head1.color('black')
        head1.direction = "stop"
        
    #TODO: Check for food collision
    if head.distance(food) < 20:
        score+=100
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
        
    if head1.distance(food) < 20:
        score+=100
        # Move the food to a random spot
        x = r.randint(-290, 290)
        y = r.randint(-290, 290)
        food.teleport(x,y)
        bodyPart = t.Turtle(shape="square")
        bodyPart.speed(0)
        bodyPart.penup()
        bodyPart.color('black')
        bodyPart.fillcolor('gray')
        bodyParts1.append(bodyPart)
        
        
    #TODO: Move the body parts
    moveBodyParts()
    moveBodyParts1()
    #TODO: Move the head forward
    move()
    move1()
    #TODO: Check for body collision
    for eachBodyPart in bodyParts:
        if head.distance(eachBodyPart)<10:
            for i in range(len(bodyParts)):
                bodyParts[i].hideturtle()
            bodyParts=[]
            head.goto(-50,0)
            head.color('black')
            head.direction = "stop"

    for eachBodyPart in bodyParts1:
        if head.distance(eachBodyPart)<10:
            for i in range(len(bodyParts)):
                bodyParts[i].hideturtle()
            bodyParts=[]
            head.goto(-50,0)
            head.color('black')
            head.direction = "stop"

    for eachBodyPart in bodyParts:
        if head1.distance(eachBodyPart)<10:
            for i in range(len(bodyParts1)):
                bodyParts1[i].hideturtle()
            bodyParts1=[]
            head1.goto(-50,0)
            head1.color('black')
            head1.direction = "stop"
    
    for eachBodyPart in bodyParts1:
        if head1.distance(eachBodyPart)<10:
            for i in range(len(bodyParts1)):
                bodyParts1[i].hideturtle()
            bodyParts1=[]
            head1.goto(50,0)
            head1.color('black')
            head1.direction = "stop"

    if head1.distance(head)<20 or head.distance(head1)<20:
        for i in range(len(bodyParts1)):
            bodyParts1[i].hideturtle()
        bodyParts1=[]
        head1.goto(50,0)
        head1.color('black')
        head1.direction = "stop"
        for i in range(len(bodyParts)):
            bodyParts[i].hideturtle()
        bodyParts=[]
        head.goto(-50,0)
        head.color('black')
        head.direction = "stop"


    time.sleep(delay)

    
