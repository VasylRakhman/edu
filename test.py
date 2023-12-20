fname = 'mbox-short.txt'
counter = 0
sum_confidence = 0
with open(fname) as fh:
# Use the file name mbox-short.txt as the file name
    for line in fh:
        if line.startswith("X-DSPAM-Confidence:"):
            counter += 1
            confidence_index = line.find('0')
            sum_confidence += float(line[confidence_index:])
    avg = sum_confidence / counter
    print(avg)
