__author__ = 'demi'


# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).

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
            res += '%f second' % seconds
    else:
        res += ', '
        if isinstance(seconds, int):
            res += '%d seconds' % seconds
        else:
            res += '%f seconds' % seconds

    return res


def download_time(file_size, size_units, bandwidth, bw_units):
    fileBytes = getBytes(file_size, size_units)
    bwBytes = getBytes(bandwidth, bw_units)
    res = convert_seconds(float(fileBytes) / bwBytes)
    return res


def getBytes(size, units):
    res = size
    if units == 'kB':
        res *= 2 ** 10 * 8
    elif units == 'kb':
        res *= 2 ** 10
    elif units == 'MB':
        res *= 2 ** 20 * 8
    elif units == 'Mb':
        res *= 2 ** 20
    elif units == 'GB':
        res *= 2 ** 30 * 8
    elif units == 'Gb':
        res *= 2 ** 30
    elif units == 'TB':
        res *= 2 ** 40 * 8
    elif units == 'Tb':
        res *= 2 ** 40
    return res

print(download_time(1,'kB',3,'MB'))

print(download_time(11,'GB', 5, 'MB'))

print(download_time(1024, 'kB', 1, 'MB'))
#>>> 0 hours, 0 minutes, 1 second

print(download_time(1024, 'kB', 1, 'Mb'))
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print(download_time(13, 'GB', 5.6, 'MB'))
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print(download_time(13, 'GB', 5.6, 'Mb'))
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print(download_time(10, 'MB', 2, 'kB'))
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print(download_time(10, 'MB', 2, 'kb'))
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable


