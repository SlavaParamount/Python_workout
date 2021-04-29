
def pig_latin():
    print("Input word:")

    a = input()

    vowel = ['a', 'e', 'i', 'o', 'u']

    if a[0] in vowel:
        return a + 'way'
    
    return a[1::] + a[0] + 'ay'

print(pig_latin())