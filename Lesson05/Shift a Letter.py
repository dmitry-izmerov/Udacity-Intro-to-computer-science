__author__ = 'demi'

import string

# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a'
# following 'z'.

def shift(letter):
    lowers = [i for i in string.ascii_lowercase]
    n = len(lowers)
    num = 0
    counter = 0
    for c in lowers:
        if c == letter:
            num = counter
            break
        counter += 1
    num += 1
    return lowers[num % n]

print(shift('a'))
#>>> b
print(shift('n'))
#>>> o
print(shift('z'))
#>>> a