from pynput import keyboard
from pynput import mouse

# Classes
class ClickRecorder:
    def __init__(self):
        self.first_click = None
        self.second_click = None

    def on_mouse_click(self, x, y, button, pressed):
        if pressed:
            if self.first_click is None:
                self.first_click = (x, y)
                print("First click recorded:", self.first_click)
            else:
                self.second_click = (x, y)
                print("Second click recorded:", self.second_click)
                self.print_selected_area()
                self.stop_listener()

    def print_selected_area(self):
        if self.first_click is not None and self.second_click is not None:
            x1, y1 = self.first_click
            x2, y2 = self.second_click
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            selected_area = f"Selected Area: (x={x1}, y={y1}, width={width}, height={height})"
            print(selected_area)

    def stop_listener(self):
        mouse_listener.stop()

# Functions
def check_key(key):
    if key == keyboard.Key.esc:
        key_listener.stop()
        mouse_listener.stop() # end all listners while program is ending
        print("Esc pressed, exiting program!")
        quit()

# Listeners
click_recorder = ClickRecorder()
mouse_listener = mouse.Listener(on_click=click_recorder.on_mouse_click)
key_listener = keyboard.Listener(on_press=check_key) # Keep the program running until interrupted

print("Click on the first point.")
print("(Press ESC to end the program)")
mouse_listener.start()
key_listener.start()
key_listener.join()
