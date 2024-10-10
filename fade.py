#imports
import board
from neopixel import NeoPixel
import time
import random

#setup
np = NeoPixel(board.D2, 30, auto_write = False, brightness = 0.3)
steps = 50


def fade_out(color, speed):
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

    
def fade_in(color, speed):
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

"""
def fade_out():
    for i in range(256):
        np.fill((0, 0, 255 - i))
        np.show()

def fade_in():
    for i in range(256):
        np.fill((0, 0, i))
        np.show()
    
while True:
    fade_in()
    fade_out()
"""


"""
i = 0
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
color_list = [red, green, blue, yellow, cyan, magenta]


#main
while True:
    for i in range(np.n):
        np[i] = random.choice(color_list)
    np.show()
    time.sleep(.1)
"""
