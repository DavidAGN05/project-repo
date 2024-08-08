def main():
    x = input("What time is it? ")
    if 8 >= convert(x) >= 7:
        print("breakfast time")
    elif 13 >= convert(x) >= 12:
        print("lunch time")
    elif 19 >= convert(x) >= 18:
        print("dinner time")
    else:
        print("Somethings off")

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes) / 60
    time = hours + minutes
    return time

if __name__ == "__main__":
    main()