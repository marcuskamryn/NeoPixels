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
        
    """
    Sets a count to 0 then goes into a for loop for np.n times. Then it'll set the neopixels to
    the color parameter. Then the funtion goes into another for loop np.n times where it'll set
    every 3rd neopixel to black so it'll create a chasing effect.
    
    Args:
        color(tuple): The RGB value.
    
    Shows
        The colors being chased to the left.
    
    """
        
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
    """

    """

    
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
    
    """
    
    Args:
        color(tuple):
        speed(double): ... if user does not input a speed it is automatically set to 0.005.
        
    Shows:
        Shows the color fading in
    """
        
def fire(pcolor, color1, color2):
    np.fill(pcolor)
    np.show()
    for i in range(np.n / 2):
        np[random.randint(0, np.n - 1)] = color1
        np[random.randint(0, np.n - 1)] = color2
        np.show()
        time.sleep(random.randint(1,5) / 1000)
        
    """
    Sets the neoPixels to the pcolor. Then goes into a for loop for half of the neopixel's
    length. Inside the for loop, it'll set set a random neopixel with the range for np[0] -
    np[np.n-1] to color1. It will then do the same randomization for color2. It will then show
    and sleep for a very short randomized period of time from 0.001 - 0.005 of a second.
    
    Arg:
        pcolor (tuple): The base color
        color1(tuple): The first random color
        color2(tuple): The second random color
        
    Shows:
        The neopixels will look like fire against another surface.
    
    """
        
def lightning(color):
    for i in range(random.randint(2, 10)):
        time.sleep(random.randint(1,5) / 100)
        np.fill((255, 255, 255))
        np.show()
        time.sleep(random.randint(1,5) / 100)
        np.fill(color)
        np.show()
    time.sleep(2)
    
    """
    Goes into a for loop for a random amount of 2 - 10. Then the function will sleep for a
    randomized time between 0.01 and 0.05. After the sleep period is up the neopixels will flash
    white (255, 255, 255) and sleep for the same randomized time. After that sleep period it
    flashes set the neopixels to color. After the for loop it'll sleep for 2 seconds.
    
    Args:
        color(tuple): The base color of the neopixels
        
    Shows:
        Makes the neopixels looks like it's flashing lightning
    
    """


def sparkle(background, foreground, t, num):
    np.fill(background)
    for i in range(num):
        np[random.randint(0, np.n - 1)] = foreground
        np.show()
        time.sleep(t)
    
    """
    When the function is called, it sets the fill of the neopixels to the background. Then it'll
    go into a loop for num amount of times. In the loop it'll set a random neopixel from np[0] to
     np[np.n-1] to the foreground color. After, it'll show the background with the randomized
    foreground neopixel, then time.sleep() for however long t is and will repeat the process.

    Args:
        background(tuple): The base color
        foreground(tuple): The color that's randomized flashes
        t(double): The amount for sleep inbetween each loop
        num(int): The number of times the loop will run
        
    Shows:
        A sparkling effect with the foreground as the sparkle
    """

        
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
    fade_out((8, 84, 13))
    time.sleep(0.5)
    fade_in((230, 115, 0))
