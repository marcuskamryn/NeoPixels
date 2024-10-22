import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write = False, brightness = 0.3)

np.fill((230, 115, 0))

def fire(pcolor, color1, color2):
    np.fill(pcolor)
    np.show()
    for i in range(np.n / 2):
        np[random.randint(0, np.n - 1)] = color1
        np[random.randint(0, np.n - 1)] = color2
        np.show()
        time.sleep(random.randint(1,5) / 1000)
    
    
while True:
    fire((230, 115, 0), (250, 75, 5), (255, 50, 0))
