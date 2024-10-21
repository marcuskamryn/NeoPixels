import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write = False, brightness = 0.3)


def lightning(color):
    np.fill(color)
    np.show()
    time.sleep(2)
    for i in range(random.randint(1, 5)):
        stop = (random.randint(1,5) / 100)
        time.sleep(stop)
        np.fill((255, 255, 255))
        np.show()
        time.sleep(stop)
        np.fill(color)
        np.show()


while True:
    lightning((68, 0, 65))
