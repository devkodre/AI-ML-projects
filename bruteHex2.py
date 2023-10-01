import sys; args = sys.argv[1:]
str = args[0]

setOfchoices = ["1","2","3","4","5","6"]

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
  
  hex1 = [puzzle[0],puzzle[1],puzzle[2],puzzle[6],puzzle[7],puzzle[8]]
  hex2 = [puzzle[5],puzzle[6],puzzle[7],puzzle[12],puzzle[13],puzzle[14]]
  hex3 = [puzzle[13],puzzle[14],puzzle[15],puzzle[19],puzzle[20],puzzle[21]]
  hex4 = [puzzle[15],puzzle[16],puzzle[17],puzzle[21],puzzle[22],puzzle[23]]
  hex5 = [puzzle[9],puzzle[10],puzzle[11],puzzle[16],puzzle[17],puzzle[18]]
  hex6 = [puzzle[2],puzzle[3],puzzle[4],puzzle[8],puzzle[9],puzzle[10]]
  hex7 = [puzzle[7],puzzle[8],puzzle[9],puzzle[14],puzzle[15],puzzle[16]]
  
  return isNoDuplicates([hex1,hex2,hex3,hex4,hex5,hex6,hex7])

def isNoDuplicates(lst):
  for sn in lst:
    for i,e in enumerate(sn):
      if e != ".":
        for x in sn[i+1:]:
          if e == x: return False
  return True

def displayPzl(pzl):
  return "  " + " ".join([*pzl[:5]]) +"\n" + " ".join([*pzl[5:12]]) +"\n" + " ".join([*pzl[12:19]]) +"\n" + "  " + " ".join([*pzl[19:]])


solution = bruteForce(str)
print(displayPzl(solution))