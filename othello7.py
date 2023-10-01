import sys; args = sys.argv[1:]

#args = '1934'.split(" ")
#ms = [-9, 63, 62, 49, 56, 48, 0, 54, 15, 7, 14, 6, 17, 1, 53, 9]
#args = '.****....*ooox..xxxoxxxoxxoxoxooxoxxxxooo*xxxxoo*.xxxx**.xxxxx..'.replace("*",".").split(" ") #+ [str(ms[l]) for l in range(len(ms)-1,0,-1)]



def main():
    #args = ['x...x.o.x....o.xxxxxooxxoxooooox.oooxoxxoooxxxxxxoxxxxx...ooo...']
    #args = ['4445262046522934122542386030175918_919_4161143496153_54762633121_05441133923_2_8_64033_148221432_310375051582415_75655-157']
    #args = ["ooooooo.ooxxxxx.oxxxxxx.oxxxoxoxoxxoxxoooxoxo.o.ooox.o.oxxxxxx.."]
    #args = '37 43 18 38 46 9 34 54 19 20 52 51 26 44 10 1 39 61 11 17 62 2 50 30 0 41 22 42 53 63 3 58 40 32 45 49 8 25 12 29 24 13 59 48 21 14 31 23 6 4 15 33 56 5 57 16 55 60 -1 7 -1 47'.split(" ")
    
    #setGlobals(args)
    nb = board
    token = defaultToken
    opT = opToken
    nb, token, opT = nb.upper(), token.upper(), opT.upper()
    possibleChoices, flippedSection = findMoves(nb,token)
    if not possibleChoices:
        token, opT = opT, token
        possibleChoices, flippedSection = findMoves(nb,token)
    #No move made B-E
    if (not moves and not verbose) or  verbose:
        printBoard(nb,possibleChoices)
        print("")
        print(nb + calcScore(nb))

        if possibleChoices:
            print(f"Possible moves for {token}: {possibleChoices}")
            print("")
        else:
            #print("No moves possible")
            print("")

    #if not moves:
        #moves.append(quickMove(nb,token))
    
    #new move A-E
    #loop here
    for move in moves:
        if move >= 0:
            if (move == moves[len(moves)-1] and  not verbose) or verbose:
                print(f"{token} plays to {move}") 
            nb = makeMove(nb, token, move, flippedSection)
            #swap tokens after the move
            token, opT = opT, token
            possibleChoices, flippedSection = findMoves(nb,token)
            if not possibleChoices:
                token, opT = opT, token
                possibleChoices, flippedSection = findMoves(nb,token)
            if (move == moves[len(moves)-1] and  not verbose) or verbose:
                printBoard(nb, possibleChoices, move)
                print("")
                print(nb + calcScore(nb))

                if possibleChoices:
                    print(f"Possible moves for {token}: {possibleChoices}")
                    print("")
                else:
                    #print("No moves possible")
                    print("")
                    #break

            #moves.append(quickMove(nb,token))
    #othello 4 part w quick move

    if possibleChoices:
        print(f"my preferred move is: {quickMove(nb,token)}")
        #print(TERMINALalphabeta(nb, token, -65,65, abCache))

        if nb.count(".") < hl:
            ab =TERMINALalphabeta(nb, token, -65,65, abCache)
            print(f"Min Score: {ab[0]}; move sequence: {ab[1:]}")
        else:
            ab =alphabeta(nb, token, -10000,10000, abCache)
            print(f"Min Score: {ab[0]}; move sequence: {ab[1:]}")


    
    
    
        #to here


        


