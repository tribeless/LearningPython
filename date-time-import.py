from datetime import date
from datetime import time
from datetime import datetime

def main():
    #date class
    today = date.today()
    print(today)

    #date class individual components
    print("Date components are:", today.day,today.month,today.year)

    #weekday number, remember that 0-Monday 6-Sunday unlike cron where 0-Sunday
    print("Todays weekday number is:",today.weekday())

    #lets try assign these weekday numbers to an array of weekdays,lets see:
    daysOfWeek = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
    counter = today.weekday()

    for index,day in enumerate(daysOfWeek):
        if(index==counter):
            print(day, "and weekday number is:" ,counter)
            counter+=1

    #lets get the whole time and date together

    today = datetime.now()
    print(today)

    #lets get the time portion only
    today = datetime.now()
    print(datetime.time(today))

if __name__ == "__main__":
    main()