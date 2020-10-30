from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

Red = (225,0,0)
Yellow = (225,225,0)
Green = (0,225,0)
Cyan = (0,225,225)
Blue = (0,0,225)
Mangenta = (225,0,225)
Black = (0,0,0)
White = (225,225,225)

sense.show_letter("M", Red)
sleep(.5)
sense.show_letter("U", Yellow)
sleep(.5)
sense.show_letter("R", Green)
sleep(.5)
sense.show_letter("T", Cyan)
sleep(.5)
sense.show_letter("A", Blue)
sleep(.5)
sense.show_letter("G", Mangenta)
sleep(.5)
sense.show_letter("H", White)
sleep(.5)

