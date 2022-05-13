import os
import time
import keyboard
import wmi
import subprocess
import psutil
import pygame
f = wmi.WMI()

file_path = "closer.py"
prog_name = "pythonw.exe"

p = subprocess.Popen([prog_name, file_path])

flag = 0
running =  0

def check_system():
    global flag
    for p in psutil.process_iter(attrs=['pid', 'name']):
        if "notepad.exe" in (p.info['name']).lower():
            flag = 1
        if "taskmgr.exe" in (p.info['name']).lower():
            flag = 1
        if "python-3.10.2-amd64.exe" in (p.info['name']).lower():
            flag = 1
        if "processhacker.exe" in (p.info['name']).lower():
            flag = 1

def close_file():
    os.system('TASKKILL /F /IM notepad.exe')

def password_correction():
    global flag
    if os.path.exists("D:\\"):
        with open("D:\\password.txt", "r") as password_file:
            password_check = password_file.read()
            if password_check == "KU$G_p9Jaq3x2r@^":
                flag = 2
                print("Welcome Semih")
                pygame.mixer.init()
                pygame.mixer.music.load("welcome.mp3")
                pygame.mixer.music.play()
            else:
                print("Wrong password")


def lock():
    global flag
    if keyboard.is_pressed('f12'):
        flag = 0

while True:
    if flag == 1:
        if running == 0:
            p = subprocess.Popen([prog_name, file_path])
        running = 1
        password_correction()
    elif flag == 0:
        p.kill()
        running = 0
        check_system()
    elif flag == 2:
        p.kill()
        lock()
