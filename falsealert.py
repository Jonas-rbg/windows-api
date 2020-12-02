import ctypes
import random
user_handle = ctypes.WinDLL("User32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")
hWnd = None
uType = 0x00000001
import sys
import time
import os
loading= "LOADING\n"
bar = "[■■■■■■■■■■■■■■■■■■■■■■■■]"
print(loading)
for c in bar:
    
    time.sleep(0.3)
    sys.stdout.write(c)
    sys.stdout.flush()
    

os.system('cls')
print("Injecting Windows\nFound Match\nLooking For Backdoor...\nInjecting Into Google Chrome\nFound DATA\nSending Information To 192.107.1.1:80\nSuccessfully Stole Information")
for x in range(10):
    lpText = random.choice(["Virus Detected","Uninstalling SYS32","Error","Virus","CODE 404"])
    lpCaption = random.choice(["Message","Alert","Error","Virus","CODE 404"])
    response = user_handle.MessageBoxW(hWnd,lpText,lpCaption,uType)


error = k_handle.GetLastError()
if error !=0:
    print("Error code: {0}".format(error))
    exit(1)
if response == 1:
    print("user clicked ok!")
elif response == 2:
    print("user clicked cancel")
