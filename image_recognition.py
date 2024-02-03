from screen_capture import get_screenshot
import cv2
import numpy as np

def find_image_on_screen(template_path, threshold=0.7):

    print(f"Path: {template_path}")

    screen = get_screenshot()
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
    h, w, _ = template.shape
    res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    
    if loc[0].size > 0:
        pt = (loc[1][0], loc[0][0])
        return (pt[0] + w // 2, pt[1] + h // 2)
    return None
