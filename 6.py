
def pig_latin(word):
    

    vowel = ['a', 'e', 'i', 'o', 'u']

    if word[0] in vowel:
        return word + 'way'
    
    return word[1::] + word[0] + 'ay'


print("Input string:")

str_inp = input()

str_spl = str_inp.split()

res = list(map(pig_latin, str_spl))

print(' '.join(res))