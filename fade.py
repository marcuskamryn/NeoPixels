#imports
import board
from neopixel import NeoPixel
import time
import random

#setup
np = NeoPixel(board.D2, 30, auto_write = False, brightness = 0.3)
steps = 0

def fade_out(r, g, b):
    if r > g and b:
        steps = r
    elif g > r and b:
        steps = g
    else:
        steps = b
    for i in range(steps):
        np
    
def fade_in(r, g, b):

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
