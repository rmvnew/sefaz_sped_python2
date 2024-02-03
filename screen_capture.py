from PIL import ImageGrab
import numpy as np
import cv2

def get_screenshot():
    screen = np.array(ImageGrab.grab())
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    return screen
