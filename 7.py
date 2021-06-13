a = ['a', 'e', 'i', 'o', 'u']

def ubbi_dubbi(word):
    res = ''
    for letter in word:
        if letter in a:
            print('found')
            letter = 'ub' + letter
        res += letter
    return res

print(ubbi_dubbi('asdacx'))