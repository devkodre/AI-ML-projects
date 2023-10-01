import sys; args=sys.argv[1:]
import time
import math

start = time.time() 
w = 4
def main():
  if args:
    with open(args[0]) as f1:
      goal = ""
      puzzle = ""
      for i, line in enumerate(f1):
        p = line.strip()
        if i == 0: 
          goal = p
          pzlen = len(goal)
          w = int(max([j for j in range(1,int(math.sqrt(pzlen) + 0.5) + 1) if (pzlen/j * j) == pzlen]))
          steps = solve(goal, goal)
        else:
          puzzle = p
          steps = solve(puzzle, goal)
          #print(f"Steps: {steps}")
          #print(f"Time: {float('%.3g' % (time.time()-start))}s")

def condensePath(path):
  length = len(path)
  cp = ""
  swaps = [-1, -w, w, 1]
  cdir = ['L', 'U', 'D', 'R']
  
  if length > 0:
    for i in range(1, length):
      nbr1 = path[i-1].index('_')
      nbr2 = path[i].index('_')
      cp += cdir[swaps.index(nbr2-nbr1)]
    return cp
  
  if length == 0:
    return "X"
  if length == 1:
    return "G"
  
  

      
  
     
def swap(str, a, b):
  lst = [*str]
  lst[a], lst[b] = lst[b], lst[a]
  return "".join(lst)

def neighbors(pz):
  space = pz.index('_')+1
  iList = []
  swaps = [-1,w,-w,1] 
  if space%w == 0:
    swaps = swaps[:3]
  elif space % w == 1:
    swaps = swaps[1:] 
  
  for n in swaps:
    if 0 < space+n <= w**2:
      iList.append(space + n)
  
  return[swap(pz,space-1,i-1) for i in iList]
  
def isSolvable(pz, goal):
  initCount = 0
  goalCount = 0
  start = pz.replace('_','')
  end = goal.replace('_','')
  for x in range(len(start)-1):
    for y in range(x+1,len(start)):
      if ord(start[y]) < ord(start[x]):
        initCount+=1
  if goal != '12345678_':
    for x in range(len(end)-1):
      for y in range(x+1,len(end)):
        if ord(end[y]) < ord(end[x]):
          goalCount+=1
  if len(pz) % 2 != 0:
    return initCount % 2 == goalCount % 2
  else:
    return ((initCount + (pz.index('_'))//w) % 2) == ((goalCount + (goal.index('_')//w)) % 2)

def solve(puzzle, goal):
  if puzzle == goal:
    print(puzzle + ": G")
    return 0
  if not isSolvable(puzzle, goal):
    print(puzzle + ": X")
    return -1
  
  parseMe = [(h(puzzle, goal), puzzle)]
  dctSeen = {puzzle: ""}

  while parseMe:
    parseMe.sort(reverse=True)
    pzl = parseMe.pop()[1]
    #neighborlst= [nb if nb not in dctSeen else "0" for nb in neighbors(pzl)]
    for nbr in [n for n in neighbors(pzl) if n not in dctSeen]:
      #if nbr in dctSeen: continue
      if nbr == goal:    
        path = [nbr,pzl] 
        steps = 1
        prev = dctSeen.get(pzl)
        while prev!="":
          path.append(prev)
          steps += 1
          prev = dctSeen.get(prev)
        path.reverse()
        print(puzzle + ": " + condensePath(path))
        return steps
      parseMe.append((h(nbr,goal),nbr))
      dctSeen[nbr] = pzl
       
def h(pzl, goal):
  manhattanSum = 0
  for i in range(len(pzl)):
      if pzl[i] != '_':
        i2 = goal.index(pzl[i])
        manhattanSum += abs(i/w - i2/w) + abs(i%w - i2%w)
  return manhattanSum

if __name__ == "__main__": main()  

 # Dev Kodre Pd:4 2024
