from collections import Counter
from functools import reduce

with open('input.txt', 'r') as inputFile:
    lines = inputFile.readlines()
    checksum = { 2: 0, 3: 0}
    for line in lines:
        c = Counter(line).most_common(2)
        values = set([result[1] for result in c])
        for num in values:
            if num in checksum:
                checksum[num] += 1
    print(reduce((lambda x, y: x * y), list(checksum.values())))
