#funcs

def func1(a,b=7):
    result = 1
    for x in range(b):
        result = result*a
    return result

def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(func1(32,2))
print(multi_add(2,3,4,5,6,7,8,9))