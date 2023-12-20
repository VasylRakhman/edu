fname = 'mbox-short.txt'
emails_list = list()

with open(fname) as fh:

    count = 0
    for line in fh:
        buff_line = line.rstrip().split()
        if len(buff_line) < 1: continue
        elif buff_line[0] == 'From':
            count += 1 
            emails_list.append(buff_line[1])



for email in emails_list:
    print(email)
print("There were", count, "lines in the file with From as the first word")
