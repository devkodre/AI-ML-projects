import sys; args = sys.argv[1:]
import time

#args = "dct20k.txt 14x14 108 H3x2 V2x3 V4x4 V7x4 v9x6 H8x5".split(" ")
#1 args = ['dct20k.txt', '4x4', '0']
#2 args = ['dct20k.txt', '5x5', '0', 'H3x0scare']
#3args = ['dct20k.txt', '5x5', '0', 'V4x1e']
#4 args = ['dct20k.txt', '4x4', '2']
#5 args = ['dct20k.txt', '5x5', '2', 'h3x2E']
#6 args = ['dct20k.txt', '5x5', '4', 'v3x2C']
#7args = ['dct20k.txt', '4x5', '0']
#8 args = ['dct20k.txt', '5x4', '0']
#9 args = ['dct20k.txt', '7x7', '11']
#10 args = ['dctEckel.txt', '9x13', '19', 'v2x3#', 'v1x8#', 'h3x1#', 'v4x5##']
args = ['dctEckel.txt', '15x15', '37', 'H0x4#', 'v4x0#', 'h6x8a']


def setGlobals():
    
    global dct
    dct = {}
    global dctSize
    dctSize = 0
    with open(args[0]) as file:
        for line in file:
            dctSize +=1
            line = line.strip()
            if len(line) >= 3 and line.isalpha():
                if len(line) in dct:
                    dct[len(line)].add(line.lower())
                else:
                    dct[len(line)] = {line}
    #dctFile = s[0]
    s = args
    s = [s[i] for i in range(1,len(s))] 
    global pzl, length, height, bsCount, neighbors
    pzl=""; length =0; height=0; bsCount = 0
    #numsList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    neighbors = []
       
    
    
    #dct = sorted(dct, key=len)


    """if s:
        for e in s:
            if '.txt' in e:
                continue
            elif 'x' in e and ('h' not in e.lower() and 'v' not in e.lower()):
                i = s[0].index('x')
                height = int(s[0][:i])
                length = int(s[0][i+1:])
                puzzle = '-'*height*length
            elif 'x' in e:
                seedString = e.lower()
                i = seedString.index('x')
                y = int(seedString[1:i])
                ###for idx in range(i+1, len(seedString)):
                    if sum(int(x in seedString[idx]) for x in numsList) < 1:
                        wordIdx = idx
                        break
                    if idx == len(seedString) - 1:
                        wordIdx = len(seedString)###
                wordIdx = i+2
                while seedString[i+1:wordIdx].isnumeric():
                    wordIdx+=1
                wordIdx-=1
                x = int(seedString[i+1:wordIdx])
                if len(seedString) == wordIdx:
                    puzzle = puzzle[:length*y+x] + "#" + puzzle[length*y+x+1:]
                else:
                    if 'h' in seedString:
                        for idx, c in enumerate(e[wordIdx:]): 
                            puzzle = puzzle[:length*y+x+idx] + c + puzzle[length*y+x+idx+1:]
                    elif 'v' in seedString:
                        for idx, c in enumerate(e[wordIdx:]): 
                            puzzle = puzzle[:length*y+x+(idx*length)] + c + puzzle[length*y+x+(idx*length)+1:]
            elif e.isnumeric():
                bsCount = int(e)"""
    
    size = [int(x) for x in s[0].split('x')]
    height, length = size[0], size[1]
    bsCount = int(s[1])
    seedStrings = []
    if len(s) > 2:
        for seed in s[2:]:
            orientation = seed[0]; idx = 1
            while seed[idx] in '1234567890':
                idx += 1
            i1 = int(seed[1:idx])
            i2 = '' 
            words = ''
            idx += 1
            while idx < len(seed) and seed[idx] in '1234567890':
                i2 += seed[idx]
                idx += 1
            i2 = int(i2)
            words = seed[idx:]
            seedStrings.append((orientation, i1, i2, words))

    pzl = '.'*(height*length); pzl = [*pzl]
    for o,n1,n2,words in seedStrings:
        # print(chars)
        if o.lower() == 'h':
            for i,c in enumerate(words):
                i1 = n1*length+n2+i 
                i2 = height*length-i1-1

                if c=='#' and pzl[i1] != '#': bsCount -= 1
                pzl[i1] = c
                if c == '#' and pzl[i2] != '#':  
                    pzl[i2] = '#'
                    if i2 != i1: bsCount -= 1
                elif pzl[i2] == '.':
                    pzl[i2] = '-'
        else:
            for i,c in enumerate(words):
                i1 = n1*length+n2+length*i
                i2 = height*length-i1-1

                if c=='#' and pzl[i1]!='#': bsCount -= 1
                pzl[i1] = c
                if c == '#' and pzl[i2] != '#': 
                    pzl[i2] = '#'
                    if i1 != i2: bsCount -= 1
                elif pzl[i2] == '.':
                    pzl[i2] = '-'

    for i in range(height*length):
        x = []
        if i%length > 0: x.append(i-1)
        if i%length < length-1: x.append(i+1)
        if i//length > 0: x.append(i-length)
        if i//length < height-1: x.append(i+length)
        neighbors.append(x)

