# Improved demo/test program to be more Micro:bit user friendly...

from microbit import *
import time
import DS1302

# Create an instance of a DS1302 class object and call it 'ds'.
ds = DS1302.DS1302(clk=pin13, dio=pin14, cs=pin15)

#Setup date/time one time only...
#ds.DateTime([2018, 3, 9, 4, 23, 0, 1])  # March 3, 2018 at 11:00:01 pm.

while True:
    # Show we are (still) alive...
    display.show(Image.HAPPY)
    time.sleep_ms(2000)
    
    # Use DS1302 to display current date in MM/DD/YYYY format on 5x5 LED matrix display
    display.scroll("Date: ")
    display.scroll(ds.Month())
    display.scroll('/')
    display.scroll(ds.Day())
    display.scroll('/')
    display.scroll(ds.Year())
    time.sleep_ms(1000)
    
    # Use DS1302 to display current time in HH:MM:SS format on 5x5 LED matrix display
    display.scroll("Time: ")
    display.scroll(ds.Hour())
    display.scroll(':')
    display.scroll(ds.Minute())
    display.scroll(':')
    display.scroll(ds.Second())
    time.sleep_ms(10000)          # Wait 10 seconds & repeat...
