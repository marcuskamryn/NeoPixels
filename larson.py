import board
from neopixel import NeoPixel
import time

np = NeoPixel(board.D2, 30, auto_write = False, brightness = 0.3)

def bounce(background, foreground, num):
    direction = 1
    i = 0
    bc = 0
    dim =  [int(c * 0.8) for c in foreground]
    dimmer = [int(c * 0.2) for c in foreground]
    
    
    while bc < num:
        np.fill(background)
        np[i] = foreground
        if( i - 2 >= 0):
            np[i - 2] = dimmer
            
        if(i - 1 >= 0):
            np[i - 1] = dim
            
        if(i + 2 <= np.n - 1):
            np[i + 2] = dimmer
            
        if(i + 1 <= np.n - 1):
            np[i +1] = dim
        
        time.sleep(0.1)
        np.show()
        
        i += direction
        if(i >= (np.n - 1) or i <= 0):
            direction *= -1
            bc += 1
    

while True:
    bounce((0, 0, 0), (255, 0, 0), 4)
