import sys ;s=sys.argv[1:]
import time

#s = ['Eckel.txt']

start = time.time() 
w = 4
hlookUpdct = {}
def main():
  if s:
    with open(s[0]) as f1:
      #n = 0
      goal = ""
      puzzle = ""
      global goalNeighborsdct
      for i, line in enumerate(f1):
        p = line.strip()
        if i == 0: 
          goal = p
          goalNeighborsdct = {c:i for i, c in enumerate(goal)}
          manhattanSum = 0
          for i in range(16):
            for i2 in range(len(goal)):
              manhattanSum = abs(i//w - i2//w) + abs(i%w - i2%w)
              hlookUpdct[(i,i2)] = manhattanSum
          steps = aStar(goal, goal)
        else:
          
          puzzle = p
          
          steps = aStar(puzzle, goal)
          #n+=1
          #print(steps)
          #print(f"Steps: {steps}")
          #print(f"Time: {float('%.3g' % (time.time()-start))}s")

def condensePath(path):
  length = len(path)
  cp = ""
  swaps = [-1, -w, w, 1]
  cdir = ['L', 'U', 'D', 'R']

  if length == 1:
    return "G"

  if length > 0:
    for i in range(1, length):
      nbr1 = path[i-1].index('_')
      nbr2 = path[i].index('_')
      cp += cdir[swaps.index(nbr2-nbr1)]
    return cp
  
  if length == 0:
    return "X"
  
  
  

      
  
     
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

  for x in range(len(end)-1):
    for y in range(x+1,len(end)):
      if ord(end[y]) < ord(end[x]):
        goalCount+=1
  if len(pz) % 2 != 0:
    return initCount % 2 == goalCount % 2
  else:
    return ((initCount + (pz.index('_'))//w) % 2) == ((goalCount + (goal.index('_')//w)) % 2)

def aStar(root, goal):
  if not isSolvable(root,goal):
    print(root + ": X")
    return
  #openSet = [(0,("X",0))]
  #add(openSet, (h(root,goal),(root,level)))


  estimate = h(root,goal)
  openSet = [0]*82
  for i in range(len(openSet)):
    openSet[i] = set()
  openSet[estimate].add((root,0))
  #add(totalEstimate, estimate)
  
  closedSet = {}
  

  while True:
    while len(openSet[estimate]) == 0:
      estimate += 1
    pzl, lvl = openSet[estimate].pop()
    #pzl, lvl = remove(openSet)[1]
    if pzl in closedSet:
        continue
    closedSet[pzl] = lvl
    if pzl == goal:
        path = [goal]
        rev = goal
        while rev != root:
            for nbr in neighbors(rev):
                if nbr in closedSet and nbr not in path and closedSet[rev] - closedSet[nbr] == 1:
                  
                  path.append(nbr)
                  rev = nbr
                  if nbr == root:
                    break
        path.reverse()
                  

        print(root + ": " + condensePath(path))
        return len(path)-1
                    
    parentSpace = pzl.index('_')        
    #for nbr in neighbors(pzl):
    space = parentSpace+1
    iList = []
    swaps = [-1,w,-w,1] 
    if space%w == 0:
      swaps = swaps[:3]
    elif space % w == 1:
      swaps = swaps[1:] 
  
    for n in swaps:
      if 0 < space+n <= w**2:
        iList.append(space + n)
    for ni in iList:
        nbr = swap(pzl,space-1,ni-1)
        char = nbr[parentSpace]
        nbrIndex = parentSpace
        goalIndex = goalNeighborsdct[char]
  
        parentIndex = pzl.index(char)
        #manhattanParent = abs(parentIndex//w - goalNeighborsdct[char]//w) + abs(parentIndex%w - goalNeighborsdct[char]%w) 
        #manhattanNbr = abs(nbrIndex//w - goalNeighborsdct[char]//w) + abs(nbrIndex%w - goalNeighborsdct[char]%w)
        manhattanParent = hlookUpdct[(parentIndex, goalIndex)]
        manhattanNbr = hlookUpdct[(nbrIndex, goalIndex)]
        f = 1 + estimate + manhattanNbr - manhattanParent
        #f = lvl + 1 + h(nbr,goal)
        openSet[f].add((nbr,lvl+1))
        #add(openSet, (f, (nbr,lvl + 1)))





       
def h(pzl, goal):
  manhattanSum = 0
  for i in range(len(pzl)):
      if pzl[i] != '_':
        i2 = goal.index(pzl[i])
        manhattanSum += abs(i//w - i2//w) + abs(i%w - i2%w)
  return manhattanSum




if __name__ == "__main__": main()  

 # Dev Kodre Pd:4 2024
