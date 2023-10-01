import sys; args = sys.argv[1:]
str = args[0]

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
  
  hex1 = [puzzle[0],puzzle[1],puzzle[2],puzzle[6],puzzle[7],puzzle[8]]
  hex2 = [puzzle[5],puzzle[6],puzzle[7],puzzle[12],puzzle[13],puzzle[14]]
  hex3 = [puzzle[13],puzzle[14],puzzle[15],puzzle[19],puzzle[20],puzzle[21]]
  hex4 = [puzzle[15],puzzle[16],puzzle[17],puzzle[21],puzzle[22],puzzle[23]]
  hex5 = [puzzle[9],puzzle[10],puzzle[11],puzzle[16],puzzle[17],puzzle[18]]
  hex6 = [puzzle[2],puzzle[3],puzzle[4],puzzle[8],puzzle[9],puzzle[10]]
  hex7 = [puzzle[7],puzzle[8],puzzle[9],puzzle[14],puzzle[15],puzzle[16]]

  r1 = [puzzle[0],puzzle[1],puzzle[2],puzzle[3],puzzle[4]]
  r2 = [puzzle[5],puzzle[6],puzzle[7],puzzle[8],puzzle[9],puzzle[10],puzzle[11]]
  r3 = [puzzle[12],puzzle[13],puzzle[14],puzzle[15],puzzle[16],puzzle[17],puzzle[18]]
  r4 = [puzzle[19],puzzle[20],puzzle[21],puzzle[22],puzzle[23]]

  d1 = [puzzle[1],puzzle[0],puzzle[6],puzzle[5],puzzle[12]]
  d2 = [puzzle[3],puzzle[2],puzzle[8],puzzle[7],puzzle[14],puzzle[13],puzzle[19]]
  d3 = [puzzle[4],puzzle[10],puzzle[9],puzzle[16],puzzle[15],puzzle[21],puzzle[20]]
  d4 = [puzzle[11],puzzle[18],puzzle[17],puzzle[23],puzzle[22]]

  d5 = [puzzle[5],puzzle[12],puzzle[13],puzzle[19],puzzle[20]]
  d6 = [puzzle[0],puzzle[6],puzzle[7],puzzle[14],puzzle[15],puzzle[21],puzzle[22]]
  d7 = [puzzle[1],puzzle[2],puzzle[8],puzzle[9],puzzle[16],puzzle[17],puzzle[23]]
  d8 = [puzzle[3],puzzle[4],puzzle[10],puzzle[11],puzzle[18]]
  

  return isNoDuplicates([hex1,hex2,hex3,hex4,hex5,hex6,hex7,r1,r2,r3,r4,d1,d2,d3,d4,d5,d6,d7,d8])

def isNoDuplicates(lst):
  for section in lst:
    for i,e in enumerate(section):
      if e != ".":
        for x in section[i+1:]:
          if e == x: return False
  return True

def displayPzl(pzl):
  return "  " + " ".join([*pzl[:5]]) +"\n" + " ".join([*pzl[5:12]]) +"\n" + " ".join([*pzl[12:19]]) +"\n" + "  " + " ".join([*pzl[19:]])



solution = bruteForce(str)
print(displayPzl(solution))