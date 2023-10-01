import sys; args = sys.argv[1:]
import time
#str = args[0]

def setGlobals(pzl): #create constraint sets, dotSet, and Neighbors, frequency table
    global size,side
    side = int(len(pzl)**0.5)
    size = int(len(pzl))
    global setOfchoices, Neighbors, dotSet, statsCount, freqTable,LOCS

    statsCount = {}

    masterChoiceSet = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    setOfchoices = {*masterChoiceSet[:side]}
    Neighbors = {}
    dotSet = {}
    LOCS = []

    r = [set(side*x+y for y in range(side))for x in range(side)]
    c = [set(x+y for y in range(0,size,side))for x in range(side)] 
    b1 = {0,1,2,9,10,11,18,19,20}
    b2 = {3,4,5,12,13,14,21,22,23}
    b3 = {6,7,8,15,16,17,24,25,26}

    b4 = {27 + e for e in b1}
    b5 = {27 + e for e in b2}
    b6 = {27 + e for e in b3}

    b7 = {54 + e for e in b1}
    b8 = {54 + e for e in b2}
    b9 = {54 + e for e in b3}

    bSub = [b1,b2,b3,b4,b5,b6,b7,b8,b9]

    LOCS = r + c + bSub





    freqTable = {}

    for n in pzl:
        if n != ".":
            if n in freqTable:
                freqTable[n]+=1
            else:
                freqTable[n] = 1
            if freqTable[n] == side:
                del freqTable[n]


    
            
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
    

    dotSet = {index: setOfchoices - {pzl[i] for i in Neighbors[index]} for index in range(size) if pzl[index] == '.'}


def forwardLook(ds, pzl): #Initial sudoku logic to fill board using neighbors and dotset to determine possible position
    #eliminated = set()
    i = 0
    flag = False
    while i in range(81):
        if i in ds:
            index = i
            if len(ds[index]) == 1:
                pzl = makeSub(pzl,''.join(ds[index]),index)
                reMakeDS(pzl,ds,index)
                flag = True
                i = 0
                #print(f"Change {ds[index]} index: {index} or row {index//9} col {index%9}")
                del ds[index]
                #print("\n".join([pzl[x:x+9] for x in range(0,81,9)]))
            else: i+=1
        else: i+=1
    updateStatsCount("forwardLook")
    return pzl, flag


def reMakeDS(pzl, ds, index): # remakes DotSet after each forwardlook and deletes the index of the dot in dot set
    for i in Neighbors[index]:
        if i in ds:
            if pzl[index] in ds[i]:
                ds[i].remove(pzl[index])
                if len(ds[i]) == 0:
                    del ds[i]

def constraintProp(ds,pzl): #finds possible choice in a constraint set that only occurs once and determines that that is the the choice
    madeChange = True
    flag = False
    while madeChange:
        madeChange = False
        for cs in LOCS:
            tempFrq = {}
            for index in cs:
                if pzl[index] == ".":
                    for num in ds[index]:
                        if num in tempFrq:
                            tempFrq[num]+=1
                        else:
                            tempFrq[num]=1
            for i in cs:
                if pzl[i] == ".":
                    for num in ds[i]:
                        if tempFrq[num]==1:
                            madeChange = True
                            flag = True
                            pzl = makeSub(pzl,num,i)
                            reMakeDS(pzl,ds,i)
                            del ds[i]
    updateStatsCount("ConstraintProp")
    return pzl, flag
            
def availableProp(ds,pzl): # combines both propagations before brute force
    flag = True
    while flag:
        flag = False
        pzl, f1 = forwardLook(ds,pzl)
        pzl, f2 = constraintProp(ds, pzl)
        flag = f1 or f2
    return pzl



    





    



    

def bruteForce(pzl, prevChoice, ds,ft): #Brute force finds each possible choice and updates pzl and datastructures
  if not isValid(pzl, prevChoice): 
      updateStatsCount("inValid")
      return ""
  pzlCopy = pzl
  if isSolved(pzlCopy): 
      updateStatsCount("solved")
      return pzlCopy


  choice = findBestChoice(ds)
  for bc in choice:
    for c in mostProbableOrder(ds[bc], ft):
        dsCopy = {k:{*ds[k]} for k in ds}
        ftCopy = {k:ft[k] for k in ft}
        
        for nbr in Neighbors[bc]:
          if nbr not in dsCopy and pzlCopy[nbr] == c:
            continue
          if nbr in dsCopy:
            dsCopy[nbr].discard(c)
        del dsCopy[bc]
        if c not in ftCopy:
            ftCopy[c]=1
        else:
            ftCopy[c]+=1
        if ftCopy[c] == 9:
            del ftCopy[c]
        subPzl = makeSub(pzlCopy, c, bc)
        bf = bruteForce(subPzl, prevChoice, dsCopy,ftCopy)
        if bf: 
            updateStatsCount("returnBf")
            return bf

  return ""

def mostProbableOrder(choiceSet,ft): #picks the best order of the choices using the set of choices in dotset at a space
    cSetCopy  = choiceSet.copy()
    relevantFreq = choiceSet.intersection(ft)
    orderedFreq = []
    for k in relevantFreq:
        orderedFreq.append(ft[k])
    orderedFreq.sort(reverse=True)
    order = []
    for key in ft:
        if key in cSetCopy:
            for num in orderedFreq:
                if ft[key] == num and key in cSetCopy:
                    cSetCopy.remove(key)
                    order.append(key)
    for num in cSetCopy:
        order.append(num)
    updateStatsCount("order")
    return order

    


        

def isSolved(puzzle): # checks if puzzle is sobed
  if puzzle.find(".") == -1:
    updateStatsCount("isSolvedTrue")
    return True  
  else: 
    updateStatsCount("isSolvedFalse")
    return False
    
def makeSub(puzzle, sub, choice): # creates sub puzzle
  updateStatsCount("makeSub")
  return puzzle[:choice]+sub+puzzle[choice+1:]

def findBestChoice(dotSet): #Streamlined to find the best choice using dotset
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






def isValid(puzzle, prevChoice): #checks if puzzle is valid
    for index in Neighbors[prevChoice]:
        if puzzle[prevChoice] != "." and puzzle[prevChoice] == puzzle[index]:
            updateStatsCount("isValidFalse")
            return False
    updateStatsCount("isValidTrue")
    return True

def displayPzl(pzl, n): #displays pzl in one line
  if n // 100 > 0:
    toRet = str(n) + ": " + pzl
  elif n // 10 > 0:
    toRet = " " + str(n) + ": " + pzl
  else:
    toRet = "  " + str(n) + ": " + pzl
  return toRet

def displaySln(pzl): #displays solution in one line
  toRet = "     " + pzl

  return toRet

def checkSum(pzl): #used to check if solution is valid
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
            #pzl = ".8...4.5....7..3............1..85...6.....2......4....3.26............417........"
            setGlobals(pzl)
            pzlCopy = availableProp(dotSet,pzl)
            solution = bruteForce(pzlCopy,0,dotSet,freqTable)
            print(displayPzl(pzl,n))
            print(displaySln(solution), checkSum(solution))
            print("time: {0:1.3g}s".format(time.time()-startTime))
            n+=1
            #REMEMBER TO REMOVE __________________________________________
    print(statsCount)
    print("Totaltime: {0:1.3g}s".format(time.time()-begin))

if __name__ == "__main__": main() 

# Dev Kodre, Pd. 4, 2024