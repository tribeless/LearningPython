def main():
    x,y = 1234,123

    if (x > y):
        sl = "x is greater than y"
    elif (x<y):
        sl = "x is less than y"
    else:
        sl="x is equal to y"

    print(sl)
    #ternary replacement in python
    st = "x is greater than y" if(x>y) else "x is less than y or equal to y"
    print(st)
if __name__ == "__main__":
    main()
