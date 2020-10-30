from sense_hat import SenseHat

sense = SenseHat()

blue = (0,0,225)
yellow = (225,225,0)

sense.show_message("Please Help Me!", text_colour=blue, back_colour=yellow, scroll_speed=0.1)