from pynput.keyboard import Key, Controller
import time

message = "Flod para whats app em python d"
keyboard = Controller()

time.sleep(5)

for num in range(1000):
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)