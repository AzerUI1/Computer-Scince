import time
import sys

def stopwatch():
    print("Stopwatch started. Press Ctrl+C to stop.")
    start_time = time.time()
    seconds = 0
    try:
        while True:
            elapsed_time = int(time.time() - start_time)
            if elapsed_time != seconds:
                seconds = elapsed_time
                sys.stdout.write(f"\rElapsed time: {seconds} seconds")
                sys.stdout.flush()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\nStopwatch stopped at {seconds} seconds.")

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("\nTime's up!")
    print("\a") 

def main():
    print("Welcome to the Timer program! This program will help you measure the time taken for specific tasks or events.")
    print("What type of timer would you like to use? You can choose between a countdown timer or a stopwatch.")
    timer_types = ["countdown", "stopwatch"]
    user_choice = input(f"Please enter your choice ({', '.join(timer_types)}): ").strip().lower()
    if user_choice == timer_types[0]:
        seconds = int(input("Enter the time in seconds: "))
        countdown(seconds)
    elif user_choice == timer_types[1]:
        stopwatch()
    else:
        print("Invalid choice.")
main()