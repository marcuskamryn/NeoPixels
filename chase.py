import board
from neopixel import NeoPixel
import time

np = NeoPixel(board.D2, 30, auto_write = False, brightness = 0.3)


def chase(color):
    count = 0
    for i in range(np.n):
        np.fill(color)
        for i in range(np.n):
            if(i + count) % 3 == 0:
                np[i] = (0, 0, 0)
        np.show()
        time.sleep(0.1)
        count = (count + 1) % 3
        
while True:
    chase((0,0,255))
