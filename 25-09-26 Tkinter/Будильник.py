from tkinter import *
from tkinter import messagebox
import time


root = Tk()
root.title('Будильник')
root.config(background='black')
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
X = 400
Y = 200
root.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}"
              f"+{HEIGHT // 2 - Y // 2 - 25}")

screen_time = Label(root, text='00:00:00', font='Arial 50')
screen_time.config(bg='black', fg='lime')
screen_time.pack() # размещение

entry_time = Entry(root, width=10, font='Arial 20', justify=CENTER)
entry_time.pack() # Окно для ввода времени

on = Button(root, text='Включить', font=('Arial 10'))
on.pack() #  кнопка включения

off = Button(root, text='ВЫключить', font=('Arial 10'))
off .pack() # кнопка выключения

def tick():
    global time_alarm
    current_time = time.strftime("%H:%M:%S")
    if (time_alarm == current_time or
            time_alarm == time.strftime("%H:%M") or
            time_alarm == time.strftime("%H")):
        time_alarm = ''
        pass
    screen_time.after(1000, tick)
    screen_time.config(text=current_time)


def tick():
    global time_alarm
    current_time = time.strftime("%H:%M:%S")
    if (time_alarm == current_time or
            time_alarm == time.strftime("%H:%M") or
            time_alarm == time.strftime("%H")):
        time_alarm = ''
        pass
    screen_time.after(1000, tick)
    screen_time.config(text=current_time)


def on_click():
    global time_alarm
    time_alarm = entry_time.get().strip()


def off_click():
    pass

root.mainloop()