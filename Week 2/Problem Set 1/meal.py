def main():
    time = input("Enter time in HH:MM format: ").strip().lower()
    time_in_hours = convert(time)
    if 7.0 <= time_in_hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_in_hours <= 13.0:
        print("lunch time")
    elif 18.0 <= time_in_hours <= 19.0:
        print("dinner time")



def convert(time):
    try:
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)
    except ValueError:
        return -1
    return hours + (minutes / 60)

if __name__ == "__main__":
    main()
