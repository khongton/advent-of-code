import itertools

f = open('input.txt')
lines = f.readlines()
f.close()

sum = 0
for line in lines:
    sum += int(line)
print(sum)

sums = {}
curSum = 0
for line in itertools.cycle(lines):
    curSum += int(line);
    if curSum in sums:
        print(curSum)
        break
    else:
        sums[curSum] = 1
