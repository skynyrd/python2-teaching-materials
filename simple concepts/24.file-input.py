def process(line):
    print line

with open('./file-sample.txt') as f:
    for line in f:
        process(line)
