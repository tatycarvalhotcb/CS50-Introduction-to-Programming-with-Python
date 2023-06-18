def main():
    time = input("What time is it? ").strip() #ask the user for the time
    convert_time = convert(time) #set the convert from the input in the variable convert_time
    if convert_time >= 7 and convert_time <= 8: #check the times and output the right meal, no output if the time it's out of the main 3 meal times
        print("breakfast time")
    elif convert_time >= 12 and convert_time <= 13:
        print("lunch time")
    elif convert_time >= 18 and convert_time <= 19:
        print("dinner time")


#function do convert the input time in a float
def convert(time):
    hours, minutes = time.split(":") #separate the hours from minutes and set in variables
    hours = int(hours) #hours as an int
    minutes = int(minutes) #hours as an int
    return float(hours + minutes / 60) #return the time as a float


if __name__ == "__main__":
    main()


'''
def main():
    time = input("What time is it? ").strip()
    return convert(time)

def convert(time):
    hours, minutes, period = time.split(":")[0], time.split(":")[1].split()[0], time.split()[-1]
    hours = int(hours)
    minutes = 0 <= int(minutes) < 60
    am_period = "a.m." in period
    pm_period = "p.m." in period

    if hours == 7 and minutes is True or hours == 7 and minutes is True and am_period is True:
        print("breakfast time")
    elif hours == 12 and minutes is True or hours == 12 and minutes is True and pm_period is True:
        print("lunch time")
    elif hours == 18 and minutes is True or hours == 6 and minutes is True and pm_period is True:
        print("dinner time")

if __name__ == "__main__":
    main()
'''