


def run_timing():
    a = []
    print("Enter 10 km run time:")
    while True:
        cur_res = input()
        if (cur_res == ""):
            break
        else:
            try:
                a += [float(cur_res)]
            except:
                print("Error!")
    print(a)
    return (sum(a)/len(a))

print(run_timing())