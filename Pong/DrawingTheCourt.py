import turtle as t
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

drawCourt()

wn.mainloop()