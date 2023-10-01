import sys; args=sys.argv[1:]
import time
import math

start = time.time() 
w = 4
dctDirection = {}
def main():
  #if args:
    #with open(args[0]) as f1:
      
      puzzle = "JCFDIKL_GOEMNAHB"

      #if i == 0: 
      goal = "IJO_KLCFGMDENAHB"
      pzlen = len(goal)
      w = int(max([j for j in range(1,int(math.sqrt(pzlen) + 0.5) + 1) if (pzlen/j * j) == pzlen]))
      #steps = solve(goal, goal)
        #else:
      #puzzle = p
      steps = aStar(puzzle, goal)
          #print(f"Steps: {steps}")
          #print(f"Time: {float('%.3g' % (time.time()-start))}s")

def condensePath(path):
  length = len(path)
  cp = ""
  swaps = [1, -w, w, -1]
  cdir = ['L', 'D', 'U', 'R']
  if length == 1:
    return "G"

  if length > 0:
    for i in range(1, length):
      nbr1 = path[i-1].index('_')
      nbr2 = path[i].index('_')
      cp += cdir[swaps.index(nbr1-nbr2)]
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
  if goal != '12345678_':
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
  level = 0
  #openSet = [(0,("X",0))]
  #add(openSet, (h(root,goal),(root,level)))

  estimate = h(root,goal)
  openSet = [0]*82
  for i in range(len(openSet)):
    openSet[i] = set()
  openSet[estimate].add((estimate,(root,0)))
  totalEstimate = [0]
  add(totalEstimate, estimate)
  goalNeighborsdct = {c:i for i, c in enumerate(goal)}
  closedSet = {}
  

  while True:
    while len(openSet[estimate]) == 0:
      estimate += 1
    pzl, lvl = openSet[estimate].pop()[1]
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
    for nbr in neighbors(pzl):
        char = nbr[parentSpace]
        nbrIndex = parentSpace
  
        parentIndex = pzl.index(char)
        manhattanParent = abs(parentIndex//w - goalNeighborsdct[char]//w) + abs(parentIndex%w - goalNeighborsdct[char]%w) 
        manhattanNbr = abs(nbrIndex//w - goalNeighborsdct[char]//w) + abs(nbrIndex%w - goalNeighborsdct[char]%w)
        f = 1 + estimate + manhattanNbr - manhattanParent
        #f = lvl + 1 + h(nbr,goal)
        openSet[f].add((f,(nbr,lvl+1)))
        #add(openSet, (f, (nbr,lvl + 1)))





       
def h(pzl, goal):
  manhattanSum = 0
  for i in range(len(pzl)):
      if pzl[i] != '_':
        i2 = goal.index(pzl[i])
        manhattanSum += abs(i//w - i2//w) + abs(i%w - i2%w)
  return manhattanSum


# HEAP PQ

def heapDown(heap, k, lastIndex):
    l = 2*k
    r = 2*k + 1
    min = k
    if 1 > lastIndex and r > lastIndex:
        return
    if l > lastIndex:
        return
    if heap[l] - heap[min] < 0:
        min = l
    if r < lastIndex and heap[r] - heap[min] < 0:
        min = r
    if heap[k] - heap[min] > 0:
        Hswap(heap, k, min)
        heapDown(heap, min, lastIndex)

def Hswap(heap, a, b):
    heap[a], heap[b] = heap[b], heap[a]

def heapUp(heap, k):
    if k/2 == 0:
        return
    if k>= 2 and heap[k//2] - heap[k] > 0:
        Hswap(heap, k, k//2)
        heapUp(heap, k//2)

def add(heap, e):
    heap.append(e)
    heapUp(heap, len(heap)-1)

def remove(heap):
    Hswap(heap, 1, len(heap)-1)
    e = heap.pop()
    heapDown(heap,1,len(heap)-1)
    return e

def peek(heap):
    if heap:
        return heap[1]
    return


if __name__ == "__main__": main()  

 # Dev Kodre Pd:4 2024
