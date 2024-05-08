import turtle as t
import random as r
import time 

delay=0.1
bodyParts=[]
score=0
fontSetup=("Times New Roman",20,"normal")
hscore=0

wn=t.Screen()
wn.setup(width=600,height=600)
wn.bgcolor('green')

head = t.Turtle(shape='square')
head.speed(1)
head.penup()
head.direction='stop'

food=t.Turtle(shape='circle')
food.speed(1)
food.penup()
food.teleport(100,100)
food.color('red')

scorekeeper=t.Turtle()
scorekeeper.penup()
scorekeeper.goto(100,200)
scorekeeper.pendown()
scorekeeper.speed(-1000)
scorekeeper.hideturtle()

hscorekeeper=t.Turtle()
hscorekeeper.penup()
hscorekeeper.goto(-200,200)
hscorekeeper.pendown()
hscorekeeper.speed(-1000)
hscorekeeper.hideturtle()

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
        

wn.onkeypress(up,"w")
wn.onkeypress(down,"s")
wn.onkeypress(left,"a")
wn.onkeypress(right,"d")
wn.listen()

while True:
    wn.update()
    #TODO: Check for wall collision
        #up                 #down               #left               #right
    if head.ycor()>290 or head.ycor()<-290 or head.xcor()<-290 or head.xcor()>290:
        head.color('red')
        if score>hscore:
            hscore=score
            hscorekeeper.clear()
            hscorekeeper.write(f"High Score: {hscore}",font=fontSetup)
        score =0
        scorekeeper.clear()
        scorekeeper.write(f"Score: {score}",font=fontSetup)
        for i in range(len(bodyParts)):
            bodyParts[i].hideturtle()
        bodyParts=[]
        time.sleep(1)
        head.goto(0,0)
        head.color('black')
        head.direction = "stop"
        
    #TODO: Check for food collision
    if head.distance(food) < 20:
        score+=100
        scorekeeper.clear()
        scorekeeper.write(f"Score: {score}",font=fontSetup)
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
    #TODO: Check for body collision
    for eachBodyPart in bodyParts:
        if head.distance(eachBodyPart)<10:
            if score>hscore:
                hscore=score
                hscorekeeper.clear()
                hscorekeeper.write(f"High Score: {hscore}",font=fontSetup)
                head.color('red')
                score =0
                scorekeeper.clear()
                scorekeeper.write(f"Score: {score}",font=fontSetup)
                for i in range(len(bodyParts)):
                    bodyParts[i].hideturtle()
                bodyParts=[]
                time.sleep(1)
                head.goto(0,0)
                head.color('black')
                head.direction = "stop"
    time.sleep(delay)