def negamax(brd, tkn, nmCache):
    eTkn = "XO".replace(tkn,"")
    if "." not in brd: return [brd.count(tkn)-brd.count(eTkn)]
    possibleMoves, flippedSections= findMoves(brd,tkn)
    if (brd, tkn) in nmCache:
        return nmCache[(brd, tkn)]
    if not possibleMoves:
        if findMoves(brd,eTkn)[0]:
            if (brd, eTkn) not in nmCache:
                nmCache[(brd, eTkn)] = negamax(brd,eTkn, nmCache)
            nm = nmCache[(brd, eTkn)]
            return [-nm[0]] + nm[1:] + [-1]
        return [brd.count(tkn)-brd.count(eTkn)]
    
    bestSoFar = [-65]
    for mv in possibleMoves:
        newBrd = makeMove(brd,tkn,mv,flippedSections)
        if (newBrd, eTkn) not in nmCache:
            nmCache[(newBrd, eTkn)] = negamax(newBrd,eTkn, nmCache)
        nm = nmCache[(newBrd, eTkn)]
        if -nm[0] > bestSoFar[0]:
            bestSoFar = [-nm[0]] + nm[1:] + [mv]
    nmCache[(brd, tkn)] = bestSoFar
    return bestSoFar


def alphabeta(brd,tkn, alpha, beta, abCache,n=5):
    n-=1
    eTkn = "XO".replace(tkn,"")
    if n <= 0 or "." not in brd: 
        return [evaluate(brd,tkn)]
    possibleMoves, flippedSections= findMoves(brd,tkn)

    if len(possibleMoves) <= 2: n+=1

    if (brd, tkn,alpha,beta) in abCache:
        return abCache[(brd, tkn,alpha,beta)]

    if not possibleMoves:
        if not findMoves(brd,eTkn)[0]:
            return [evaluate(brd,tkn)]

        if (brd, eTkn,-beta,-alpha) not in abCache:
            abCache[(brd, eTkn,-beta,-alpha)] = alphabeta(brd,eTkn,-beta,-alpha,abCache,n)
        ab = abCache[(brd, eTkn,-beta,-alpha)]

        if -ab[0] < alpha: return [alpha-1]
        return [-ab[0]] + ab[1:] + [-1]
    
    bestSoFar = [alpha-1]
    for mv in orderMoves(brd,tkn,possibleMoves,flippedSections):
        newBrd = makeMove(brd,tkn,mv,flippedSections)

        if (newBrd, eTkn,-beta,-alpha) not in abCache:
            abCache[(newBrd, eTkn,-beta,-alpha)] = alphabeta(newBrd,eTkn,-beta,-alpha,abCache,n)
        ab = abCache[(newBrd, eTkn,-beta,-alpha)]
        score = -ab[0]
        if score < alpha: continue
        if score > beta: return[score]
        bestSoFar = [score] + ab[1:] + [mv]
        alpha = score + 1
    
    abCache[(brd, tkn,alpha,beta)] = bestSoFar
    return bestSoFar

