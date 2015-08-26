__author__ = 'demi'

import string
# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    lowers = [i for i in string.ascii_lowercase]
    size = len(lowers)
    num = 0
    counter = 0
    for c in lowers:
        if c == letter:
            num = counter
            break
        counter += 1
    num += n
    return lowers[num % size]


print(shift_n_letters('s', 1))
#>>> t
print(shift_n_letters('s', 2))
#>>> u
print(shift_n_letters('s', 10))
#>>> c
print(shift_n_letters('s', -10))
#>>> i