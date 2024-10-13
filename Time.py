# timer_lib.py
import time

def timer(hours):
    """Countdown timer function that accepts float for hours."""
    # Convert total hours to total seconds
    total_seconds = int(hours * 3600)
    
    for i in range(total_seconds, -1, -1):
        # Calculate hours, minutes, and seconds remaining
        hour = i // 3600
        remainder = i % 3600
        minute = remainder // 60
        second = remainder % 60

        # Print the current time left in HH:MM:SS format
        print(f"{hour:02}:{minute:02}:{second:02}", end='\r')  # Overwrite the same line for cleaner output
        
        # Sleep for 1 second
        time.sleep(1)

    print("\nTime ended!")
    return "time ended"


# Call the timer function
#timer(x)
print("Time ended!")
