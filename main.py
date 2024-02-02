#importing libraries
import turtle as t
from random import randint

#screen
wn = t.Screen()
t.setup(1000,500)
t.bgcolor('#151740')
t.ht()

#variables and functions
startTimer = False

class clickableTurtle:
    def __init__(self, shape, color, size, speed):
        self.shape = shape
        self.color = color
        self.size = size
        self.speed = speed
        self.trtl = t.Turtle()
        global startTimer

    def show(self):
        self.trtl.fillcolor(self.color)

        self.trtl.penup()
        self.trtl.goto(0, 0)
        self.trtl.pendown()
        self.trtl.shapesize(self.size, self.size, 1)

        self.trtl.begin_fill()
        self.trtl.shape(self.shape)
        self.trtl.end_fill()

    def move(self, x, y):
        startTimer = True

        if startTimer == True:
            xCor = round(randint((-wn.window_width()//2)+self.size*10, (wn.window_width()//2)-self.size*10))
            yCor = round(randint((-wn.window_height()//2)+self.size*10, (wn.window_height()//2)-self.size*10))

            self.trtl.penup()
            self.trtl.goto(xCor, yCor)
            self.trtl.pendown()
            self.trtl.shapesize(self.size, self.size, 1)


#initialize turtle
mainTurtle = clickableTurtle('circle', '#D936A0', 1, None)

mainTurtle.show()
mainTurtle.trtl.onclick(mainTurtle.move)

wn.mainloop()