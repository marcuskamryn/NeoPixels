import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write = False, brightness = 0.3)

def sparkle(background, foreground, t, num):
    np.fill(background)
    for i in range(num):
        np[random.randint(0, np.n - 1)] = foreground
        np.show()
        time.sleep(t)


while True:
    sparkle((10, 5, 32), (175, 45, 200), 0.005, 5)
