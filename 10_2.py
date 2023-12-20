name = "mbox-short.txt"

hours_count = dict()

with open(name) as fh:
  for line in fh:
    line_buff = line.split()
    if len(line_buff) < 1: continue
    elif line_buff[0] == 'From':
        data = line_buff[5]
        hour = data.split(':')[0]
        hours_count[hour] = hours_count.get(hour, 0) + 1

for k in sorted(hours_count):
    print(k, hours_count[k])
