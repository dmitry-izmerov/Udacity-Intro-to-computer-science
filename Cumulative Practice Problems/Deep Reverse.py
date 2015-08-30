__author__ = 'demi'


# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list,
# and returns a new list that is the deep reverse of the input list.
# This means it reverses all the elements in the list, and if any
# of those elements are lists themselves, reverses all the elements
# in the inner list, all the way down.

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)

def deep_reverse(l):
    if is_list(l):
        length = len(l)
        newlist = [i for i in l]
        i = 0
        half = int(length/2)
        while (i < half):
            first = l[i]
            last = l[length - i - 1]
            first = deep_reverse(first)
            last = deep_reverse(last)
            newlist[i] = last
            newlist[length - i - 1] = first
            i += 1

        if length % 2 != 0 and is_list(newlist[half]):
            newlist[half] = deep_reverse(newlist[half])
        return newlist
    return l

#For example,
p = [1, [2, 3], [4, 5]]
print(deep_reverse(p))
#>>> [[5, 4], [3, 2], 1]
# print(p)

# p = [1, [2, 3, [4, [5, 6]]]]
# print(deep_reverse(p))
# #>>> [[[[6, 5], 4], 3, 2], 1]
# print(p)
# #>>> [1, [2, 3, [4, [5, 6]]]]
#
# q =  [1, [2,3], 4, [5,6]]
# print(deep_reverse(q))
# #>>> [ [6,5], 4, [3, 2], 1]
# print(q)
#>>> [1, [2,3], 4, [5,6]]
