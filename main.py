#importing libraries
import turtle as t
from random import randint
import time
import threading
from tkinter import *

#------------------------------screen
#main window
mainWn = t.Screen()
t.setup(1000,500)
t.bgcolor('#151740')
t.ht()

#score and timer window
def score_and_timer_wn():
    global score

    window = Toplevel()

    score_and_time = Label(
        window,
        text=str(score),
        fg="white",
        bg="black",
        width=10,
        height=10
    )

    score_and_time.pack()

    window.mainloop()

#leaderboard window

#variables and functions
startTimer = False
score = 0

class clickableTurtle:
    def __init__(self, shape, color, size, speed):
        self.shape = shape
        self.color = color
        self.size = size
        self.speed = speed
        self.trtl = t.Turtle()
        self.trtl.speed(0)

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
        global startTimer, score

        startTimer = True
        score = score + 1

        if startTimer == True:
            xCor = round(randint((-mainWn.window_width()//2)+self.size*10, (mainWn.window_width()//2)-self.size*10))
            yCor = round(randint((-mainWn.window_height()//2)+self.size*10, (mainWn.window_height()//2)-self.size*10))

            self.trtl.penup()
            self.trtl.goto(xCor, yCor)
            self.trtl.pendown()
            self.trtl.shapesize(self.size, self.size, 1)

class countdown_timer:
    def __init__(self, xPos, yPos, size, second):
        self.xPos = xPos
        self.yPos = yPos
        self.size = size
        self.seconds = second

    def startTimer(self):
        while self.seconds > 0:
            print(f"Time remaining: {self.seconds} seconds")
            time.sleep(1)
            self.seconds -= 1

        print("Time's up!")

#initialize turtle
mainTurtle = clickableTurtle('circle', '#D936A0', 1, None)
timer = countdown_timer(None,None,None,5)

#setting up turtle
mainTurtle.show()
mainTurtle.trtl.onclick(mainTurtle.move)

#creating thread for timer
timer_thread = threading.Thread(target=timer.startTimer)

#starting the timer thread
timer_thread.start()

score_and_timer_wn()
mainWn.mainloop()