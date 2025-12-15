with open('input.txt') as file:
   inp = file.read().split(',')

# part 1
out = 0
for i in inp:
   lower, upper = i.split('-')
   for j in range(int(lower), int(upper)+1):
      l = len(str(j))
      if l % 2 == 0:
         if str(j)[ : int(l/2)] == str(j)[int(l/2) : ]:
            out += j
print(out)


# part 2
inv = []
for i in inp:
   lower, upper = i.split('-')
   for j in range(int(lower), int(upper)+1):
      l = len(str(j))
      for k in range(1, int(l/2)+1):
         if l % k == 0:
            if all(str(j)[l-k:l] == str(j)[k*m : k*(m+1)] for m in range(int(l/k)-1)):
               if not(j in inv):
                  inv.append(j)
print(sum(inv))
