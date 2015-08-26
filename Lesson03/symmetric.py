__author__ = 'demi'


# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(lists):
    if len(lists) == 0:
        return True
    if len(lists) != len(lists[0]):
        return False

    rowCounter1 = 0
    rowCounter2 = 0
    colCounter1 = 0
    colCounter2 = 0
    while rowCounter1 < len(lists):
        while colCounter1 < len(lists[0]):
            if lists[rowCounter1][colCounter1] != lists[rowCounter2][colCounter2]:
                return False
            colCounter1 += 1
            rowCounter2 += 1
        colCounter1 = 0
        rowCounter2 = 0
        rowCounter1 += 1
        colCounter2 += 1
    return True

print(symmetric([[1, 2, 3],
                 [2, 3, 4],
                 [3, 4, 1]]))
#>>> True

print(symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "fish"],
                 ["fish", "fish", "cat"]]))
#>>> True

print(symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "dog"],
                 ["fish", "fish", "cat"]]))
#>>> False

print(symmetric([[1, 2],
                 [2, 1]]))
#>>> True

print(symmetric([[1, 2, 3, 4],
                 [2, 3, 4, 5],
                 [3, 4, 5, 6]]))
#>>> False

print(symmetric([[1, 2, 3],
                 [2, 3, 1]]))
#>>> False