import sys; args = sys.argv[1:]
import time
import random
s = 3
if args:
  s = int(len(args[0])**0.5)
numpz = 500

def main():
  startTime = time.time()
  if args:
    path, steps = shortestPath(args[0],args[1] if len(args) > 1 else '12345678_')
    displayInfo(path,steps,startTime)
  else:
    stats = [0,0]
    l = ["1","2","3","4","5","6","7","8","_"]
    for n in range(1):
      random.shuffle(l)
      
      pz = ''.join(l)
      random.shuffle(l)
      goal = "".join(l)
      path, steps = shortestPath("13857_246",goal)
      max = 0
      fp = ""
      print(steps)
        
      if steps != -1:
        stats[0] += steps #total length of all solvable paths
        stats[1]+= 1      #total solvable puzzles
    
    print(fp,path)
    
  
  
    
    
def shortestPath(pz, goal):
   
  if pz == goal:
    #print("".join([pz[s*n:s*n+s] + "\n" for n in range(s)]))
    #print('Steps: 0')
    #print('Time: '+ "{0:1.3g}s".format(time.time()-startTime))
    return [pz], 0
  if not isSolvable(pz, goal):
    #print("".join([pz[s*n:s*n+s] + "\n" for n in range(s)]))
    #print("Steps: -1")
    #print("time: {0:1.3g}s".format(time.time()-startTime))
    return [pz], -1
    
     
  parseMe = [pz]
  dctSeen = {pz:""}
  
   
  while parseMe:
    e = parseMe[0]
    del parseMe[0]
    for p in [n for n in neighbors(e) if n not in dctSeen]:
      if p == goal:
        path = [e,p]
        steps =1
        rev = dctSeen.get(path[0])
        while rev != "":
          steps+=1
          path.insert(0,rev)
          rev = dctSeen.get(rev)
        
        #displayPuzzle(path)
        #print(f"Steps: {steps}")
        #print("time: {0:1.3g}s".format(time.time()-startTime))
        return path, steps
        
      parseMe.append(p)
      dctSeen.update({p:e})
      
  #displayPuzzle([pz])
  #print("Steps: -1")
  #print("time: {0:1.3g}s".format(time.time()-startTime))  
  return [pz], -1         
  

def neighbors(pz):
  space = pz.index('_')+1
  iList = []
  swaps = [-1,s,-s,1] 
  if space%s == 0:
    swaps = swaps[:3]
  elif space % s == 1:
    swaps = swaps[1:] 
  
  for n in swaps:
    if 0 < space+n <= s**2:
      iList.append(space + n)
  
  return[swap(pz,space-1,i-1) for i in iList]

def swap(pz,a,b):
  list = [*pz]
  list[a], list[b] = list[b], list[a]
  return "".join(list)
  
def displayInfo(path, steps, t):
  displayPuzzle(path)
  print(f"Steps: {steps}")
  print("time: {0:1.3g}s".format(time.time()-t))  
  
def printStats(stats, t):
  print("Total time: {0:1.3g}s".format(time.time()-t)) 
  print(f"Total number of puzzles processed: {numpz}")
  print(f"Total number of solvable puzzles: {stats[1]}")
  print(f"Average path length of solvable puzzles: {stats[0]/stats[1]}")
   
   
def displayPuzzle(path):
  str=""
  for a in range(0,len(path),6):
    for b in range(0,s*s,s):
      for x in path[a:a+6]:
        str+=x[b:b+s] + " "
      str+="\n"
    str+="\n"
  print(str)  
  
def isSolvable(pz, goal):
  initCount = 0
  goalCount = 0
  start = pz.replace('_','')
  end = goal.replace('_','')
  for x in range(len(start)-1):
    for y in range(x+1,len(start)):
      if start[y] < start[x]:
        initCount+=1
  if goal != '12345678_':
    for x in range(len(end)-1):
      for y in range(x+1,len(end)):
        if end[y] < end[x]:
          goalCount+=1
        
  if len(pz) % 2 != 0:
    return initCount % 2 == goalCount % 2
  else:
    return ((initCount + (pz.index('_'))/s) % 2) == ((goalCount + (goal.index('_')/s)) % 2)
    
if __name__ == "__main__": main()  
  




# Dev Kodre, Pd. 4, 2024