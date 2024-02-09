#importing libraries
import turtle as t
from random import randint
import time
import threading
from tkinter import *

#------------------------------screen
#main window
mainWn = t.Screen()
mainWn.mode('world')
t.setup(1000,500)
t.bgcolor('#151740')
t.ht()

#score and timer window
def score_and_timer_wn():
    global score

    window = Toplevel()

    window.geometry("200x200+550+470")

    score_and_time = Label(
        window,
        text=str(score),
        font=("Arial", 25),
        fg="#060126",
        bg="#1BF2B5",
        width=20,
        height=20
    )

    score_and_time.pack()

    update_score_label(score_and_time)

    window.mainloop()

#leaderboard window

#updating score/timer window
def update_score_label(label):
    global score
    label.config(text=str(score))
    label.after(10, lambda: update_score_label(label))

#retry screen
def retryWn():
    def execute_commands():
        global score, startTimer, showRetryWn

        startGame()
        score = 0
        startTimer = False
        showRetryWn = False

    retry = Toplevel()

    label = Label(retry, text="Try Again?")
    button1 = Button(retry, text="Yes", command=execute_commands())
    button2 = Button(retry, text = "No", command=mainWn.bye())

    button1.pack(), button2.pack()
    label.pack()

#variables and functions
startTimer = False
score = 0
showRetryWn = False

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
    def __init__(self, second):
        self.seconds = second
        self.running = True

    def startTimer(self):
        while self.seconds > 0 and self.running:
            print(f"Time remaining: {self.seconds} seconds")
            time.sleep(1)
            self.seconds -= 1

        print("Time's up!")
        #retryWn()
    
    def stop(self):
        self.running = False

#initialize turtle
def startGame():
    global mainTurtle, timer

    mainTurtle = clickableTurtle('circle', '#D936A0', 1, None)
    timer = countdown_timer(5)

    #setting up turtle
    mainTurtle.show()
    mainTurtle.trtl.onclick(mainTurtle.move)

    #creating thread for timer
    timer_thread = threading.Thread(target=timer.startTimer)

    #starting the timer thread
    timer_thread.start()

def terminate():
    global timer, mainWn
    timer.stop()
    mainWn.bye()

mainWn.listen()
mainWn.onkey(terminate, 'q')

startGame()
score_and_timer_wn()
mainWn.mainloop()