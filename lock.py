import os
import keyboard
import wmi
import subprocess
import psutil
from tkinter import *
from tkinter import ttk

f = wmi.WMI()

file_path = "C:\\Users\\özer çelik\\Desktop\\lock2\\closer.py"
prog_name = "C:\\Program Files\\Python310\\python.exe"

p = subprocess.Popen([prog_name, file_path])

flag = 0
closeflag = 0

def check_system():
    global flag
    for p in psutil.process_iter(attrs=['pid', 'name']):
        if "notepad.exe" in (p.info['name']).lower():
            print("Notepad is running")
            flag = 1
        else:
            print("Notepad.exe is not running")
        if "taskmgr.exe" in (p.info['name']).lower():
            print("Task Manager  is running")
            flag = 1
        else:
            print("Task Manager is not running")
        if "python-3.10.2-amd64.exe" in (p.info['name']).lower():
            print("Python-unnistal is runnning")
            flag = 1
        else:
             print("Python-unistall is not running")

def close_file():
    os.system('TASKKILL /F /IM notepad.exe')


def login_form():
    win = Tk()
    win.resizable(False, False)
    win.overrideredirect(True)
    win.geometry("300x400")
    password = StringVar()
    def password_correction():
        global flag
        p = password.get()
        if p == "1234":
            ttk.Label(win, text="Welcome").pack()
            win.destroy()
        elif p != "1234":
            ttk.Label(win, text="Try again").pack()
        elif p == "lock":
            os.system('TASKKIL /F /IM notepad.exe')
            win.destroy()
            flag = 0
    win.deiconify()
    entry = Entry(win, width=25, textvariable=password, show="*")
    entry.pack(pady=20)
    ttk.Button(win, text="Ok", command=password_correction).pack()
    win.mainloop()

def lock():
    global flag
    if keyboard.is_pressed('f12'):
        os.system('TASKKILL /F /IM notepad.exe')
        flag = 0

while True:
    if flag == 1:
        p = subprocess.Popen([prog_name, file_path])
        login_form()
        flag = 2
        print(flag)
    elif flag == 0:
        p.kill()
        print("program is terminated")
        check_system()
    elif flag == 2:
        p.kill()
        lock()