#check if part of horizontal or vertical word of length 3
def isLegal(pzl):
    
    for i in range(len(pzl)):
        if pzl[i] == "#":
            continue
        hFlag, vFlag = False, False
        for nbr in neighbors[i]:
            delta = nbr - i
            if pzl[i] != "#":
                if delta==length and nbr+length < height*length and '#' not in [pzl[nbr], pzl[nbr+length]]: 
                    vFlag = True
                elif delta==-length and nbr-length >= 0 and '#' not in [pzl[nbr], pzl[nbr-length]]:
                    vFlag = True
                elif i//length > 0 and i//length < height-1 and '#' not in [pzl[i], pzl[i+length], pzl[i-length]]: 
                    vFlag = True
                
                if delta==1 and nbr+1 < height*length and (nbr+1)//length==nbr//length and '#' not in pzl[nbr:nbr+2]: 
                    hFlag = True
                elif delta==-1 and nbr-1 >= 0 and (nbr-1)//length==nbr//length and '#' not in pzl[nbr-1:nbr+1]: 
                    hFlag = True
                elif i%length > 0 and i%length < length-1 and '#' not in [pzl[i], pzl[i+1], pzl[i-1]]: 
                    hFlag = True
        if not vFlag or not hFlag: return False
    return vFlag and hFlag and isConnected(pzl)

def isLegalSpace(pzl, i):
    hFlag, vFlag = False, False
    for nbr in neighbors[i]:
        delta = nbr - i
        if pzl[i] != "#":
            if delta==length and nbr+length < height*length and '#' not in [pzl[nbr], pzl[nbr+length]]: 
                vFlag = True
            elif delta==-length and nbr-length >= 0 and '#' not in [pzl[nbr], pzl[nbr-length]]:
                vFlag = True
            elif i//length > 0 and i//length < height-1 and '#' not in [pzl[i], pzl[i+length], pzl[i-length]]: 
                vFlag = True
            
            if delta==1 and nbr+1 < height*length and (nbr+1)//length==nbr//length and '#' not in pzl[nbr:nbr+2]: 
                hFlag = True
            elif delta==-1 and nbr-1 >= 0 and (nbr-1)//length==nbr//length and '#' not in pzl[nbr-1:nbr+1]: 
                hFlag = True
            elif i%length > 0 and i%length < length-1 and '#' not in [pzl[i], pzl[i+1], pzl[i-1]]: 
                hFlag = True
    return hFlag and vFlag


#used in tandum with isValid to see if everything is set
def isConnected(pzl):
    spaces = [i for i,c in enumerate(pzl) if c != "#"]
    seen = set([spaces[0]]) 
    searchList = [spaces[0]]
    for e in searchList:
        for n in neighbors[e]:
            if pzl[n] != "#":
                if n not in seen: searchList.append(n)
                seen.add(n)
    return len(seen) == len(spaces)

def getConnectedSections(pzl):
    cs = []
    seen = set()
    spaces = [i for i,c in enumerate(pzl) if c != "#"]

    for s in spaces:
        if s not in seen:
            searchList = [s]
            for e in searchList:
                for n in neighbors[e]:
                    if pzl[n] != '#':
                        if n not in seen: searchList.append(n)
                        seen.add(n)
                seen.add(e)
            cs.append(set(searchList))
    return cs
global startTime
startTime = time.time()
def bruteForce(pzl, bsCount):
    #bl = isLegal(pzl)
    #printPzl(pzl)
    #print("")
    if not isLegal(pzl): return ""
    
    
    if bsCount < 0 or ('.' not in pzl and bsCount > 0) or (bsCount < 0 and '.' in pzl):
        return ""
    if bsCount == 0: return pzl
    i = pzl.find('.')
    #if i == height*length//2: return ""
    #options = ['#','-'] if time.time()-startTime < 28 else (['#','-'] if bsCount*2 >= pzl.count('.')//2 else ['-','#'])
    options = '-#' if '#' in [pzl[n] for n in neighbors[i]] else '#-'
    for c in options:
        #if c != '###':
        np = pzl[:i] + c + pzl[i+1:height*length-i-1] + c + pzl[height*length-i:]
        #else:
            #np = pzl[:i] + c + pzl[i+3:height*length-i-3] + c + pzl[height*length-i:]
        if c == "#":
            bf = bruteForce(np, bsCount-2)
        #elif c == "###":
            #bf = bruteForce(np, bsCount-6)
        else:
            bf = bruteForce(np, bsCount)
        if bf: return bf
    return ""
