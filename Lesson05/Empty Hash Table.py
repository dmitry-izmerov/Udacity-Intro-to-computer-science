__author__ = 'demi'


# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    res = []
    for i in range(nbuckets):
        res.append([])
    return res

print(make_hashtable(5))
