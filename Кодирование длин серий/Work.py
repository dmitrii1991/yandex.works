import re
s = input()
number = r'([A-Z]\d*)'
length = 0

while len(s) >= 1:
    A = False
    a = re.search(number, s)
    if len(a.group()) > 1:
        length += int(a.group()[1:])
    else:
        length += 1
    _, i = a.span()
    s = s[i:]
print(length)
