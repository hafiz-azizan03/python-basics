#PYTHON Alarm clock

import time  # to update the clock by second
import datetime   #to work with strft, string format time
import pygame # to use soundtrack, make sure to download

def set_alarm(alarm_time):  #(alarm_time) parameter will be in strft format(24hr format)
    print(f"Alarm set for {alarm_time}")
    sound_file="Morning Alarm.mp3" #this can be absolute or relative file path, this is relative
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")  #access datetime module,access the class datetime and use now method. strft sets the format, percentage are format specifiers
        print(current_time)

        if current_time>alarm_time:
            print("Wake up!! ⏰⏰")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running=False

        time.sleep(1)

if __name__ == "__main__":  #we can run this file if we run this main python directly, then we can set the  alarm
    alarm_time = input("Enter the alarm time (HH:MM:SS):")
    set_alarm(alarm_time)  #invoke the function of set alarm and pass in the alarm_time
