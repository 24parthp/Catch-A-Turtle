#importing libraries
import turtle as t
from random import randint
import time
import threading
from tkinter import *
import sys
import json

#------------------------------screen
#main window
mainWn = t.Screen()
mainWn.mode('world')
t.setup(1000,500)
t.bgcolor('#151740')
t.ht()

#user's name window
def ask_username():

    def sendUserInfo():
        global username 
        input = inputtxt.get('1.0', 'end-1c')
        username = str(input)
        print(username)
        username_wn.destroy()

    username_wn = Toplevel()
    username_wn.title('Username Input')
    username_wn.geometry('200x100')

    inputtxt = Text(username_wn, height = 1, width = 10)
    inputtxt.pack()

    button = Button(username_wn, text='Start', command=sendUserInfo)
    button.pack()

    username_wn.grab_set()

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
    global mainTurtle, timer, startTimer

    mainTurtle = clickableTurtle('circle', '#D936A0', 1, None)
    timer = countdown_timer(5)

    #setting up turtle
    mainTurtle.show()
    mainTurtle.trtl.onclick(mainTurtle.move)

    #terminate window
    terminate()

    #asking for users name
    ask_username()

#start timer thread
def startTimerThread():
    global startTimer, timer, terminate_threads

    while not startTimer and not terminate_threads:
        time.sleep(0.1)
    
    if terminate_threads:
        return

        #starting the timer thread
    if startTimer == True:
        #creating thread for timer
        timer_thread = threading.Thread(target=timer.startTimer)
        timer_thread.start()

#closes all the windows and also the timer theard
def terminate():
    def closeEverything():
        global timer, mainWn, terminate_threads
        terminate_threads = True
        timer.stop()
        exit.destroy()
        mainWn.bye()
        sys.exit()

    exit = Toplevel()
    exit.geometry('500x100')

    Warningtxt = Text(exit, height=5, width=60)
    Warningtxt.pack()

    Warningtxt.insert(END, "To exit the program press the 'exit' button on the bottom. \n!!! DO NOT CLOSE THE PROGRAM BY PRESSING THE 'X' ON THE TOP RIGHT!!!")

    button = Button(exit, text='Exit', command=closeEverything)
    button.pack()

#----------------------------variables
startTimer = False
score = 0
showRetryWn = False
username = 'test123'
terminate_threads = False

timer_check_thread = threading.Thread(target=startTimerThread)
timer_check_thread.start()

startGame()
score_and_timer_wn()
mainWn.mainloop()

# to-do
# make a new window which 'terminate's the program ----- Done
# Make a window which asks for users name -------------- Done
# ask for user's name ---------------------------------- Done
# implement json 
# make a new window for leaderboard