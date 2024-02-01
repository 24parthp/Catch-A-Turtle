#importing libraries
import turtle as t
import random

#screen
wn = t.Screen()
t.setup(1000,500)

#variables and functions
clickedTurtle = False

class clickableTurtle:
    def __init__(self, shape, color, size, speed):
        self.shape = str(shape)
        self.color = str(color)
        self.size = size
        self.speed = speed

    def show(self):
        t.fillcolor(self.color)

        #t.goto(random.randint(0+self.size, width-))
        t.shapesize(self.size, self.size, 1)

        t.begin_fill()
        t.shape(self.shape)
        t.end_fill()

    # def move(self):
    #     if clickedTurtle == True:


#initialize turtle
mainTurtle = clickableTurtle('circle', 'blue', 10, None)

mainTurtle.show()

#mouse events

wn.mainloop()