import pyautogui

def click_on_location(location):
    if location is not None:
        pyautogui.moveTo(location)
        pyautogui.click()
        print(f"Clicou na localização: {location}")
