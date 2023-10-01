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
  
  if not noDuplicate(r): 
    return False

  col = []
  for i in range(n):
    c = []
    for k in range(i,len(puzzle),n):
      c.append(puzzle[k])
    col.append(c)
  
  if not noDuplicate(c): return False

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

def noDuplicate(lst):
  for section in lst:
    for i,e in enumerate(section):
      if e != ".":
        for x in section[i+1:]:
          if e == x: return False
  return True

def displayPzl(s):
  toRet = ""
  for i in range(0,len(s),n):
    str = ""
    for k in range(i,i+n):
      str += s[k]+" "
    toRet += str + "\n"
  return toRet



str = ""
for i in range(n**2):
  str += "."

solution = bruteForce(str)
print(displayPzl(solution))