from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while True:
    # take reading from all the three sensors
    temp = sense.get_temperature() 
    press = sense.get_pressure()
    hum = sense.get_humidity()
    
    # round the values to one decimal place
    temp = round(temp,1)
    press = round(press,1)
    hum = round(hum,1)
    
    # create a message
    message = "temp: " + str(temp) + "press: " + str(press) + "hum: " + str(hum)
    
    # Display message
    sense.show_message(message, scroll_speed = 0.075)