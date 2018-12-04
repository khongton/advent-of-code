from pprint import pprint
dims = 1000

grid = [[0 for height in range(dims)] for width in range(dims)]
with open('input.txt', 'r') as f:
  lines = f.readlines()
  for line in lines:
    data = line.split()
    claimID = data[0]
    fabricDelims = list(map(lambda x: int(x), data[2][:-1].split(',')))
    fabricArea = list(map(lambda x: int(x), data[3].split('x')))

    overlapTriggered = False
    for width in range(fabricDelims[1], fabricDelims[1] + fabricArea[1]):
      for x in range(fabricDelims[0], fabricDelims[0] + fabricArea[0]):
        grid[width][x] += 1

  result = filter(lambda x: x > 1, [overlap for row in grid for overlap in row])
  print(len(list(result)))