#check if dash is part of word
def printPzl(pzl):
    for i in range(height):
        print(pzl[i*length:i*length+length])
    print()

def fillclosedOffSections(pzl,bCount):
    cs = []
    seen = set()
    
    for i,c in enumerate(pzl):
        if c == "#" and i not in seen:
            ep1 = False
            ep2 = False
            searchList = [i]
            for e in searchList:
                for n in neighbors[e]:
                    if pzl[n] == '#':
                        if len(neighbors[e]) == 3 and len(neighbors[n]) == 4:
                            if ep1:
                                ep2 = True
                            else:
                                ep1 = True
                        if n not in seen: searchList.append(n)
                        seen.add(n)
                seen.add(e)
            if ep1 and ep2:
                cs.append(set(searchList))
    
    for sections in cs:
        start = min(sections)
        end = max(sections) 
        if start%length < end%length:
            for i in range(start,end):
                if i%length >= start%length and i%length<= end%length:
                    pzl[i] = "#"
                    bCount-=1
        elif start%length == end%length:
            for i in range(start-(start%length), end):
                if i%length >= (start-(start%length))%length and i%length <= end%length:
                    pzl[i] = "#"
                    bCount-=1
        else:
            for i in range(start-(end%length), end + (start%length) - (end%length)):
                if i%length >= (start-(end%length))%length and i%length <= (end + (start%length) - (end%length))%length:
                    pzl[i] = "#"
                    bCount-=1

    return pzl, bCount

def placeWordHorizontal(brd):
    rows = [brd[i:i+length] for i in range(0,len(brd),length)]
    seen = set()
    matches = {}
    rowNum = 0
    for r in rows:
        count = 0
        startIndex = 0
        for i, c in enumerate(r):
            if c == '-':
                if count == 0:
                    startIndex = i
                count+=1
            else:
                if count >= 3:
                    if rowNum in matches:
                        matches[rowNum].append((startIndex,count))
                    else:
                        matches[rowNum] = [(startIndex,count)]

                count = 0
        if count>= 3:
            if rowNum in matches:
                matches[rowNum].append((startIndex,count))
            else:
                matches[rowNum] = [(startIndex,count)]
        rowNum+=1

    return matches
    



    #print(matches)


def getAvailableWords(brd):
    #create letter constraint set. Map index of letter to legal places
    # when finding an open index, get word, check if it isValid meaning it makes sense vertically
    # spec would be a list of length word, 

    #find a 

    #if letters in the constraint set ensure that it is possible to make a word based on the given letters

    letterConstraintSet = {} 
    for i, e in enumerate(brd):
        if e != "#":
            letterConstraintSet[i] = ([],[])
            for j in range(i,length*height,length):
                if j != "#":
                    letterConstraintSet[i][1].append(j)
            for j in range(i,0,-length):
                if j != "#":
                    letterConstraintSet[i][1].append(j)
            for j in range(i,i+length):
                if j != "#":
                    letterConstraintSet[i][0].append(j)
            for j in range(i,i-i%length,-1):
                if j != "#":
                    letterConstraintSet[i][0].append(j)
    return letterConstraintSet

def putWord(pzl, spec, word):
    p = [*pzl]
    orientation,r,c,_ = spec
    idx = r * length + c
    for i,c in enumerate(word):
        p[idx + orientation * i] = c
    return ''.join(p)

def getBestSpec(words):
    bestChoice = ()
    min = dctSize
    for spec in words:
        l = len(words[spec])
        if l == 0: return False
        if l < min:
            bestChoice = spec; min = len(words[spec])
    return bestChoice

def updateWordChoices(newPzl, newWords, rng = False):
    if not rng:
        for spec in newWords:
            for index, i in enumerate(range(spec[1] * length + spec[2], spec[1] * length + spec[2] + spec[3] * spec[0], spec[0])):
                if newPzl[i] != '-':
                    newWords[spec] = {w for w in newWords[spec] if w[index] == newPzl[i].lower()}
        
    else:
        for spec in newWords:
            for index, i in enumerate(range(spec[1] * length + spec[2], spec[1] * length + spec[2] + spec[3] * spec[0], spec[0])):
                if i not in rng:
                    continue
                if newPzl[i] != '-':
                    newWords[spec] = {w for w in newWords[spec] if w[index] == newPzl[i].lower()}
    return newWords
