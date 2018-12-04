import itertools

f = open('input.txt')
lines = f.readlines()
f.close()

with open('input.txt', 'r') as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        sum += int(line)
    print(sum)

    sums = {}
    curSum = 0
    for line in itertools.cycle(lines):
        curSum += int(line)w
        if curSum in sums:
            print(curSum)
            break
        else:
            sums[curSum] = 1