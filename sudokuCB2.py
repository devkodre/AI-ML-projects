import sys; args = sys.argv[1:]
import time
#str = args[0]
statsCount = {}
def calcfactors(c):
    a, b, i = 1, c, 0
    while a < b:
        i += 1
        if c % i == 0:
            a = i
            b = c//a
    
    return b, a
def setGlobals(pzl): #create constraint sets, dotSet, and Neighbors, frequency table
    global size,side,bW,bH
    side = int(len(pzl)**0.5)
    size = int(len(pzl))
    bH, bW = calcfactors(side)

    global setOfchoices, Neighbors, dotSet, freqTable,LOCS, choiceBoard, bSub, csInter, filledVals, minCharVal

    filledVals = []
    
    for i,e in enumerate(pzl):
        if e != ".":
            filledVals.append((e,i))



    masterChoiceSet = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F",
    'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    #setOfchoices = {*masterChoiceSet[:side]}
    setOfchoices = {c for c in pzl if c != "."}
    if len(setOfchoices) < side:
        for c in masterChoiceSet:
            if c not in setOfchoices:
                setOfchoices.add(c)
            if len(setOfchoices) == side:
                break
    
    minCharVal = min(setOfchoices)

        
    Neighbors = []
    dotSet = {}
    choiceBoard = []
    LOCS = []

    r = [set(side*x+y for y in range(side))for x in range(side)]
    c = [set(x+y for y in range(0,size,side))for x in range(side)] 
    bSub = []
    b = 0
    for b in range(side):
        temp = set()
        for bHeight in range(bH):
            for bWidth in range(bW):
                    index = bWidth + bW*(b%bH) + bHeight*side + side*(b//bH)*bH
                    temp.add(index)
        bSub.append(temp)

    LOCS = r + c + bSub

    Neighbors = [set().union(*[cs for cs in LOCS if pos in cs]) - {pos} for pos in range(size)]
    

    dotSet = {index: setOfchoices - {pzl[i] for i in Neighbors[index]} for index in range(size) if pzl[index] == '.'}
    for i,c in enumerate(pzl):
        choiceBoard.append("")
        if c == ".":
            for s in setOfchoices:
                choiceBoard[i]+=s
                
        else:
            choiceBoard[i] = c
    
    csInter = {i:[] for i in range(size)}    #maps index to the index of constraint sets in LOCS that include that index
    for i in range(size):                    #For example: 0> first row, first column, first block| 0>0,9,18 (first 9 rows, 9 columns, 9 box)
        for k in range(len(LOCS)):           #             1> first row, second column, first block 1>0,10,18 
            if i in LOCS[k]:
                csInter[i].append(k)

def forwardLook(cb, filled):
    for val in filled:
        for removable in Neighbors[val[1]]:
            checker = len(cb[removable])
            cb[removable] = cb[removable].replace(val[0], "")
            if len(cb[removable]) < checker and len(cb[removable]) == 1:
                filled.append((cb[removable], removable))
            if len(cb[removable]) == 0:
                return None
    newCb, newFilled = constraintProp(cb)
    if newFilled is None:
        return None
    elif len(newFilled) > 0:
        return forwardLook(newCb, newFilled)
    else:
        updateStatsCount("forwardLook")
        return newCb 
    


def constraintProp(pzl): #finds possible choice in a constraint set that only occurs once and determines that that is the the choice
    changed = []
    newPzl = pzl.copy()
    for set in LOCS:
        for char in setOfchoices:
            count = 0
            count_val = -1
            for val in set:
                if char in pzl[val] and len(pzl[val]) > 1:
                    count += 1
                    count_val = val
            if count == 1:
                changed.append((char, count_val, set))
                newPzl[count_val] = char
    updateStatsCount("ConstraintProp")
    #printFormat(pzl)
    #print()
    return newPzl, changed




def availableProp(pzl, filled): # combines both propagations before brute force
    
    pzl = forwardLook(pzl, filled)
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
    #pzf = forwardLook(pzl)
    #if pzf != None: pzl = pzf 
    i = findBestChoice(pzl)
    choices = pzl[i]
    for c in choices:
        subPz = pzl.copy()
        subPz[i]=c 
        newf = [(c, i)]
        bF = forwardLook(subPz,newf)
        if bF != None:
            result = bruteForce(bF)
            if result != None:
                return result
    
        
                    
    return None

"""def mostProbableOrder(choiceSet,ft):#picks the best order of the choices using the set of choices in dotset at a space
    
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
    return order"""

    


        

def isSolved(puzzle): # checks if puzzle is sobed
  updateStatsCount("isSolved")
  for val in puzzle:
        if len(val) > 1:
            return False
  return True
  
    
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
        sum += ord(pzl[i])-ord(minCharVal)
    return str(sum)


def main():
    n = 1
    maxTime = 0
    pzlNum = 0
    begin = time.time()
    with open(args[0]) as f:
        for line in f:
            startTime = time.time()
            pzl = line.strip()
            #pzl = "..J1......V....C..1....F.0..N...KV..0...J..W...VF....C..F.W..J..K......N.....VF.."
            setGlobals(pzl)
            cb = availableProp(choiceBoard, filledVals)
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