global finalScore,finalBoard, ogWrds
ogWrds = {}
finalScore = 0
finalScore = ""

def evaluatePzl(p):
    maxLen = 0
    score = 0
    for spec in ogWrds:
        orientation,r,c,size = spec
        maxLen+= size
        wrd = "".join([p[c] for c in range(r*length+c, r*length+c+size*orientation, orientation)])
        if wrd in dct[size]:
            score += size
    return score/maxLen



def bfWords(pzl, words):
    global finalScore,finalBoard
    if not words: return pzl
    bestSpec = getBestSpec(words)
    if bestSpec == False: return ""
    orientation,r,c, size = bestSpec

    choices = words.pop(bestSpec)
    rng = range(r*length+c, r*length+c+size*orientation, orientation)
    for choice in choices:
        newWords = {spec:words[spec]-{choice} for spec in words}
        newPzl = putWord(pzl, bestSpec, choice)
        newWords = updateWordChoices(newPzl,newWords,rng)
        bf = bfWords(newPzl, newWords)
        if bf: return bf
    words[bestSpec] = choices
    return ""

def getSpecs(pzl):
    specList = []
    for r in range(height):
        seenInSpec = False
        spec = []
        start = (None, None)
        for c in range(length):
            idx = r * length + c
            if pzl[idx] == '#':
                    if seenInSpec:
                        seenInSpec = False
                        if not all([pzl[i] != '-' for i in spec]):
                            specList.append((1, start[0], start[1], len(spec)))
                        spec = []
                    else:
                        continue
            else:
                if not seenInSpec:
                    seenInSpec = True
                    start = (r, c)
                spec.append(idx)
        if seenInSpec and not all([pzl[i] != '-' for i in spec]):
            specList.append((1, start[0], start[1], len(spec)))


    for c in range(length):
        seenInSpec = False
        spec = []
        start = (None, None)
        for r in range(height):
            idx = r * length + c
            if pzl[idx] == '#':
                    if seenInSpec:
                        seenInSpec = False
                        if not all([pzl[i] != '-' for i in spec]):
                            specList.append((length, start[0], start[1], len(spec)))
                        spec = []
                    else:
                        continue
            else:
                if not seenInSpec:
                    seenInSpec = True
                    start = (r, c)
                spec.append(idx)
        if seenInSpec and not all([pzl[i] != '-' for i in spec]):
            specList.append((length, start[0], start[1], len(spec)))
    return specList
            




def main():
   
    global pzl,ogWrds
    setGlobals()
    bCount =  bsCount
    p = pzl
    if bCount == (height*length):
        p = "#"*height*length
        printPzl(p)
        return
    #printPzl(p)
    
    

    p = [*p]
    if height%2 and length%2 and bCount%2: 
        p[(height*length)//2] = '#'
        bCount -= 1
    

    for i in range(len(p)):
        if p[i] != '.': continue
        if not isLegalSpace(p, i):
            p[i] = '#'; bCount -= 1
    
    cs = getConnectedSections(p)
    # print([len(c) for c in cc])
    maxL = max([len(c) for c in cs])
    for c in cs:
        if len(c) == maxL: continue
        for i in c:
            pzl[i] = '#'
            bCount -= 1
    p,bCount = fillclosedOffSections(p,bCount)
    p = ''.join(p)
    


    #printPzl(p)
    p = bruteForce(p,bCount).replace(".","-")
    printPzl(p)

    """if p == '-'*16:
        p = "".join(['this',
                     'have',
                     'area',
                     'test'])
        printPzl(p)
        return"""
    specLst = getSpecs(p)
    #cs = getAvailableWords(p)
    wrds = {}
    for spec in specLst:
        wrds[spec] = {w for w in dct[spec[3]]}
    ogWrds = wrds
    

    if p.upper() != p.lower():
        wrds = updateWordChoices(p,wrds)
    
    

    if args[1] == ['15x15']:
        for spec in wrds:
            w = wrds[spec].pop()
            p = putWord(p, spec, w)
            for spec in wrds:
                wrds[spec] = wrds[spec] - {w}
    else: p = bfWords(p, wrds)
    
    score = evaluatePzl(p)
    print(f"Score is: {score}")
    printPzl(p)

    #print(p.count("#"))

if __name__ == "__main__": main()

# Dev Kodre, Pd. 4, 2024