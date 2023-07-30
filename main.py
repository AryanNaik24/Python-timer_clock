

from playsound import playsound
import time
import os

ClEAR = "\033[2J"
ClEAR_AND_RETURN = "\033[H"

# playsound("alarm.mp3")
def screen_clear():
    _ = os.system('cls')
def alarm(seconds):
    time_elapsed = 0

    print(ClEAR)
    # os.system('cls' if os.name == 'nt' else 'clear')
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        screen_clear()


        time_left = seconds - time_elapsed

        minutes_left = time_left // 60
        seconds_left = time_left % 60
        hours_left = minutes_left // 60

        print(f"Alarm in : {hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}")
    playsound("alarm.mp3")
        # os.system('cls' if os.name == 'nt' else 'clear')
minutes = int (input("how many minutes?"))
seconds = int (input("how many seconds?"))


ttl_seconds = minutes*seconds+seconds



alarm(ttl_seconds)

