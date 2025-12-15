with open('input.txt') as file:
   inp = file.read().splitlines() 

# part 1

oper = inp[4]
star = []
plus = []
for i in range(len(oper)):
   if oper[i] == '*':
      star.append(i)
   elif oper[i] == '+':
      plus.append(i)
both = sorted(star + plus + [len(oper)])

out = 0
for i in range(len(both)-1):
   if both[i] in star:
      calc = 1
      for j in range(4):
         calc *= int(inp[j][both[i]:both[i+1]])
   else:
      calc = 0
      for j in range(4):
         calc += int(inp[j][both[i]:both[i+1]])
   out += calc
print(out)


# part 2

out = 0
for i in range(len(both)-1):
   numbers = [''.join(inp[j][b] for j in range(4)) for b in range(both[i], both[i+1]-1)]
   if both[i] in star:
      calc = 1
      for j in range(len(numbers)):
         calc *= int(numbers[j])
   else:
      calc = 0
      for j in range(len(numbers)):
         calc += int(numbers[j])
   out += calc
print(out)



