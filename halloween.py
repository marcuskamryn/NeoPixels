import board
from neopixel import NeoPixel
import time
import random

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
        
def fire(pcolor, color1, color2):
    np.fill(pcolor)
    np.show()
    for i in range(np.n / 2):
        np[random.randint(0, np.n - 1)] = color1
        np[random.randint(0, np.n - 1)] = color2
        np.show()
        time.sleep(random.randint(1,5) / 1000)
        
def lightning(color):
    for i in range(random.randint(1, 5)):
        stop = (random.randint(1,5) / 100)
        time.sleep(stop)
        np.fill((255, 255, 255))
        np.show()
        time.sleep(stop)
        np.fill(color)
        np.show()
    np.fill(color)
    np.show()
    time.sleep(2)


def sparkle(background, foreground, t, num):
    np.fill(background)
    for i in range(num):
        np[random.randint(0, np.n - 1)] = foreground
        np.show()
        time.sleep(t)

        
while True:
    for i in range(np.n * 2):
        fire((230, 115, 0), (250, 75, 5), (255, 50, 0))
    fade_out((230, 115, 0))
    time.sleep(1)
    for i in range(5):
        lightning((125, 0, 225))
    fade_out((125, 0, 225))
    fade_in((8, 84, 13))
    for i in range(3):
        chase((8, 84, 13))
    fade_out((125, 0, 225))
    time.sleep(0.5)
    for i in range(10):
        sparkle((0,0,0), (255, 0, 0), 0.05, 15)
