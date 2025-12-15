with open('input.txt') as file:
   inp = file.read().splitlines() 

# part 1

split = inp.index('')
fresh = [[int(x) for x in i.split('-')] for i in inp[:split]]

out = 0
for i in inp[split+1 : ]:
   i = int(i)
   out += any(r[0] <= i <= r[1] for r in fresh)
print(out)


# part 2

intervals = []
for i in range(len(fresh)):
   if fresh[i][0] > 0:
      interval = fresh[i]
      j = i+1
      while j < len(fresh):
         if fresh[i][0] <= fresh[j][1] and fresh[j][0] <= fresh[i][1]:
            interval[0] = min(fresh[i][0], fresh[j][0])
            interval[1] = max(fresh[i][1], fresh[j][1])
            fresh[j] = [0, 0]
            j = i
         j += 1
      intervals.append(interval)
print(sum(i[1]-i[0] for i in intervals) + len(intervals))