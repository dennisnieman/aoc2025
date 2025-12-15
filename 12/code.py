with open('input.txt') as file:
   inp = file.read().splitlines() 

import torch
import numpy as np

# part 1

fits = [-1 for i in range(1000)]
for i in range(1000):
   units_avail = int(inp[30+i][0:2]) * int(inp[30+i][3:5])
   units_req = np.array([int(x) for x in inp[30+i].split(' ')[1:]]) @ np.array([7, 7, 6, 7, 7, 5])
   if units_avail < units_req : fits[i] = 0

   boxes_avail = int(int(inp[30+i][0:2])/3) * int(int(inp[30+i][3:5])/3)
   boxes_req = sum(int(x) for x in inp[30+i].split(' ')[1:])
   if boxes_req <= boxes_avail: fits[i] = 1