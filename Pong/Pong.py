import turtle as t
import random as r

screenW=500
screenH=500
rightScore=0
leftScore=0
fontSetup=("Times New Roman",24,"normal")
fontSettings=("Times New Roman",52,"normal")
fontSetupTitle=("Times New Roman",72,"normal")
wn=t.Screen()
wn.setup(width=screenW,height=screenH)
wn.bgcolor('black')

trtl=t.Turtle()
trtl.speed(0)
trtl.color('white')
trtl.shapesize(3,10)
trtl.fillcolor('black')
trtl.shape('square')
trtl.teleport(-0,-100)

drawer=t.Turtle()
drawer.speed(0)
drawer.color('white')
drawer.teleport(-100,100)
drawer.write("Pong",font=fontSetupTitle)
drawer.teleport(-28,-115)
drawer.write("Play",font=fontSetup)

left=t.Turtle()
left.color('dark blue')
left.speed(1)
left.shape('square')
left.penup()
left.turtlesize(4,1)
left.teleport(-500,0)
left.direction="stop"

right=t.Turtle()
right.color('dark red')
right.speed(1)
right.shape('square')
right.penup()
right.turtlesize(4,1)
right.teleport(500,0)
right.direction="stop"

ball=t.Turtle('circle')
ball.color('white')
ball.penup()
ball.speed(0)

lScore = t.Turtle(visible=False)
lScore.speed(0)
lScore.color('white')
lScore.penup()
lScore.setposition(-1000/4,600/4)
lScore.write(leftScore,font=fontSettings)

rScore = t.Turtle(visible=False)
rScore.speed(0)
rScore.color('white')
rScore.penup()
rScore.setposition(1000/4,600/4)
rScore.write(rightScore,font=fontSettings)

def drawCourt():
    global wn
    screen_h = 650
    screen_w = 1050
    dashLine=300

    pen=t.Turtle()
    pen.color('white')
    pen.speed(0)
    pen.teleport(-500,300)


    wn = t.Screen()
    wn.setup(width=screen_w, height=screen_h)
    wn.bgcolor('black')

    pen.goto(500,300)
    pen.teleport(-500,-300)
    pen.goto(500,-300)

    for i in range(12):
        pen.teleport(0,dashLine-(26*(i)))
        pen.goto(0,dashLine-(26*(i+1)))
        dashLine-=26

    pen.hideturtle()

def gameStart(x,y):
    global drawer
    global trtl
    global rightScore
    global leftScore
    drawer.hideturtle()
    drawer.clear()
    trtl.hideturtle()
    drawCourt()
    if leftScore <7 or rightScore<7:
        ballMove()
    



    

    

def leftup():
    left.direction="up"
    move()
def leftdown():
    left.direction="down"
    move()
def rightup():
    right.direction="up"
    move()
def rightdown():
    right.direction="down"
    move()


def move():
    if left.direction=="up":
        if left.ycor()<300:
            left.sety(left.ycor()+20)
        left.direction="stop"
            
    elif left.direction=="down":
        if left.ycor()>-300:
            left.sety(left.ycor()-20)
        left.direction="stop"
            
    elif right.direction=="up":
        if right.ycor()<300:
            right.sety(right.ycor()+20)
        right.direction="stop"
            
    elif right.direction=="down":
        if right.ycor()>-300:    
            right.sety(right.ycor()-20)
        right.direction="stop"
               
    # br=""
    # while br!="break":
    #     wn.update()
    #     move()
    #     br=="break"
            
def ballMove():
    global rightScore
    global leftScore
    if leftScore <7 or rightScore<7:
        ball.fd(20)
    x,y=ball.position()
    
    if y>300:
         ball.setheading(-ball.heading())

    elif y<-300:  
        ball.setheading(-ball.heading())

    elif x>500:
         if leftScore <7 or rightScore<7:
            leftScore+=1
         lScore.clear()
         lScore.write(leftScore,font=fontSettings)
         if leftScore <7 or rightScore<7:
            resetBall()
         ball.setheading(r.randint(-30,30))

    elif x<-500:
         if leftScore <7 or rightScore<7:
            rightScore+=1
         rScore.clear()
         rScore.write(rightScore,font=fontSettings)
         if leftScore <7 or rightScore<7:
            resetBall()
         ball.setheading(r.randint(150,210))

    if ball.distance(left) <30:
        ball.setx(ball.xcor()+15)
        ball.setheading(180-ball.heading())
    elif ball.distance(right)<30:
        ball.setx(ball.xcor()-15)
        ball.setheading(180-ball.heading())

    if rightScore >=7:
        rScore.clear()
        rScore.write("Winner!",font=fontSettings)
    elif leftScore >= 7:
        lScore.clear()
        lScore.write("Winner!",font=fontSettings)
    if leftScore <7 or rightScore<7:
        wn.ontimer(ballMove,50)
def resetBall():
     global leftScore
     global rightScore
    
     if leftScore <7 or rightScore<7:

        ball.setposition(0,0)
        #randomizer for who serves first
        if r.randint(0,1)==0:    #left first
            ball.setheading(r.randint(150,210))
        else:
            ball.setheading(r.randint(-30,30))




wn.onkeypress(resetBall,"r")




trtl.onclick(gameStart)

wn.onkeypress(leftup,"w")
wn.onkeypress(leftdown,"s")
wn.onkeypress(rightup,"Up")
wn.onkeypress(rightdown,"Down")

wn.listen()

wn.mainloop()