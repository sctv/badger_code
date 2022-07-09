import board
import terminalio
import displayio
import vectorio
import adafruit_sht4x
import time
from adafruit_display_text import label

"""
An example of how to show text on the Badger 2040's
screen using the built-in DisplayIO object with the SHT40 temperature/humidy sensor.
"""

i2c = board.I2C()  # uses board.SCL and board.SDA
sht = adafruit_sht4x.SHT4x(i2c)
print("Found SHT4x with serial number", hex(sht.serial_number))

sht.mode = adafruit_sht4x.Mode.NOHEAT_LOWPRECISION
# Can also set the mode to enable heater for condensing environments 
# sht.mode = adafruit_sht4x.Mode.LOWHEAT_100MS
print("Current mode is: ", adafruit_sht4x.Mode.string[sht.mode])
temperature, relative_humidity = sht.measurements
print("Temperature: %0.1f C" % temperature)
print("Humidity: %0.1f %%" % relative_humidity)
print("initiation start")
display = board.DISPLAY

# Set text, font, and color
temp = "Temp:"
temp_val = "20C" #dummy value
humid = "Humid: "
humid_val= "60%" #dummy value 
font = terminalio.FONT
color = 0x000000 

# Set the palette for the background color
palette = displayio.Palette(1)
palette[0] = 0xFFFFFF #black

# Add a background rectangle
rectangle = vectorio.Rectangle(pixel_shader=palette, width=display.width + 1, height=display.height, x=0, y=0)

# Create the temp and humid labels
temp_label = label.Label(font, text=temp, color=color, scale=3)
temp_val = label.Label(font, text=str(temperature), color=color, scale=3)
humid_label = label.Label(font, text=humid, color=color, scale=3)
humid_val = label.Label(font, text=str(relative_humidity), color=color, scale=3)

# Set the label locations
temp_label.x = 20
temp_label.y = 45
temp_val.x = 140
temp_val.y = 45

humid_label.x = 20
humid_label.y = 90
humid_val.x = 140
humid_val.y = 90

# Create the display group and append objects to it
group = displayio.Group()
group.append(rectangle)
group.append(temp_label)
group.append(temp_val)

group.append(humid_label)
group.append(humid_val)


# Show the group and refresh the screen to see the result
#display.show(group)
#display.refresh()

# Loop forever so you can enjoy your message


#Show the group and refresh the screen to see the result
while True:
    temperature, relative_humidity = sht.measurements
    print("Temperature: %0.1f C" % temperature)
    print("Humidity: %0.1f %%" % relative_humidity)
    print("")
    # Add a background rectangle
    rectangle = vectorio.Rectangle(pixel_shader=palette, width=display.width + 1, height=display.height, x=0, y=0)

# Create the temp and humid labels
    temp_label = label.Label(font, text=temp, color=color, scale=3)
    temp_val = label.Label(font, text=str('%.1f' % temperature)+" C", color=color, scale=3)
    humid_label = label.Label(font, text=humid, color=color, scale=3)
    humid_val = label.Label(font, text=str('%.d' % relative_humidity)+" %", color=color, scale=3)

# Set the label locations
#Temperature label locations 
    temp_label.x = 20
    temp_label.y = 45
    temp_val.x = 140
    temp_val.y = 45

#Humidity label locations 
    humid_label.x = 20
    humid_label.y = 90
    humid_val.x = 140
    humid_val.y = 90

# Create the display group and append objects to it
    group = displayio.Group()
    group.append(rectangle)
    group.append(temp_label)
    group.append(temp_val)
    group.append(humid_label)
    group.append(humid_val)
    display.show(group)
    display.refresh()
    time.sleep(10) #sleep for 10 seconds
    
    

