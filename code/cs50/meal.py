def main():
    time = input("What time is it? ")
    final = convert(time)
    if final >= 7 and final <= 8:
        print("breakfast time")
    elif final >= 12 and final <= 13:
        print("lunch time")
    elif final >= 18 and final <= 19:
        print("dinner time")
    
def convert(time):
    hours, minutes = time.split(":")
    hrs = float(hours)
    mins = float(minutes) / 60
    return hrs + mins

if __name__ == "__main__":
    main()
