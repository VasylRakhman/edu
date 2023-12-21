import re

total_sum = 0
filename = 'data/txt/regex_sum.txt'
with open(filename) as fh:

    for line in fh:
        total_sum += sum([int(number) for number in re.findall('[0-9]+',line)])

print(total_sum)
