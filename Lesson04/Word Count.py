__author__ = 'demi'


# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.

def count_words(str):
    count = 0
    for s in str.split(' '):
        if len(s) > 0:
            count += 1
    return count

passage =("The number of orderings of the 52 cards in a deck of cards "
"is so great that if every one of the almost 7 billion people alive "
"today dealt one ordering of the cards per second, it would take "
"2.5 * 10**40 times the age of the universe to order the cards in every "
"possible way.")
print(count_words(passage))
print(count_words(""))
print(count_words("As Professor Evans would say, 'Stay Udacious!'"))
#>>>56

