__author__ = 'demi'

import string
# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def rotate(str, n):
    res = ''
    for c in str:
        res += shift_n_letters(c, n)
    return res

def shift_n_letters(letter, n):
    if letter == ' ':
        return letter

    lowers = [i for i in string.ascii_lowercase]
    size = len(lowers)
    num = 26
    counter = 0
    for c in lowers:
        if c == letter:
            num = counter
            break
        counter += 1Recursive Factorial
    num += n
    return lowers[num % size]

print(rotate('sarah', 13))
#>>> 'fnenu'
print(rotate('fnenu', 13))
#>>> 'sarah'
print(rotate('dave', 5))
#>>>'ifaj'
print(rotate('ifaj', -5))
#>>>'dave'
print(rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
              "sv rscv kf ivru kyzj"), -17))
#>>> ???