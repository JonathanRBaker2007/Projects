import turtle as t
import random as r

screenW=1000
screenH=600
rscore=0
lscore=0

wn=t.Screen()
wn.setup(width=screenW,height=screenH)
wn.bgcolor('black')

ball=t.Turtle('circle')
ball.color('white')
ball.penup()
ball.speed(0)

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

def ballMove():
    global rscore
    global lscore
    ball.fd(20)
    x,y=ball.position()
    
    if y>500:
         ball.setheading(-ball.heading())

    if y<-500:  
        ball.setheading(+ball.heading())

    if x>500:
         lscore+=1
         resetBall()

    if x<-500:
         rscore+=1
         resetBall()


    wn.ontimer(ballMove,50)
def resetBall():
     ball.setposition(0,0)
     #randomizer for who serves first
     if r.randint(0,1)==0:    #left first
          ball.setheading(r.randint(150,210))
     else:
          ball.setheading(r.randint(-30,30))

wn.onkeypress(resetBall,"r")
wn.listen()
drawCourt()
ballMove()
wn.mainloop()