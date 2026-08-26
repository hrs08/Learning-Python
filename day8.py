#python alarm clock
import datetime
import time

def set_alarm(alarm_time):
	print(f"Alarm set for {alarm_time}")
	#use a sound file if want
	is_running = True

	while is_running:
		current_time = datetime.datetime.now().strftime("%H:%M:%S")
		print(current_time)

		if current_time == alarm_time:
			print("Wakey , wakey !!")

			is_running = False
		

		time.sleep(1)
		
if __name__ == "__main__":
	alarm_time = input("Enter the alarm time (HH:MM:SS) : ")
	current_time = datetime.datetime.now().strftime("%H:%M:%S")
	if alarm_time < current_time:
		print("Wrong time entered")
	else:
		set_alarm(alarm_time)
