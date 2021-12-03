import time
import grovepi
import pickle

import os.path
from os import path

# Connect the Grove Sound Sensor to analog port A0
# SIG,NC,VCC,GND
sound_sensor = 0

grovepi.pinMode(sound_sensor,"INPUT")

samples = 0

for x in range(200):
 # Read the sound level
    sensor_value = grovepi.analogRead(sound_sensor)
    samples = samples + sensor_value
    #print("sensor_value = %d" %sensor_value)
    time.sleep(.1)

samples = samples/200
print("Average after 200 samples in 20 seconds = %d" %samples)

pickle.dump(samples, open("sound.pickle", "wb"))
