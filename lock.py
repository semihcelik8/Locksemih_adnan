import os
import keyboard
import wmi
import subprocess
import pygame
f = wmi.WMI()

flag = 0

CREATE_NO_WINDOW = 0x08000000

try:
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0)
    pygame.mixer.music.load("welcome.mp3")
    pygame.mixer.music.play()
except:
    pass

def killprograms():
    subprocess.call('taskkill /F /IM processhacker.exe', creationflags=CREATE_NO_WINDOW)
    subprocess.call('taskkill /F /IM taskmgr.exe', creationflags=CREATE_NO_WINDOW)

def password_correction():
    global flag
    if os.path.exists("E:\\"):
        with open("E:\\password.txt", "r") as password_file:
            password_check = password_file.read()
            if password_check == "[PASSWORD GOES HERE]":
                try:
                    pygame.mixer.init()
                    pygame.mixer.music.load("welcome.mp3")
                    pygame.mixer.music.play()
                except:
                    pass
                flag = 1

def lock():
    global flag
    if keyboard.is_pressed('f12'):
        flag = 0

while True:
    if flag == 0:
        killprograms()
        password_correction()
    else:
        lock()
