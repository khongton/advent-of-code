from collections import Counter
from functools import reduce
from difflib import SequenceMatcher, ndiff
from operator import itemgetter

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

with open('input.txt', 'r') as f:
    lines = f.readlines()
    workingData = []
    for idx, comparer in enumerate(lines):
        for comparee in lines[idx:]:
            if comparer != comparee:
               workingData.append((comparer, comparee, SequenceMatcher(None, comparer, comparee).ratio()))
    matchingIDs = max(workingData, key=itemgetter(2))

    resultStr = ''
    for x, y in zip(matchingIDs[0], matchingIDs[1]):
        if x == y:
            resultStr += x
    print(resultStr)
