import sys; args = sys.argv[1:]
#n = int(len(args[0])**0.5)
n = 7
setOfchoices = ["1","2","3","4","5","6","7"]

def bruteForce(pzl):

  if not isValid(pzl): return ""
  if isSolved(pzl): return pzl

  choice = pzl.index(".")
  
  for c in setOfchoices:
    subPzl = makeSub(pzl, c, choice)
    bf = bruteForce(subPzl)
    if bf: return bf

  return ""

def isSolved(puzzle):
  if puzzle.find(".") == -1:
    return True  
  else: 
    return False
    
def makeSub(puzzle, sub, choice):
  return puzzle[:choice]+sub+puzzle[choice+1:]



def isValid(puzzle):
  
  r = []
  for i in range(0,len(puzzle),n):
    r.append([*puzzle[i:i+n]])
  
  if not isNoDuplicates(r): 
    return False

  cSet = []
  for i in range(n):
    c = []
    for k in range(i,len(puzzle),n):
      c.append(puzzle[k])
    cSet.append(c)
  
  if not isNoDuplicates(cSet): 
    return False

  d1 = []
  for i in range(n):
    d1.append(r[i][i])
  
  for i,e in enumerate(d1):
    if e != ".":
      for x in d1[i+1:]:
        if e == x: 
           return False

  d2 = []
  for i in range(n):
    d2.append(r[i][n-i-1])

  for i,e in enumerate(d2):
    if e != ".":
      for x in d2[i+1:]:
        if e == x: 
           return False
  
  return True

def isNoDuplicates(lst):
  for sn in lst:
    for i,e in enumerate(sn):
      if e != ".":
        for x in sn[i+1:]:
          if e == x: return False
  return True

def displayPzl(pzl):
  toRet = ""
  for i in range(0,len(pzl),n):
    str = ""
    for k in range(i,i+n):
      str += pzl[k]+" "
    toRet += str + "\n"
  return toRet



str = ""
for i in range(n**2):
  str += "."

solution = bruteForce(str)
print(displayPzl(solution))