def evaluate(brd, tkn):
    corners = {0, 7, 56, 63}
    if (brd, tkn) in evaluateCache:
        return evaluateCache[(brd, tkn)]

    eTkn = "XO".replace(tkn,"")
    if "." not in brd:
        return 100*(brd.count(tkn)-brd.count(eTkn))/64
    score = -100
    #coin parity
    cpScore = 100* (brd.count(tkn)-brd.count(eTkn))/(brd.count(tkn)+brd.count(eTkn))
    #cpScore = brd.count(tkn)-brd.count(eTkn)
    #mobility
    moves,_ = findMoves(brd,tkn)
    eMoves,_ = findMoves(brd,eTkn)
    mobScore = 0
    if moves or eMoves:
        mobScore = 100 * (len(moves)-len(eMoves))/(len(moves)+len(eMoves))
        #mobScore = len(moves)-len(eMoves)
    #corners
    numCorners = len(corners.intersection(moves))
    eNumCorners = len(corners.intersection(eMoves))
    cScore = 100*(numCorners + (brd[0] == tkn) + (brd[7] == tkn) + (brd[56] == tkn) + (brd[63] == tkn) 
    - (eNumCorners + (brd[0] == eTkn) + (brd[7] == eTkn) + (brd[56] == eTkn) + (brd[63] == eTkn)))/4
    #cScore = numCorners + (brd[0] == tkn) + (brd[7] == tkn) + (brd[56] == tkn) + (brd[63] == tkn)
    #cScore -= eNumCorners + (brd[0] == eTkn) + (brd[7] == eTkn) + (brd[56] == eTkn) + (brd[63] == eTkn)
    #stability
    """
    stable = stability(brd,tkn)
    eStable = stability(brd,eTkn)
    sScore = 0
    if stable or eStable:
        sScore = 100*(len(stable) - len(eStable))/(len(stable) + len(eStable))
        #sScore = len(stable) - len(eStable)"""
    

    # cpScore*0.3 + mobScore*0.7 + cScore*0.9 + sScore* 0.2 89.3
    # cpScore*0.3 + mobScore*0.7 + cScore*0.9 + sScore* 0.5 86.7
    # cpScore*0.5 + mobScore*0.7 + cScore*0.9 + sScore* 0.1 88.5
    # cpScore*0.3 + mobScore*0.9 + cScore*0.9 + sScore* 0.1 91.2
    # cpScore*0.3 + mobScore*1 + cScore*0.9 + sScore* 0     90.4
    # cpScore*0.4 + mobScore*1.1 + cScore*1 + sScore* 0.1   92.5
    # cpScore*0.5 + mobScore*1.1 + cScore*1.1 + sScore* 0.1 91.8
    # cpScore*0.4 + mobScore*1 + cScore*1.2 + sScore*0      92.1
    # cpScore*0.3 + mobScore*1.2 + cScore*1 + sScore*0.1    92.8
    # cpScore*0.3 + mobScore*1.2 + cScore*1.1 + sScore*0.1  91.4
    # cpScore*0.3 + mobScore*1.3 + cScore*1 + sScore*0.1    91.2
    # cpScore*0.3 + mobScore*1.2 + cScore*1                 92.9
    # cpScore*0.2 + mobScore*1.2 + cScore*1                 93.2
    # cpScore*0.1 + mobScore*1.2 + cScore*1                 94.4
    # mobScore*1.2 + cScore*1                               91.1
    # cpScore*0.1 + mobScore*1.2 + cScore*1                 94.8
    # cpScore*0.1 + mobScore*1.2 + cScore*1                 95.4
    # cpScore*0.1 + mobScore*1.2 + cScore*0.9               92.6
    # cpScore*0.1 + mobScore*1.3 + cScore*1.1               93.8
    # cpScore*0.1 + mobScore*1.2 + cScore*1.05              95.4
    # cpScore*0.1 + mobScore*1.225 + cScore*1.05            94
    # cpScore*0.1 + mobScore*1.2 + cScore*0.995             93.7

    score = cpScore*0.1 + mobScore*1.2 + cScore*1.05 #+sScore*0.1

    
    evaluateCache[(brd, tkn)] = score

    return score

def TERMINALalphabeta(brd,tkn, alpha, beta, abCache):
    eTkn = "XO".replace(tkn,"")
    if "." not in brd: 
        return [brd.count(tkn)-brd.count(eTkn)]
    possibleMoves, flippedSections= findMoves(brd,tkn)

    if (brd, tkn,alpha,beta) in abCache:
        return abCache[(brd, tkn,alpha,beta)]

    if not possibleMoves:
        if not findMoves(brd,eTkn)[0]:
            return [brd.count(tkn)-brd.count(eTkn)]

        if (brd, eTkn,-beta,-alpha) not in abCache:
            abCache[(brd, eTkn,-beta,-alpha)] = TERMINALalphabeta(brd,eTkn,-beta,-alpha,abCache)
        ab = abCache[(brd, eTkn,-beta,-alpha)]

        if -ab[0] < alpha: return [alpha-1]
        return [-ab[0]] + ab[1:] + [-1]
    
    bestSoFar = [alpha-1]
    for mv in orderMoves(brd,tkn,possibleMoves,flippedSections):
        newBrd = makeMove(brd,tkn,mv,flippedSections)

        if (newBrd, eTkn,-beta,-alpha) not in abCache:
            abCache[(newBrd, eTkn,-beta,-alpha)] = TERMINALalphabeta(newBrd,eTkn,-beta,-alpha,abCache)
        ab = abCache[(newBrd, eTkn,-beta,-alpha)]
        score = -ab[0]
        if score < alpha: continue
        if score > beta: return[score]
        bestSoFar = [score] + ab[1:] + [mv]
        alpha = score + 1
    
    abCache[(brd, tkn,alpha,beta)] = bestSoFar
    return bestSoFar

