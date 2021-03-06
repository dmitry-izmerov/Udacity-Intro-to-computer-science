__author__ = 'demi'


# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.

def longest_repetition(l):
    max_counter = 0
    max_c = None
    counter = 0
    prev = None
    for i in l:
        if i == prev:
            counter += 1
        else:
            counter = 1
            prev = i
        if counter > max_counter:
            max_c = prev
            max_counter = counter
    return max_c



#For example,
print(longest_repetition([2, 2, 3, 3, 3]))
# 3

print(longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]))
# 3

print(longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']))
# b

print(longest_repetition([1, 2, 3, 4, 5]))
# 1

print(longest_repetition([]))
# None

