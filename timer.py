from time import strftime, sleep
from datetime import datetime, timedelta
import re
from playsound import playsound



class Clock:

    def __init__(self):
        pass

    def time():
        return strftime("%H:%M:%S")


def display(clock):
    print(clock.time())
    pass


def timer(clock, in_time):
    curr_date = datetime.now()
    alert_time = curr_date + timedelta(minutes=in_time)
    alert_time = alert_time.strftime("%H:%M:%S")
    print("Timer set for " + alert_time)
    while True:
        sleep(60)
        if clock.time() == alert_time:
            print("TIME'S UP\n")
            playsound("file://C:/Users/mpeixoto/Timer/tuturu.mp3")
            break
        else:
            curr_date = datetime.now()
            curr_time = curr_date.strftime("%H:%M:%S")
            print(curr_time)
            continue
    pass


def main():
    clock = Clock
    while True:
        choice = input("Enter 1 to set a timer or 2 to quit:\n")
        if choice == "1":
            in_time = input("Set timer to go off in how many minutes (99 max)?\n")
            if re.match("^\d{1,2}$", in_time):
                timer(clock, int(in_time))
                pass
            else:
                print("Invalid input.")
                main()
                pass
            break
        elif choice == "2":
            print("Goodbye.")
            quit()
        else:
            print("Invalid input, try again.")
            continue
    main()
    pass


main()