import re

__author__ = 'demi'


# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags.
# You may assume the input does not include any unclosed tags, that is,
# there will be no '<' without a following '>'.

def remove_tags(s):
    res = []
    l = parse_tags(s)
    for s in l:
        s = s.strip()
        if len(s):
            res += s.split(' ')
    return res

def parse_tags(s):
    if s.find('<') == -1:
        return [s]
    else:
        res = []
        pattern = r'([^<>]*)(?:</?\w+[^>]*>(.+?)</?\w+[^>]*>|<.*?/?>)([^<>]*)'
        match = re.search(pattern, s, re.DOTALL)
        while match:
            matched = match.group(0)
            before = match.group(1)
            content = match.group(2)
            after = match.group(3)
            s = s[len(matched):]
            if before and len(before):
                res.append(before)
            if content:
                res += parse_tags(content)
            if after and len(after):
                res.append(after)
            match = re.search(pattern, s, re.DOTALL)
        return res


def remove_tags_from_answer(s):
    start = s.find('<')
    while start != -1:
        end = s.find('>', start)
        s = s[:start] + ' ' + s[end + 1:]
        start = s.find('<')
    return s.split()


print(remove_tags("An empty tag<>"))
#>>> ['An', 'empty', 'tag']

print(remove_tags("<start>This line starts and ends with a tag<end>"))
#>>> ['This', 'line', 'starts', 'and', 'ends', 'with', 'a', 'tag']

print(remove_tags("This line ends with a tag<br />"))
#>>> ['This', 'line', 'ends', 'with', 'a', 'tag']

print(remove_tags("<br />This line starts with a tag"))
#>>> ['This', 'line', 'starts', 'with', 'a', 'tag']

print(remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>'''))
#>>> ['Title','This','is','a','link','.']

print(remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>'''))
#>>> ['Hello','World!']

print(remove_tags("<hello><goodbye>"))
#>>> []

print(remove_tags("This is plain text."))
#>>> ['This', 'is', 'plain', 'text.']

