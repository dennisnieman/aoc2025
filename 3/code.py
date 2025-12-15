with open('input.txt') as file:
   inp = file.read().splitlines() 

# part 1

out = 0
for i in inp:
   numbers = [int(x) for x in i]
   m = max(numbers[:-1])
   loc = min(u for u, j in enumerate(numbers) if j == m)
   out += int(str(m) + str(max(numbers[j] for j in range(loc+1, len(numbers)))))
print(out)

# part 2

out = 0
for i in inp:
   numbers = [int(x) for x in i]
   joltage = ''
   lowerLimit = 0
   while len(joltage) < 12:
      m = max(numbers[lowerLimit : len(numbers)+len(joltage)-11])
      loc = lowerLimit + min(u for u, j in enumerate(numbers[lowerLimit : ]) if j == m)
      joltage = joltage + str(numbers[loc])
      lowerLimit = loc + 1
   out += int(joltage)
print(out)