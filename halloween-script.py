from sense_hat import SenseHat
from time import *
import datetime

now = datetime.datetime.now()
sense = SenseHat()
month = now.strftime('%m')

while(month == '10'):
    now = datetime.datetime.now()
    month = now.strftime('%m')
    a = 0
    sense.clear((a, a, a))
    sleep(1)
    while (a < 255):
        a = a + 51
        sense.clear((a, a, a))
        sleep(1)
    sense.clear((0, 0, 0))
    r = 0
    sleep(1)
    while (r < 255):
        r = r + 51
        sense.clear((r, 0, 0))
        sleep(1)
    sense.clear((0, 0, 0))
    g = 0
    sleep(1)
    while (g < 255):
        g = g + 51
        sense.clear((0, g, 0))
        sleep(1)
    sense.clear((0, 0, 0))
    b = 0
    sleep(1)
    while (b < 255):
        b = b + 51
        sense.clear((0, 0, b))
        sleep(1)