global stabilityCache, groupCache, isStableCache
stabilityCache, groupCache, isStableCache = {}, {}, {}

def stability(brd, tkn):
    if (brd, tkn) in stabilityCache:
        return stabilityCache[(brd, tkn)]

    stableDisks = []
    visited = set()
    for i,s in enumerate(brd):
        if s == tkn and i not in visited:
            group = connectedGroup(brd, tkn, i, set())
            if isStable(brd, group, tkn):
                stableDisks += group
                visited |= {*group}
    stabilityCache[(brd, tkn)] = stableDisks
    return stableDisks

def connectedGroup(brd, tkn, i,vs):
    if (brd, tkn, i) in groupCache:
        return groupCache[(brd, tkn, i)]
    vs.add(i)
    group = [i]
    for dx in [1,-1,8,-8]:
        x = i + dx
        if x in vs: continue
        elif ((x % 8 == 0 and dx in [1,9,-7]) or 
           (x % 8 == 8 - 1 and dx in [-1,7,-9])):
           continue
        elif 0<=x<64 and brd[x] == tkn:
           group+= connectedGroup(brd, tkn, x,vs)
    groupCache[(brd, tkn, i)] = group
    return group

def isStable(brd, group, tkn):
    #if (brd, group, tkn) in isStableCache:
        #return isStableCache[(brd, group, tkn)]
    #REMEMBER TO MAKE "ox" UPPERCASE
    eTkn = "XO".replace(tkn,"")
    for i in group:
        for dx in [1,-1,8,-8]:
            x = i + dx
            if ((x % 8 == 0 and dx in [1,9,-7]) or 
           (x % 8 == 8 - 1 and dx in [-1,7,-9])):
                continue
            elif 0<=x<64 and brd[x] == eTkn:
                j = i
                while 0<=j<64:
                    if ((j % 8 == 0 and -dx in [1,9,-7]) or 
                    (j % 8 == 8 - 1 and -dx in [-1,7,-9])):
                        break
                    if brd[j] == ".":
                        #isStableCache[(brd, group, tkn)] = False
                        return False
                    j += -dx
    #isStableCache[(brd, group, tkn)] = True
    return True








def turn(b):
   cnt = 0
   for x in b:
        if(x == "."):
            cnt = cnt + 1
   if(cnt % 2 != 0):
        return "O"
   else:
        return "X"

def printBoard(b,possibleChoices, mv = None):
    s=b
    if possibleChoices:
        for i in possibleChoices:
            s = s[:i] + "*" + s[i+1:]
    s = s.lower()
    if mv:
        s = s[:mv] + s[mv].upper() + s[mv+1:]
        
    print("\n".join([s[x : x + side] for x in range(0,length,side)]))

def findMoves(b,token):
    b = b.upper()
    token = token.upper()
    index = 0
    choiceSet = set()
    #global flippedSection 
    flippedSection = []
    directions = [1,-1,8,-8,9,-9,7,-7]
    opT = {"X","O"} - {token.upper()}
    opT = "".join(opT)
    if (b, token) in moveCache:
        return moveCache[(b, token)]
    for i,s in enumerate(b):
        if s == ".":
    #for i in dotSet:
            for x in directions:
                index = i
                flag = False
                while 0<= index < length:
                    if ((index % side == 0 and x in [-1,-9,7]) or
                        (index % side == side - 1 and x in [1,-7,9] )):
                        break
                    if b[index] == token: break
                    if flag and b[index] == ".": break
                    flag = True
                    index += x
                if 0 <= index < length and b[index] == token and b[index - x] != ".":

                    flippedSection.append((index,i,-x))
                    choiceSet.add(i)
    moveCache[(b, token)] = (choiceSet,flippedSection)
    


    return choiceSet,flippedSection
