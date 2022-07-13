import random

def func():
    print("hello world")



    x = random.randint(0,1)
    if x == 1:
        print('hey')
    else:
        print('no entry')

    return x

def func2():

    integer = 10

    if integer % 2 == 0:
        integer += 1

    return integer