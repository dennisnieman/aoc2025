with open('input.txt') as file:
   inp = file.read().splitlines() 

# part 1

out = 0
def walk(loc):
   global out
   if loc == 'out':
      out += 1
   else:
      for i in inp:
         if i[:3] == loc:
            for l in i[5:].split(' '):
               walk(l)
walk('you')
print(out)


# part 2

inp_seen = []
outp_seen = []
def walk(loc, dac, fft):
   global inp_seen, outp_seen
   if loc == 'out':
      return dac and fft
   elif [loc, dac, fft] in inp_seen:
      return outp_seen[inp_seen.index([loc, dac, fft])]
   else:
      for i in inp:
         if i[:3] == loc:
            outp = sum(walk(l, dac or l=='dac', fft or l=='fft') for l in i[5:].split(' '))
      inp_seen.append([loc, dac, fft])
      outp_seen.append(outp)
      return outp
print(walk('svr', 0, 0))