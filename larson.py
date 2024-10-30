import board
from neopixel import NeoPixel
import time

np = NeoPixel(board.D2, 30, auto_write = False, brightness = 0.3)

def bounce(background, foreground, num):
    direction = 1
    for i in range(num):
        for i in range(np.n):
            np.fill(background)
            np[i * direction] = foreground
            time.sleep(0.1)
            np.show()
        direction = direction * (-1)
    

while True:
    bounce((0, 0, 255), (255, 0, 0), 4)
