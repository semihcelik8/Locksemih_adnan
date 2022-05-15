import os
import keyboard
import wmi
import subprocess
import psutil
import pygame
f = wmi.WMI()

flag = 0
running =  0

def check_system():
    global flag
    for p in psutil.process_iter(attrs=['pid', 'name']):
        if "taskmgr.exe" in (p.info['name']).lower():
            flag = 1
        if "processhacker.exe" in (p.info['name']).lower():
            flag = 1

def runcloser():
    os.startfile("closer.exe")

def killcloser():
    CREATE_NO_WINDOW = 0x08000000
    subprocess.call('taskkill /F /IM closer.exe', creationflags=CREATE_NO_WINDOW)

def password_correction():
    global flag
    if os.path.exists("E:\\"):
        with open("E:\\password.txt", "r") as password_file:
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
            runcloser()
        running = 1
        password_correction()
    elif flag == 0:
        killcloser()
        running = 0
        password_correction()
        check_system()
    elif flag == 2:
        killcloser()
        lock()
