filename = "romeo.txt"
lst = list()

with open(filename) as fh:
    for line in fh:

        buff_list = line.rstrip().split()
        for word in buff_list:
            if word not in lst:
                lst.append(word)
lst.sort()
print(lst)
