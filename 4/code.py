with open('input.txt') as file:
   inp = file.read().splitlines() 

# part 1

out = 0
I = len(inp)
J = len(inp[0])
for i in range(I):
   for j in range(J):
      neighbours = [range(max(0,i-1), min(i+2,I)), range(max(0,j-1), min(j+2,J))]
      if inp[i][j] == '@':
         rolls = 0
         for n in neighbours[0]:
            for m in neighbours[1]:
               rolls += (inp[n][m] == '@')
         out += (rolls < 5)
print(out)

# part 2

inp = [[x for x in i] for i in inp]
out = 0
aRollWasRemoved = 1
while aRollWasRemoved:
   aRollWasRemoved = 0
   I = len(inp)
   J = len(inp[0])
   for i in range(I):
      for j in range(J):
         neighbours = [range(max(0,i-1), min(i+2,I)), range(max(0,j-1), min(j+2,J))]
         if inp[i][j] == '@':
            rolls = 0
            for n in neighbours[0]:
               for m in neighbours[1]:
                  rolls += (inp[n][m] == '@')
            if rolls < 5:
               inp[i][j] = '.'
               out += 1
               aRollWasRemoved = 1
print(out)
