with open('input.txt') as file:
   inp = file.read().splitlines() 

# part 1

out = 0
beams = [inp[0].find('S')]
for i in range(1, len(inp)):
   if i%2 == 0:
      splits = [u for u, x in enumerate(inp[i]) if x=='^' and u in beams]
      out += len(splits)
      beams = set(s-1 for s in splits).union(set(s+1 for s in splits)).union(set(b for b in beams if not(b in splits)))
print(out)



# part 2

seenIn = []
seenOut = []
def timeSplit(i, j):
   if i == 140:
      return 1
   elif (i, j) in seenIn:
      return seenOut[seenIn.index((i, j))]
   else:
      if inp[i+2][j] == '^':
         out = timeSplit(i+2, j-1) + timeSplit(i+2, j+1)
      else:
         out = timeSplit(i+2, j)
      seenIn.append((i, j))
      seenOut.append(out)
      return out

timeSplit(0, inp[0].find('S'))