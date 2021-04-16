def mysum(*args):
    summ = 0
    for arg in args:
        summ += arg
    return summ

print(mysum(1,2,3))