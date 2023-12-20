filename = 'mbox-short.txt'

sender_counter = dict()
with open(filename) as fh:
    for line in fh:
        buff = line.rstrip().split()
        if len(buff) < 1: continue
        if buff[0] == 'From':
            sender_counter[buff[1]] = sender_counter.get(buff[1], 0) + 1
max_val = 0
max_key = None
for k, v in sender_counter.items():
    if v > max_val:
        max_key = k
        max_val = v
print(max_key,sender_counter[max_key])
