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
        leaderboardwn()

    username_wn = Toplevel()
    username_wn.title('Username Input')
    username_wn.geometry('400x100+765+540')

    infotxt = Text(username_wn, height=1, width= 40)
    infotxt.pack()
    infotxt.insert(END, 'Enter Username below and then hit start')

    inputtxt = Text(username_wn, height = 1, width = 20)
    inputtxt.pack()

    button = Button(username_wn, text='Start', command=sendUserInfo)
    button.pack()

    username_wn.grab_set()

#score and timer window
def scoreWn():
    global score

    window = Toplevel()
    window.geometry("200x200+250+290")

    scoretxt = Label(
        window,
        text=str(score),
        font=("Arial", 25),
        fg="#060126",
        bg="#1BF2B5",
        width=20,
        height=20
    )

    scoretxt.pack()

    update_score_label(scoretxt)

    window.mainloop()

#leaderboard window
def leaderboardwn():
    ldwindow = Toplevel()
    ldwindow.geometry("200x500+1470+290")
    txt = Text(ldwindow, height=1000, width=100, font=("Arial", 10))

    with open('data.json', mode='r') as f:

        data = json.load(f)
        for i in data:
            name = (i['username'])
            score = (i['score'])
            print(name, score)
            showData = name + ' - ' + str(score) + '\n'
            txt.insert(END, showData)

    txt.pack()

    ldwindow.mainloop()

#timer window
def timerWn():
    global timerSeconds

    timewindow = Toplevel()
    timewindow.geometry("200x200+250+550")

    timetxt = Label(
        timewindow,
        text=timerSeconds,
        font=("Arial", 25),
        fg="#060126",
        bg="#F21D92",
        width=20,
        height=20
    )

    timertxt = Text(timewindow, height= 1, width=10, font=("Arial", 25))
    timertxt.insert(END, "Time")

    timertxt.pack(),timetxt.pack()

    update_time_label(timetxt)

    timewindow.mainloop()

#saving data
def save_score():
    global username, score

    json_file_path = "data.json"

    data = {"username": username, "score": score}

    try:
        with open(json_file_path, "r") as f:
            scores = json.load(f)
    except FileNotFoundError:
        scores = []

    scores.append(data)

    json_string = json.dumps(scores, indent= 4)

    with open(json_file_path, "w") as f:
        f.write(json_string)

#updating score/timer window
def update_score_label(label):
    global score
    label.config(text=str(score))
    label.after(10, lambda: update_score_label(label))

def update_time_label(label):
    global timerSeconds
    label.config(text=timerSeconds)
    label.after(10, lambda: update_time_label(label))

#retry screen
def retryWn():
    def execute_commands():
        global score, startTimer, mainTurtle

        save_score()
        retry.destroy()
        restartGame()
        startGame()
        score = 0
        startTimer = False

    def exit():
        save_score()
        closeEverything()

    retry = Toplevel()
    retry.geometry('400x100+1100+700')

    label = Text(retry, height=1, width=10)
    label.insert(END, "Try again?")

    button1 = Button(retry, text="Yes", command=execute_commands)
    button2 = Button(retry, text = "No", command=exit)

    label.pack(), button1.pack(), button2.pack()

class clickableTurtle:
    def __init__(self, shape, color, size, speed):
        self.shape = shape
        self.color = color
        self.size = size
        self.speed = speed
        self.t = t
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
        global score, username

        self.seconds = second
        self.running = True

    def startTimer(self):
        global timerSeconds

        while self.seconds > 0 and self.running:
            print(f"Time remaining: {timerSeconds} seconds")
            time.sleep(1)
            self.seconds -= 1
            timerSeconds = self.seconds

        print("Time's up!")
        retryWn()
    
    def stop(self):
        self.running = False

#initialize turtle
def startGame():
    global mainTurtle, timer, startTimer, terminateWn, timerSeconds

    mainTurtle = clickableTurtle('circle', '#D936A0', 1, None)
    timer = countdown_timer(timerSeconds)

    #setting up turtle
    mainTurtle.show()
    mainTurtle.trtl.onclick(mainTurtle.move)

    #terminate window
    if terminateWn == False:
        terminate()
        terminateWn = True
    else:
        return

    #asking for users name
    ask_username()

    scoreWn()

#start timer thread
def startTimerThread():
    global startTimer, timer, terminate_threads, timerSeconds

    while not startTimer and not terminate_threads:
        time.sleep(0.1)
    
    if terminate_threads:
        return

        #starting the timer thread
    if startTimer == True:
        #creating thread for timer
        timer_thread = threading.Thread(target=timer.startTimer)
        timer_thread.start()

        while timerSeconds > 0 and not terminate_threads:
            timerWn()
            time.sleep(1)

#closing everything
def closeEverything():
        global timer, mainWn, terminate_threads
        terminate_threads = True
        timer.stop()
        mainWn.bye()
        sys.exit()

#closes all the windows and also the timer thread
def terminate():

    exit = Toplevel()
    exit.geometry('500x100+700+150')

    Warningtxt = Text(exit, height=5, width=60)
    Warningtxt.pack()

    Warningtxt.insert(END, "To exit the program press the 'exit' button on the bottom. \n!!! DO NOT CLOSE THE PROGRAM BY PRESSING THE 'X' ON THE TOP RIGHT!!!")

    button = Button(exit, text='Exit', command=closeEverything)
    button.pack()

#restarts the canvas for next game
def restartGame():
    global mainTurtle
    mainTurtle.trtl.clear()

#----------------------------variables
timerSeconds = 10
startTimer = False
score = 0
username = ''
terminate_threads = False
terminateWn = False

timer_check_thread = threading.Thread(target=startTimerThread)
timer_check_thread.start()

startGame()
mainWn.mainloop()

# to-do
# make a new window which 'terminate's the program ----- Done
# Make a window which asks for users name -------------- Done
# ask for user's name ---------------------------------- Done
# configure all the data 
    # player username----------------------------------- Done
    # score--------------------------------------------- Done
# implement json --------------------------------------- Done
# make a new window for leaderboard