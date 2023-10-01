import sys; args = sys.argv[1:]
import time
#str = args[0]

def setGlobals(pzl):
    side = int(len(pzl)**0.5)
    size = int(len(pzl))
    global setOfchoices, Neighbors, dotSet, statsCount

    statsCount = {}

    masterChoiceSet = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    setOfchoices = {*masterChoiceSet[:side]}
    Neighbors = {}
    dotSet = {}

    r = [set(side*x+y for y in range(side))for x in range(side)]
    c = [set(x+y for y in range(0,size,side))for x in range(side)] 


    
            
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
    
    #for i in range(size):
        #if pzl[i] == ".":
            #dotSet[i] = set()
            #tempSet = set()
            #for j in Neighbors[i]:
                #tempSet.add(pzl[j])
        #dotSet[i].add(setOfchoices - tempSet)

    dotSet = {index: setOfchoices - {pzl[i] for i in Neighbors[index]} for index in range(size) if pzl[index] == '.'}




    
           



        

def bruteForce(pzl, prevChoice, ds):

  if not isValid(pzl, prevChoice): 
      updateStatsCount("inValid")
      return ""
  if isSolved(pzl): 
      updateStatsCount("solved")
      return pzl

  #choice = pzl.index(".")
  choice = findBestChoice(ds)
  for bc in choice:
    for c in ds[bc]:
        dsCopy = {k:{*ds[k]} for k in ds}
        #ftCopy = {k:ft[k] for k in ft}
        for nbr in Neighbors[bc]:
          if nbr not in ds and pzl[nbr] == c:
            continue
          if nbr in ds:
            dsCopy[nbr].discard(c)
        del dsCopy[bc]
        #ftCopy[c]+=1
        #if ftCopy[c] == 9:
        #    del ftCopy[c]
        subPzl = makeSub(pzl, c, bc)
        bf = bruteForce(subPzl, prevChoice, dsCopy)
        if bf: 
            updateStatsCount("returnBf")
            return bf

  return ""

def mostProbableOrder(choiceSet,ft):
    cSetCopy  = choiceSet.copy()
    orderedFreq = [*ft.values()]
    orderedFreq.sort(reverse=True)
    order = []
    for num in orderedFreq:
        for key in ft:
            if ft[key] == num and key in cSetCopy:
                cSetCopy.remove(key)
                order.append(key)
    return order

    


        

def isSolved(puzzle):
  if puzzle.find(".") == -1:
    updateStatsCount("isSolvedTrue")
    return True  
  else: 
    updateStatsCount("isSolvedFalse")
    return False
    
def makeSub(puzzle, sub, choice):
  updateStatsCount("makeSub")
  return puzzle[:choice]+sub+puzzle[choice+1:]

def findBestChoice(dotSet):
    #minDots = 100
    minSize = 100
    bestIndex = set()
    for i in dotSet:
        availableChoices = len(dotSet[i])
        if availableChoices < minSize:
            minSize = availableChoices 
            bestIndex = set()
            bestIndex.add(i)
            
    updateStatsCount("bestChoice")
    return bestIndex


def updateStatsCount(s):
    if s in statsCount:
        statsCount[s] += 1
    else:
       statsCount[s] = 1 






def isValid(puzzle, prevChoice):
    #for keyIndex in Neighbors:
        #for iSet in Neighbors[keyIndex]:
            #if puzzle[keyIndex] != ".":
                #if puzzle[keyIndex] == puzzle[iSet]:
                    #return False
    for index in Neighbors[prevChoice]:
        if puzzle[prevChoice] != "." and puzzle[prevChoice] == puzzle[index]:
            updateStatsCount("isValidFalse")
            return False
    updateStatsCount("isValidTrue")
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
    for i in range(len(pzl)):
        sum += ord(pzl[i])-ord('1')
    return str(sum)


def main():
    n = 1
    begin = time.time()
    with open(args[0]) as f:
        for line in f:
            startTime = time.time()
            pzl = line.strip()
            #pzl = "...78.4...31.........9......2..51.........9....6......7..4...5.8.......1.......2."
            setGlobals(pzl)
            solution = bruteForce(pzl,0,dotSet)
            print(displayPzl(pzl,n))
            print(displaySln(solution), checkSum(solution))
            print("time: {0:1.3g}s".format(time.time()-startTime))
            n+=1
            #REMEMBER TO REMOVE __________________________________________
    print(statsCount)
    print("time: {0:1.3g}s".format(time.time()-begin))

if __name__ == "__main__": main() 

# Dev Kodre, Pd. 4, 2024