#works but need to find out how to add sound

import datetime
from playsound import playsound
alarmhour = int(input("Enter Hour: "))
alarmins = int(input("Enter Minutes: "))
alarmAm = input("AM / PM: ").upper()

if alarmAm == "pm".upper():
    alarmhour += 12

while True:
    if alarmhour == datetime.datetime.now().hour and alarmins == datetime.datetime.now().minute:
        playsound('/Users/chnguyen/Downloads/dsa.mp3')
        print("It's time mother f'er")
        break

