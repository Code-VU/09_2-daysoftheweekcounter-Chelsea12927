def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")

    daycount = dict()

    with open(file_name) as file:
        for line in file:
            if line.startswith("From "):
                linebrokenout = line.split()
                day = linebrokenout[2]
                daycount[day] = daycount.get(day,0) + 1
        print(daycount)




## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
