#loops in python resolve to two: while and for loops for simplicity

def main():

    x = 0

    while(x<=10):
        print(x)
        x+=1

    for x in range(5,10):
        print(x)

    daysOfWeek = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
    for x in daysOfWeek:
        print(x)

    for x in range(0,10):
        if(x%2!=0):continue
        print(x)

#enumerate provides us with the index of a particular element
    daysOfWeek = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
    for i,x in enumerate(daysOfWeek):
        if(i>=5):break
        print(i,x)
        
if __name__ ==  "__main__":
    main()
   
