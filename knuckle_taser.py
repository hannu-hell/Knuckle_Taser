''' !!! Disclaimer !!!
This project by no means encourage or promote violence and is solely made for education and entertainment purposes. If you intend to make it please
handle it responsibly as it can produce high voltage and when in contact with the human body can cause severe shocks and possible damage to nervous system if
used for a prolonged amount of time.

When engaged I have allowed for a period of 1 second until next engage.

Hope you like it!

Thanks
'''

import neopixel
from machine import Pin
import time

# Pin definitions for 8-Neopixel
pixPin = 2
pixSize = 8
pix = neopixel.NeoPixel(Pin(pixPin),pixSize)

# Pinouts for the relay module
taser_1 = Pin(3, Pin.OUT)
taser_2 = Pin(4, Pin.OUT)
taser_3 = Pin(5, Pin.OUT)

engage_button = Pin(0, Pin.IN, Pin.PULL_UP)  # red button
intensity_button = Pin(1, Pin.IN, Pin.PULL_UP) # blue button

# Initial Intensity of the Knuckle Taser
intensity_state = "low"

# Light Status
light_status = False


# Color definition for the intesity (mild to strong) 
bright_blue = (3,2,252)
blue = (3,2,252)
light_blue = (42,0,213)
violet = (99, 0, 158)
jam = (161, 1, 93)
cadmium_red = (216, 0, 39)
red = (254, 0, 2)
bright_red = (255, 0, 0)

# Turn off the leds
black = (0, 0, 0)

col_list = [bright_red, bright_blue, blue, light_blue, violet, jam, cadmium_red, red]

pix.fill(black)
pix.write()
time.sleep(0.5)


# Functions
def initial_colors():
    pix[1] = bright_blue
    pix[2] = blue
    pix[3] = light_blue  
    pix[4] = violet
    pix[5] = jam
    pix[6] = cadmium_red
    pix[7] = red
    pix[0] = bright_red
    pix.write()
    
def set_low_power():
    pix.fill(black)
    time.sleep(0.2)
    pix.write()
    for _ in range(2):
        for i in range(8):
            pix[i] = col_list[i-1]
            pix.write()
            time.sleep(0.04)
        pix.fill(black)
        pix.write()
        time.sleep(0.1)
    pix.fill(black)
    pix.write()
    time.sleep(0.1)
    pix[1] = bright_blue
    pix[2] = blue
    pix[3] = light_blue
    pix[4] = violet
    pix.write()
    
def set_mid_power():
    pix.fill(black)
    time.sleep(0.2)
    pix.write()
    for _ in range(2):
        for i in range(8):
            pix[i] = col_list[i-1]
            pix.write()
            time.sleep(0.04)
        pix.fill(black)
        pix.write()
        time.sleep(0.1)
    pix.fill(black)
    pix.write()
    time.sleep(0.1)
    pix[1] = bright_blue
    pix[2] = blue
    pix[3] = light_blue
    pix[4] = violet
    pix[5] = jam 
    pix[6] = cadmium_red
    pix.write()

def set_high_power():
    pix.fill(black)
    time.sleep(0.2)
    pix.write()
    for _ in range(2):
        for i in range(8):
            pix[i] = col_list[i-1]
            pix.write()
            time.sleep(0.04)
        pix.fill(black)
        pix.write()
        time.sleep(0.1)
    pix.fill(black)
    pix.write()
    time.sleep(0.1)
    initial_colors()
    time.sleep(0.1)
    for i in range(2):
        pix.fill(black)
        pix.write()
        time.sleep(0.1)
        initial_colors()
        time.sleep(0.1)
        

def initial_sequence():
    for _ in range(2):
        for i in range(8):
            pix[i] = col_list[i-1]
            pix.write()
            time.sleep(0.05)
        pix.fill(black)
        pix.write()
        time.sleep(0.1)
    for _ in range(2):
        for i in range(8):
            pix[i] = col_list[i-1]
            pix.write()
            time.sleep(0.04)
        pix.fill(black)
        pix.write()
        time.sleep(0.1)
    for _ in range(8):
        for i in range(8):
            pix[i] = col_list[i-1]
            pix.write()
            time.sleep(0.02)
        pix.fill(black)
        pix.write()
        time.sleep(0.1)
    
    initial_colors()
    
    set_low_power()
    
    time.sleep(0.5)
    taser_1.value(1)
    time.sleep(0.3)
    taser_1.value(0)
    taser_2.value(1)
    time.sleep(0.3)
    taser_2.value(0)
    taser_3.value(1)
    time.sleep(0.3)
    taser_3.value(0)
    
    time.sleep(1)
    
    
    

# Program Commence

initial_sequence()
time.sleep(1)

# Variable to rotate intensity state of knuckle taser
selected_int = 0

# Loop sequence
while True:
    if engage_button.value() == 0:
        if intensity_state == "low":
            taser_2.value(1)
            time.sleep(1)
            taser_2.value(0)
        if intensity_state == "medium":
            taser_1.value(1)
            taser_3.value(1)
            time.sleep(1)
            taser_1.value(0)
            taser_3.value(0)
        if intensity_state == "high":
            taser_1.value(1)
            taser_2.value(1)
            taser_3.value(1)
            time.sleep(1)
            taser_1.value(0)
            taser_2.value(0)
            taser_3.value(0)
            
    if intensity_button.value() == 0:
        time.sleep(0.3)
        selected_int+=1
        light_status = True
        
    if selected_int == 1:
        intensity_state = "medium"
        if light_status:
            set_mid_power()
            light_status = False
    if selected_int == 2:
        intensity_state = "high"
        if light_status:
            set_high_power()
            light_status = False
    if selected_int == 3 or selected_int == 0:
        intensity_state = "low"
        selected_int = 0
        if light_status:
            set_low_power()
            light_status = False
        
    time.sleep(0.1)


