from datetime import datetime

def log_activity():
    activity = input("Enter your activity: ")

    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("activities.txt", "a") as file:
        file.write(f"{time_now} - {activity}\n")

    print("Activity saved successfully!")

if __name__ == "__main__":
    log_activity()
