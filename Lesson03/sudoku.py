__author__ = 'demi'

# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

def check_sudoku(lists):

    if not has_correct_digits(lists):
        return False

    nums = {}
    for i in range(1, 10):
        nums[i] = 0
    # check rows
    for l in lists:
        for i in l:
            if i not in nums:
                return False
            nums[i] += 1
            if nums[i] > 1:
                return False
        nums = clear_nums(nums)

    # check columns
    j = 0
    while j < len(lists[0]):
        i = 0
        while i < len(lists):
            item = lists[i][j]
            if item not in nums:
                return False
            nums[item] += 1
            if nums[item] > 1:
                return False
            i += 1
        nums = clear_nums(nums)
        j += 1
    return True

def clear_nums(nums):
    for i in nums:
        nums[i] = 0
    return nums

def has_correct_digits(lists):
    size = len(lists[0])
    nums = [i for i in range(1, size+1)]
    for l in lists:
        for n in l:
            if n not in nums:
                return False
    return True

print(check_sudoku(incorrect))
#>>> False

print(check_sudoku(correct))
#>>> True

print(check_sudoku(incorrect2))
#>>> False

print(check_sudoku(incorrect3))
#>>> False

print(check_sudoku(incorrect4))
#>>> False

print(check_sudoku(incorrect5))
#>>> False