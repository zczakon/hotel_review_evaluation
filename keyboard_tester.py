import keyboard
import time
import random

while True:
    keyboard.press_and_release("F13")
    interval = random.randint(1, 179)
    time.sleep(interval)