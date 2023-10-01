import sys; args = sys.argv[1:]
import time
#str = args[0]
statsCount = {}
def setGlobals(pzl): #create constraint sets, dotSet, and Neighbors, frequency table
    global size,side
    side = int(len(pzl)**0.5)
    size = int(len(pzl))
    global setOfchoices, Neighbors, dotSet, freqTable,LOCS, choiceBoard, bSub, csInter

    statsCount = {}

    masterChoiceSet = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F",
    'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    setOfchoices = {*masterChoiceSet[:side]}
    Neighbors = {}
    dotSet = {}
    choiceBoard = []
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
    for i,c in enumerate(pzl):
        choiceBoard.append("")
        if c == ".":
            for s in dotSet[i]:
                choiceBoard[i]+=s
                
        else:
            choiceBoard[i] = c
    
    csInter = {i:[] for i in range(size)}    #maps index to the index of constraint sets in LOCS that include that index
    for i in range(size):                    #For example: 0> first row, first column, first block| 0>0,9,18 (first 9 rows, 9 columns, 9 box)
        for k in range(len(LOCS)):           #             1> first row, second column, first block 1>0,10,18 
            if i in LOCS[k]:
                csInter[i].append(k)

def forwardLook(pzl): #Initial sudoku logic to fill board using neighbors and dotset to determine possible position
    #eliminated = set()
    for i in range(len(pzl)):
        if len(pzl[i])==1:
            found = pzl[i]
            for j in csInter.get(i):
                for num in LOCS[j]:
                    if num != i:
                        pzl[num]=pzl[num].replace(found,"")
                        if len(pzl[num])==0:
                            return None 
    updateStatsCount("forwardLook")
    #printFormat(pzl)
    #print()
    return pzl


def reMakeDS(pzl, ds, index): # remakes DotSet after each forwardlook and deletes the index of the dot in dot set
    for i in Neighbors[index]:
        if i in ds:
            if pzl[index] in ds[i]:
                ds[i].remove(pzl[index])
                if len(ds[i]) == 0:
                    del ds[i]

def constraintProp(pzl): #finds possible choice in a constraint set that only occurs once and determines that that is the the choice
    for cs in LOCS:
        for val in setOfchoices:
            valInd = []
            for ind in cs:
                if val in pzl[ind]:
                    valInd.append(ind)
            if len(valInd) == 1:
                pzl[valInd[0]]=val  
    updateStatsCount("ConstraintProp")
    #printFormat(pzl)
    #print()
    return pzl
def isEqual(pzlOld, pzlNew):
    for i,s in enumerate(pzlOld):
        if s != pzlNew[i]:
            return False
    return True

def availableProp(pzl): # combines both propagations before brute force
    pzlOG = pzl
    
    pzl = forwardLook(pzl)
    pzl = constraintProp(pzl)
    """while not isEqual(pzlOG,pzl):
        pzlOG = pzl
        pzl = forwardLook(pzl)
        pzl = constraintProp(pzl)""" 

    
    return pzl


def printFormat(pz):
    s = ""
    for i in range(9):
        for j in range(9):
            s += pz[i*9 + j]
            if (i*9 + j) % 3 == 0:
                s+= "||"
            else:
                s+= "|"
        s+="\n"
    print(s)

        
    





    



    

def bruteForce(pzl):
    if isSolved(pzl):
        return pzl
    pzl = constraintProp(pzl)
    #pzf = forwardLook(pzl)
    #if pzf != None: pzl = pzf 
    i = findBestChoice(pzl)
    choices = pzl[i]
    for c in choices:
        subPz = pzl.copy()
        subPz[i]=subPz[i].replace(choices, c)  
        bF = forwardLook(subPz)
        if bF != None:
            result = bruteForce(bF)
            if result != None:
                return result
    
        
                    
    return None

def mostProbableOrder(choiceSet,ft):#picks the best order of the choices using the set of choices in dotset at a space
    
    cSetCopy  = {*choiceSet}
    relevantFreq = cSetCopy.intersection(ft)
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
  updateStatsCount("isSolved")
  return sum(len(puzzle[i]) for i in range(size))== size
  
    
def makeSub(puzzle, sub, choice): # creates sub puzzle
  updateStatsCount("makeSub")
  return puzzle[:choice]+sub+puzzle[choice+1:]

def findBestChoice(pzl): #Streamlined to find the best choice using dotset
    min = 100
    index = 0
    for i in range(size):
        if 1<len(pzl[i])<min:
            min = len(pzl[i])
            index = i
            
    updateStatsCount("bestChoice")
    return index


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
  pzl = "".join(pzl)
  toRet = "     " + pzl

  return toRet

def checkSum(pzl): #used to check if solution is valid
    sum = 0
    for i in range(len(pzl)):
        sum += ord(pzl[i])-ord('1')
    return str(sum)


def main():
    n = 1
    maxTime = 0
    pzlNum = 0
    begin = time.time()
    with open("puzzles.txt") as f:
        for line in f:
            startTime = time.time()
            pzl = line.strip()
            #pzl = ".98.1....2......6.............3.2.5..84.........6.........4.8.93..5...........1.."
            setGlobals(pzl)
            cb = availableProp(choiceBoard)
            solution = bruteForce(cb)
            print(displayPzl(pzl,n))
            print(displaySln(solution), checkSum(solution))
            endTime = time.time()-startTime
            if endTime > maxTime:
                maxTime = endTime
                pzlNum = n
            print("time: {0:1.3g}s".format(endTime))
            n+=1
            #break #REMEMBER TO REMOVE __________________________________________
    print(statsCount)
    print("Totaltime: {0:1.3g}s".format(time.time()-begin))
    print(pzlNum)

if __name__ == "__main__": main() 

# Dev Kodre, Pd. 4, 2024