with open('input.txt') as file:
   inp = file.read().splitlines() 
inp = [[int(x) for x in i.split(',')] for i in inp]

# part 1

largest = 0
for i in range(len(inp)):
   for j in range(i+1, len(inp)):
      area = (abs(inp[i][0] - inp[j][0]) + 1) * (abs(inp[i][1] - inp[j][1]) + 1)
      if area > largest:
         largest = area
print(largest)

# part 2

vLines = [sorted([inp[2*j], inp[2*j+1]]) for j in range(int(len(inp)/2))]
hLines = [sorted([inp[2*j+1], inp[2*j+2]]) for j in range(int(len(inp)/2)-1)]
hLines.append(sorted([inp[0], inp[-1]]))

largest = 0
for i in range(len(inp)):
   for j in range(i+1, len(inp)):
      xmin = min(inp[i][0], inp[j][0])
      xmax = max(inp[i][0], inp[j][0])
      ymin = min(inp[i][1], inp[j][1])
      ymax = max(inp[i][1], inp[j][1])
      if all(not(ymin < h[0][1] < ymax and xmin < h[1][0] and h[0][0] < xmax) for h in hLines):
         if all(not(xmin < v[0][0] < xmax and ymin < v[1][1] and v[0][1] < ymax) for v in vLines):
            area = (abs(inp[i][0] - inp[j][0]) + 1) * (abs(inp[i][1] - inp[j][1]) + 1)
            if area > largest:
               largest = area
print(largest)