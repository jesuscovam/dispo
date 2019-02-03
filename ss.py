import pyautogui

count = 0

def s():
    global count
    count += 1
    img = pyautogui.screenshot('./imgs/img' + str(count) + '.png')
    
