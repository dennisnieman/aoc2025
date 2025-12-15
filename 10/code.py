with open('input.txt') as file:
   inp = file.read().splitlines() 
inp = [i.split(' ') for i in inp]

# part 1

out = 0
for i in inp:
   goal = tuple(int(x == '#') for x in i[0][1:-1])
   seen = {tuple(0 for j in range(len(goal)))}

   configs = {tuple(0 for j in range(len(goal)))}
   buttons = i[1:-1]
   pushes = 0
   while not(goal in configs):
      newConfigs = set()
      for config in configs:
         for button in buttons:
            button = [int(x) for x in button[1:-1].split(',')]
            new = tuple((c + (j in button)) % 2 for j, c in enumerate(config))
            if not(new in seen):
               seen.add(new)
               newConfigs.add(new)
      configs = newConfigs.copy()
      pushes += 1
   out += pushes
print(out)


# part 2

import numpy as np
from scipy.optimize import milp, LinearConstraint

out = 0
for i in inp:
   goal = np.array([int(x) for x in i[-1][1:-1].split(',')])
   n_lights = len(goal)
   n_buttons = len(i[1:-1])
   A = np.array([[int(str(x) in b[1:-1].split(',')) for x in range(n_lights)] for b in i[1:-1]]).T
   lc = LinearConstraint(A=A, lb=goal, ub=goal)
   opt = milp(c = [1 for j in range(n_buttons)], integrality=1, constraints=lc)
   out += opt.fun
print(int(out))