global makeMoveCache
makeMoveCache = {}
def makeMove(b, token, move, flippedSection):
    #dotSet.remove(move)
    if (b,token,move) in makeMoveCache: return makeMoveCache[(b,token,move)]
    b=b.upper()
    token = token.upper()
    seenDirection = set()
    start = 0
    for sect in flippedSection:#[move]:
        firstOccurance = False
        if move == sect[1] and sect[2] not in seenDirection:
            start, end, direction = sect
            while end != start:
                if b[end] != token:
                    if b[end] != ".":
                        firstOccurance = True
                    b = b[:end] + token + b[end+1:]
                    
                elif firstOccurance: 
                    break
                end -= direction
            seenDirection.add(direction)        
    makeMoveCache[(b,token,move)] = b
    return b

def quickMove(board, token):
    global hl
    if board.lower() in theoryDct:
        return theoryDct[board.lower()]
    
    if not board: 
        board = ('.'*27 + "ox......xo" + '.'*27).upper()
        hl = token
    else:
        board = board.upper()
        token = token.upper()
        if 0 < board.count(".") <hl:
            return TERMINALalphabeta(board, token, -65, 65, abCache)[-1]
        ab = alphabeta(board, token, -10000, 10000, abCache)
        #print(ab)
        return ab[-1]
        #possibleChoices,_ = findMoves(board,token)
        #sortedMoves = orderMoves(board, token, possibleChoices)
        #return sortedMoves[0]


def orderMoves(board, token, possibleChoices,fs):
    if (board, token) in orderCache:
        return orderCache[(board, token)]

    cornerToEdges = {0: {1,2,3,4,5,6,7,8,16,24,32,40,48,56},
             7: {0,1,2,3,4,5,6,15,23,31,39,47,55,63},
             56: {0,8,16,24,32,40,48,57,58,59,60,61,62,63},
             63: {7,15,23,31,39,47,55,56,57,58,59,60,61,62}}
    edgeToCorner = {edgeInd: corner for corner in cornerToEdges for edgeInd in cornerToEdges[corner]}
    corners = {0, 7, 56, 63}
    aroundCorner = {1: 0, 8: 0, 9: 0, 6: 7, 14: 7, 15: 7, 48: 56, 49: 56, 57: 56, 54: 63, 55: 63, 62: 63}


    
    opT = {"O","X"} - {token}
    opT = "".join(opT)
    sortedMoves = []

    for move in possibleChoices:
        score = 0
        if move in corners:
            score += 100
        elif move in edgeToCorner:
            if board[edgeToCorner[move]] == token:
                score += 0
        for n in [1,-1,8,-8]:#,9,-9,7,-7]:
            if move+n >= 0 and move+n < length and board[move+n] == '.': score -= 1
        if move in aroundCorner:
            if board[aroundCorner[move]] == '.':
                score = -100
            elif board[aroundCorner[move]] == opT:
                score = -99
        #mobility
        """newB = makeMove(board,token,move,fs)

        eChoices,_ = findMoves(newB,opT)
        choices,_ = findMoves(newB,token)
        if eChoices or choices:
            score += 4*(len(choices) - len(eChoices)) / (len(choices) + len(eChoices))"""
        sortedMoves.append((score, move))
        
    
    sortedMoves.sort(reverse=True)
    moves = [t[1] for t in sortedMoves]
    orderCache[(board, token)] = moves
    return moves

def calcScore(b):
    x = b.count("X")
    y = b.count("O")
    return f"  {x}/{y}"       
            
def condensePath(nums):
    nums = nums.replace("_", "0")
    #if not nums.isnumeric():
        #return
    for i in range(0,len(nums),2):
        if nums[i] != "-" and nums[i+1] != "-":
            moves.append(int(nums[i] + nums[i+1]))
        


