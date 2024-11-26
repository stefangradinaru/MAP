import pyautogui
import time
import keyboard

def  cautare_google():
    if pyautogui.locateOnScreen(r'C:\Users\stefa\Desktop\Facultate Info\Anul II\Semestrul I\MAP\Lab_2\test.png', confidence=0.3) !=None:
        print("DA")
        time.sleep(10)
        camp_google=  pyautogui.locateOnScreen(r'C:\Users\stefa\Desktop\Facultate Info\Anul II\Semestrul I\MAP\Lab_2\Cauta.png', confidence=0.3)
        pyautogui.click(camp_google)
        time.sleep(5)
        pyautogui.write("https://www.youtube.com/watch?v=a2giXO6eyuI")
        pyautogui.press('enter')
        time.sleep(2)

cautare_google()