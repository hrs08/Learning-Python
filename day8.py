# Python alarm clock
import datetime
import time


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time.strftime('%H:%M:%S')}")

    while True:
        current_time = datetime.datetime.now()

        print(current_time.strftime("%H:%M:%S"))
        if current_time >= alarm_time:
            print("Wakey, wakey!!")
            break

        time.sleep(1)


if __name__ == "__main__":
    alarm_input = input("Enter the alarm time (HH:MM or HH:MM:SS): ")

    try:
        if len(alarm_input) == 5:
            alarm_time_only = datetime.datetime.strptime(
                alarm_input, "%H:%M"
            ).time()
        else:
            alarm_time_only = datetime.datetime.strptime(
                alarm_input, "%H:%M:%S"
            ).time()

    except ValueError:
        print("Invalid time format.")
        print("Please use HH:MM or HH:MM:SS")
        exit()

    now = datetime.datetime.now()

    alarm_time = datetime.datetime.combine(
        now.date(),
        alarm_time_only
    )
	
    if alarm_time <= now:
        print("That time has already passed today.")
    else:
        set_alarm(alarm_time)
