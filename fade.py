#imports
import board
from neopixel import NeoPixel
import time
import random

#setup
np = NeoPixel(board.D2, 30, auto_write = False, brightness = 0.3)
steps = 50


def fade_out(color, speed = 0.005):
    red_value = color[0]
    green_value = color[1]
    blue_value = color[2]
    
    red_ratio = color[0] / 50
    green_ratio = color[1] / 50
    blue_ratio = color[2] / 50
    
    for i in range(51):
        red = red_value - i*red_ratio
        green = green_value - i*green_ratio
        blue = blue_value - i*blue_ratio
        np.fill((red, green, blue))
        np.show()
        time.sleep(speed)

    
def fade_in(color, speed = 0.005):
    red_value = color[0]
    green_value = color[1]
    blue_value = color[2]
    
    red_ratio = color[0] / 50
    green_ratio = color[1] / 50
    blue_ratio = color[2] / 50
    
    for i in range(51):
        red = i*red_ratio
        green = i*green_ratio
        blue = i*blue_ratio
        np.fill((red, green, blue))
        np.show()
        time.sleep(speed)
        

while True:
    fade_out((255, 53, 78), 0.05)
    fade_in((78, 53, 255), 0.05)
