import pytesseract
import pyautogui
import time
import cv2
import numpy as np

search_image = '[path]'

location_request = False
time.sleep(2)

show_rect = False

def display_rectangles(screen_image):
    if show_rect:
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        cv2.imshow("Matches", screen_image)
        cv2.namedWindow("Matches", cv2.WINDOW_NORMAL)
        cv2.moveWindow("Matches", 0, -30)
        cv2.resizeWindow("Matches", 500, 300)
        cv2.waitKey(0)

def compare_image_with_screen(template_image):
    
    screen_image = pyautogui.screenshot()
    screen_image = cv2.cvtColor(np.array(screen_image), cv2.COLOR_RGB2BGR)
    template_image = cv2.imread(template_image)
    result = cv2.matchTemplate(screen_image, template_image, cv2.TM_CCOEFF_NORMED)
    threshold = 0.87
    locations = np.where(result >= threshold)
    matched_locations = list(zip(locations[1], locations[0]))

    for location in matched_locations:
        list(zip(locations[1], locations[0]))
        x, y = location
        cv2.rectangle(screen_image, (x, y), (x + template_image.shape[1], y + template_image.shape[0]), (0, 255, 0), 2)

    display_rectangles(screen_image)
    pyautogui.moveTo(x, y)

    if location_request:
        return list(zip(locations[1], locations[0]))
    return len(locations[0]) > 0

while 1:
    ENEMIES_PRESENT = compare_image_with_screen(search_image)
    if ENEMIES_PRESENT:
        show_rect = True
        location_request = False
        locations = compare_image_with_screen(search_image)  # Retrieve the locations
        print('Image found')
    else:
        print('Image not found')
   