dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'a':10, 'b': 11, 'c': 12, 'd': 13, 'f': 15}
print("Enter hex number")
a = input()

res = 0

for i, s in enumerate(a):
    res += dic[s] * (16**(len(a) - i - 1))

print(res)