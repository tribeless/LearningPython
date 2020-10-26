from datetime import datetime

#formating date to sth individual
# %a=weekday %b=month %Y=year %d=day of month
def main():
    today = datetime.now()
    print(today.strftime("%a,%b,%Y,%d"))

#for locale time,timedate and date:
# %x= local date %X=locale time %c=locale date/time
    print(today.strftime("%x,%X,%c"))

#%I/%H=12/24 %S=second %M=minute %p=pm/am
    print(today.strftime("%I,%H,%S,%M,%p"))
if __name__ == "__main__":
    main()
