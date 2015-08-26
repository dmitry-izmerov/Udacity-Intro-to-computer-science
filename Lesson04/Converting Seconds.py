__author__ = 'demi'


# Write a procedure, convert_seconds, which takes as input a non-negative
# number of seconds and returns a string of the form
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes,
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(seconds):
    res = ''
    mins = 0
    hours = 0
    if(seconds > 0):
        mins = int(seconds/60)
        seconds = seconds - (mins*60)
        hours = int(mins/60)
        mins = mins - (hours*60)

    if hours == 1:
        res += '%d hour' % hours
    else:
        res += '%d hours' % hours

    if mins == 1:
        res += ', '
        res += '%d minute' % mins
    else:
        res += ', '
        res += '%d minutes' % mins

    if seconds == 1:
        res += ', '
        if isinstance(seconds, int):
            res += '%d second' % seconds
        else:
            res += '%.1f second' % seconds
    else:
        res += ', '
        if isinstance(seconds, int):
            res += '%d seconds' % seconds
        else:
            res += '%.1f seconds' % seconds

    return res

print(convert_seconds(3600))

print(convert_seconds(3661))
#>>> 1 hour, 1 minute, 1 second

print(convert_seconds(7325))
#>>> 2 hours, 2 minutes, 5 seconds

print(convert_seconds(7261.7))
#>>> 2 hours, 1 minute, 1.7 seconds