with open('input.txt') as file:
   inp = file.read().splitlines() 

# part 1

pos = 50
out = 0
for i in inp:
   if i[0] == 'R':
      pos = (pos + int(i[1:])) % 100
   else:
      pos = (pos - int(i[1:])) % 100
   out += (pos == 0)
print(out)



# part 2

pos = 50
out = 0
for i in inp:
   if i[0] == 'R':
      for j in range(int(i[1:])):
         pos = (pos + 1) % 100
         out += (pos == 0)
   else:
      for j in range(int(i[1:])):
         pos = (pos - 1) % 100
         out += (pos == 0)
print(out)