#def setGlobals(s):
s = args
global side, length, board, defaultToken, moves, opToken, nmCache,verbose,abCache, status, moveCache, hl
global dotSet, orderCache, evaluateCache, thoeryDct
theoryDct = {
'...........................ox......xo...........................':19,
'..................ox.......ox......xo...........................':26,
'..................ooo.....xxo......xo...........................':45,
'..................ooo....oooo......xx........x..................':21,
'..................ooooo..ooox......xx........x..................':12,
'............xo....ooooo..ooox......xx........x..................':10,
'..........xooo....ooooo..ooox......xx........x..................':34,
'..........xooo...oooooo..oxox.....xxx........x..................':3,
'...x......xxoo...ooxooo..ooooo....xxx........x..................':23,
'...x......xxoo...ooxxoxx.oooooo...xxx........x..................':32,
'...x......xxoo...oxxxoxx.oooooo.xoxxx........x..................':40,
'...x......xxoo...oxxxoxx.oxoooo.xooxx...xo...x..................':16,
'...x......xxoo..xxxxxoxx.oxoooo.xooooo..xo...x..................':24,
'...x......xxoo..xxxxxoxxxxxoooo.xooooo..xo...o.......o..........':31,
'..ox......oxoo..xxoxxoxxxxoxxxxxxooooo..xo...o.......o..........':5,
'..ox.x....ooxx..xxoxoxxxxxoxxoxxxoooooo.xo...o.......o..........':4,
'..oxxx...ooxxx..xooxoxxxxoooxoxxxoooooo.xo...o.......o..........':1,
'.xxxxx...oooooo.xooxoooxxooooooxxoooooo.xo...o.......o..........':50,
'.xxxxx...oooooo.xooxoooxxooooooxxoooooo.xo...o...ox..o..........':58,
'.xxxxx...oooooo.xooxoooxxooooooxxoooooo.xo...o...xo..o....xo....':60,
'.xxxxx...oooooo.xooxoooxxooooooxxoooooo.xo...o..ooo..o....xxx...':56,
'.xxxxx...oooooo.xooxoooxxooooooxxoooooo.xo...o..xoo..o..x.xxx...':6,
'.xxxxxx..ooooxo.xooxxooxxooxoooxxoooooo.xxo..o..xoo..o..x.xxx...':0,
'xxxxxxx.oooooxo.xoxxxooxxooxoooxxoooooo.xxo..o..xoo..o..x.xxx...':57,
'xxxxxxx.oooooxo.xoxxxooxxooxoooxxoooooo.xxo..o..xxo..o..xxxxx...':51,
'xxxxxxx.oooooxo.xoxxxooxxooxoooxxxooooo.xxx..o..xxxx.o..xxxxx...':43,
'xxxxxxx.oooooxo.xoxxxooxxxoxoooxxxxoooo.xxxxoo..xxxx.o..xxxxx...':47,
'xxxxxxx.oooooxo.xoxxxooxxxoxoxoxxxxoooo.xxxxoooxxxxx.o..xxxxx...':39,
'xxxxxxx.ooooxxo.xoxxxxoxxxoxoxxxxxxxxoxxxxxxoooxxxxx.x.oxxxxx...':63,
'xxxxxxx.ooooxxo.xoxxxxoxxxoxoxxxxxxxxoxxxxxxoooxxxxx.o.xxxxxxo.x':62,
'xxxxxxx.ooooxxo.xoxxxxoxxxoxoxxxxxxxooxxxxxxoooxxxxxox.xxxxxxxxx':54,
'xxxxxxx.ooooxxo.xoxxxxoxxxoxoxxxxxxxxoxxxxxxoxxxxxxxoxxxxxxxxxxx':15,
'...................x.......xx......xo...........................':34,
'...................x.......xx.....xoo....x......................':21,
'...................x.o.....xxx....xoo....x......................':20,
'...........x.......xxo.....xox....xoo....x......................':37,
'...........x.......xxxx....xoo....xooo...x......................':13,
'...........x.o.....xxox....xxxx...xooo...x......................':33,
'...........xxo.....xxxx....xxxx..ooooo...x......................':4,
'....o......xoo.....xoxx..x.xoxx..xoooo...x......................':2,
'..o.o......ooo.....xoxx..x.xoxx..xxxxxx..x......................':23,
'..oxo......xxo.....xoxoo.x.xoxx..xxxxxx..x......................':31,
'..oxxx.....xxx.....xoxoo.x.xoooo.xxxxxx..x......................':6,
'..ooooo....xxo.....xoxoo.x.xooxo.xxxxxxx.x......................':47,
'..ooooo....xxo.....xoxoo.x.xooxo.xxxxxxo.x....xo................':54,
'..ooooo....xxxx....xoxoo.x.xoooo.xxxxxoo.x....oo......o.........':7,
'..oooooo...xxxxx...xooxo.x.xoxoo.xxxxxoo.x....oo......o.........':26,
'..oooooo..xxoxxx...xooxo.xooxxoo.xxxxxoo.x....oo......o.........':18,
'..oooooo..oooxxx.xxxxxxo.xxoxxoo.xxxxxoo.x....oo......o.........':16,
'..oooooo.xxxxxxxoxxooooo.xxxxxoo.xxxxxoo.x....oo......o.........':1,
'.ooooooo.xoxxxxxoxxoooox.xxxxxox.xxxxxox.x....xx......ox........':63,
'.ooooooo.xoxxxxooxxooooo.xxxxxoo.xxxxxoo.x....xo......xo......xo':24,
'.ooooooo.xoxxxxoooxooooooxooooooxxxxxxoo.x....xo......xo......xo':0,
'ooooooooxxxxxxxoxxooooooxxxoooooxxxxxxoo.x....xo......xo......xo':40,
'oooooooooxxxxxxooxoooooooxooooooooxxxxooox....xo......xo......xo':53,
'oooooooooxxxxxxooxoooooooxooooooooxxxxooox..x.oo.....xoo......xo':61,
'oooooooooxxxxxxooxoooooooxooooooooxxxxooox..x.oo.....xoo.....ooo':60,
'oooooooooxxxxxxooxoooooooxooooooooxxxxooox..x.oo.....ooo....oooo':45,
'oooooooooxxxxxxooxoooooooxooooooooxxooooox..xooo.....ooo....oooo':52,
'oooooooooxxxxxxooxoooooooxooooooooxxooooox..oooo....oooo....oooo':50,
'oooooooooxxxxxxooxoooooooxooooooooxxooooox..oooox.o.oooo....oooo':56,
'oooooooooxxxxxxooxoooooooxooooooooxxooooox..ooooo.x.ooooo..xoooo':49,
'oooooooooxxxxxxooxoooooooxoooooooxxxooooox..oooooxx.ooooox.xoooo':58,
'oooooooooxxxxxxooxoooooooxoooooooxxxooooox..oooooox.oooooooooooo':42,
'oooooooooxxxxxxooxoxoooooxoxooooooxxoooooooxooooooo.oooooooooooo':51}

evaluateCache = {}
orderCache = {}
verbose = False
dotSet = {}
moveCache = {}
status = {"moveCache":0}
abCache = {}
nmCache = {}
#global flippedSection ; flippedSection = {}
hl= 14
board = ""
defaultToken = "."
moves = []
#new way of input
for e in s:
    if e.upper() == "V":
        verbose = True
        continue
    if "HL" in e:
        hl = int(e[2:])
    if "." in e:
        board = e.upper()
    elif e.upper() in ["X","O"]:    
        defaultToken = e.upper()
    elif len(e) <= 2 and e.isnumeric():
        moves.append(int(e))
    else:
        condensePath(e)

    
tokens = {"X", "O"}

if board == "":
    board = ('.'*27 + "ox......xo" + '.'*27).upper()
if defaultToken == ".":
    defaultToken = turn(board)

#dotSet = {i for i in range(len(board)) if board[i] == "."}

opToken = tokens - {defaultToken}
opToken = "".join(opToken)
length = len(board)
side = int(length**0.5)
    
    
    
    #choiceSet = set() 

if __name__ == "__main__": main()

# Dev Kodre, Pd. 4, 2024