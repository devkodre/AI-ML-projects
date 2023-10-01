import sys; args = sys.argv[1:]
import time
#str = args[0]

def setGlobals(pzl):
    side = int(len(pzl)**0.5)
    size = int(len(pzl))
    global setOfchoices, Neighbors

    masterChoiceSet = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    setOfchoices = masterChoiceSet[:side]
    Neighbors = {}

    #rows
    for i in range(size):
        Neighbors[i] = set()
        y = i//side
        x = i%side
        for r in range(side):
            index = r + side*y
            if i != index :
                Neighbors[i].add(index)
        for c in range(0,size,side):
            index = c + x 
            if i != index :
                Neighbors[i].add(index)
        for bHeight in range(3):
            for bWidth in range(3):
                if x < 3 and y < 3:
                    index = bWidth + bHeight*side
                    if i!= index :
                        Neighbors[i].add(index)

                elif x < 6 and y < 3:
                    index = bWidth + 3 + bHeight*side
                    if i!= index :
                        Neighbors[i].add(index)
                elif x < 9 and y < 3:
                    index = bWidth + 6 + bHeight*side
                    if i!= index :
                        Neighbors[i].add(index)

                elif x < 3 and y < 6:
                    index = bWidth + bHeight*side + 27
                    if i!= index :
                        Neighbors[i].add(index)
                elif x < 6 and y < 6:
                    index = bWidth + 3 + bHeight*side + 27
                    if i!= index :
                        Neighbors[i].add(index)
                elif x < 9 and y < 6:
                    index = bWidth + 6 + bHeight*side + 27
                    if i!= index :
                        Neighbors[i].add(index)
                
                elif x < 3 and y < 9:
                    index = bWidth + bHeight*side + 54
                    if i!= index :
                        Neighbors[i].add(index)
                elif x < 6 and y < 9:
                    index = bWidth + 3 + bHeight*side + 54
                    if i!= index :
                        Neighbors[i].add(index)
                elif x < 9 and y < 9:
                    index = bWidth + 6 + bHeight*side + 54
                    if i!= index :
                        Neighbors[i].add(index)

    
           



        

def bruteForce(pzl, prevChoice):

  if not isValid(pzl, prevChoice): return ""
  if isSolved(pzl): return pzl

  choice = pzl.index(".")
  
  for c in setOfchoices:
    subPzl = makeSub(pzl, c, choice)
    bf = bruteForce(subPzl, choice)
    if bf: return bf

  return ""

def isSolved(puzzle):
  if puzzle.find(".") == -1:
    return True  
  else: 
    return False
    
def makeSub(puzzle, sub, choice):
  return puzzle[:choice]+sub+puzzle[choice+1:]



def isValid(puzzle, prevChoice):
    #for keyIndex in Neighbors:
        #for iSet in Neighbors[keyIndex]:
            #if puzzle[keyIndex] != ".":
                #if puzzle[keyIndex] == puzzle[iSet]:
                    #return False
    for index in Neighbors[prevChoice]:
        if puzzle[prevChoice] != "." and puzzle[prevChoice] == puzzle[index]:
            return False
    return True

def displayPzl(pzl, n):
  if n // 100 > 0:
    toRet = str(n) + ": " + pzl
  elif n // 10 > 0:
    toRet = " " + str(n) + ": " + pzl
  else:
    toRet = "  " + str(n) + ": " + pzl
  return toRet

def displaySln(pzl):
  toRet = "     " + pzl
  return toRet

def checkSum(pzl):
    sum = 0
    for i in range(81):
        sum += ord(pzl[i])-ord('1')
    return str(sum)


def main():
    n = 1
    with open(args[0]) as f:
        for line in f:
            startTime = time.time()
            pzl = line.strip()
            #s = ".17369825632158947958724316825437169791586432346912758289643571573291684164875293"
            setGlobals(pzl)
            solution = bruteForce(pzl,0)
            print(displayPzl(pzl,n))
            print(displaySln(solution), checkSum(solution))
            print("time: {0:1.3g}s".format(time.time()-startTime))
            n+=1

if __name__ == "__main__": main() 

# Dev Kodre, Pd. 4, 2024