import time
from datetime import datetime
from pynput.keyboard import Controller, Key
import webbrowser

keyboard = Controller()

isStarted = False

lst = [
    ["https://us04web.zoom.us/j/73077209804?pwd=U1RyWXBBSDVWeC84bFFUaDlpbmx0dz09", "12:58", "13:20"]
]

for i in lst:
    while True:
        if not isStarted:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                webbrowser.open(i[0])
                isStarted = True
        else:
            if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                keyboard.press('w')
                time.sleep(1)
                keyboard.press(Key.enter)
                isStarted = False
                break
        time.sleep(5)
