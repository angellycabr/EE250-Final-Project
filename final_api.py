import requests
import sys
import time

sys.path.append('/home/pi/Dexter/GrovePi/Software/Python')

import grovepi
import grove_rgb_lcd as lcd

# Modules for my apps
import music  # TODO: Create my_app.py using another API, following the examples as a template

LCD_LINE_LEN = 16

lcd.setRGB(0, 128, 0)

# Installed Apps!
APPS = [
    # TODO: Add your new app here
    music.MUSIC_APP,
]

# Cache to store values so we save time and don't abuse the APIs
CACHE = [''] * len(APPS)
for i in range(len(APPS)):
    # Includes a two space offset so that the scrolling works better
    CACHE[i] = '  ' + APPS[i]['init']()

app = 0     # Active app
ind = 0     # Output index

while True:
    try:
        time.sleep(0.1)

        # Display app name
        lcd.setText_norefresh(APPS[app]['name'])

        # Scroll output
        lcd.setText_norefresh('\n' + CACHE[app][ind:ind+LCD_LINE_LEN])
        # TODO: Make the output scroll across the screen (should take 1-2 lines of code)
        ind = (ind + 1)%(len(CACHE[app]))


    except KeyboardInterrupt:
        # Gracefully shutdown on Ctrl-C
        lcd.setText('')
        lcd.setRGB(0, 0, 0)

        break

    except IOError as ioe:
        if str(ioe) == '121':
            # Retry after LCD error
            time.sleep(0.25)

        else:
            raise
