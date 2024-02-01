#importing libraries
import turtle as t

#screen
wn = t.Screen()

#variables and functions
class clickableTurtle():
    def __init__(self, shape, color, size, speed):
        self.shape = str(shape)
        self.color = str(color)
        self.size = str(size)
        self.speed = speed

    def show(self):
        t.fillcolor(self.color)

        t.begin_fill()
        t.shape(self.shape, self.shape, 0)
        t.end_fill()

#game configuration

#initialize turtle

#game functions

#mouse events

wn.mainloop()