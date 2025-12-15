with open('input.txt') as file:
   inp = file.read().splitlines() 
inp = [[int(x) for x in i.split(',')] for i in inp]

import numpy
import itertools as it

# part 1

dist = lambda p, q: (p[0]-q[0])**2 + (p[1]-q[1])**2 + (p[2]-q[2])**2

matrix = numpy.array([[1e11 for j in range(len(inp))] for i in range(len(inp))])

for i in range(len(inp)):
   p = inp[i]
   for j in range(i+1, len(inp)):
      q = inp[j]
      matrix[i][j] = dist(p, q)

circuits = [{i} for i in range(len(inp))]
for x in range(1000):
   pos = matrix.argmin()
   junction1, junction2 = int(pos/len(inp)), int(pos%len(inp))
   matrix[junction1, junction2] = 1e11
   seen = [i for i, c in enumerate(circuits) if junction1 in c or junction2 in c]
   if len(seen) == 2:
      c1, c0 = circuits.pop(seen[1]), circuits.pop(seen[0])
      newCircuit = c1.union(c0)
      circuits.append(newCircuit)

sizes = sorted([len(c) for c in circuits])
print(sizes[-1]*sizes[-2]*sizes[-3])

# part 2

matrix = numpy.array([[1e11 for j in range(len(inp))] for i in range(len(inp))])

for i in range(len(inp)):
   p = inp[i]
   for j in range(i+1, len(inp)):
      q = inp[j]
      matrix[i][j] = dist(p, q)

circuits = [{i} for i in range(len(inp))]
while len(circuits) > 1:
   pos = matrix.argmin()
   junction1, junction2 = int(pos/len(inp)), int(pos%len(inp))
   matrix[junction1, junction2] = 1e11
   seen = [i for i, c in enumerate(circuits) if junction1 in c or junction2 in c]
   if len(seen) == 2:
      c1, c0 = circuits.pop(seen[1]), circuits.pop(seen[0])
      newCircuit = c1.union(c0)
      circuits.append(newCircuit)
print(inp[junction1][0] * inp[junction2][0])
