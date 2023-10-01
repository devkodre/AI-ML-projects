import sys; args = sys.argv[1:]

#args = ['xxxxxxxx.xxoxoooxxxooxooxoxoxoooooxxoxooooxoxoooooxxoooox.xxxxxx']
#args = '37 43 18 38 46 9 34 54 19 20 52 51 26 44 10 1 39 61 11 17 62 2 50 30 0 41 22 42 53 63 3 58 40 32 45 49 8 25 12 29 24 13 59 48 21 14 31 23 6 4 15 33 56 5 57 16 55 60 -1 7 -1 47'.split(" ")



def main():
    #args = ['x...x.o.x....o.xxxxxooxxoxooooox.oooxoxxoooxxxxxxoxxxxx...ooo...']
    #args = ['4445262046522934122542386030175918_919_4161143496153_54762633121_05441133923_2_8_64033_148221432_310375051582415_75655-157']
    #args = ["ooooooo.ooxxxxx.oxxxxxx.oxxxoxoxoxxoxxoooxoxo.o.ooox.o.oxxxxxx.."]
    #args = '37 43 18 38 46 9 34 54 19 20 52 51 26 44 10 1 39 61 11 17 62 2 50 30 0 41 22 42 53 63 3 58 40 32 45 49 8 25 12 29 24 13 59 48 21 14 31 23 6 4 15 33 56 5 57 16 55 60 -1 7 -1 47'.split(" ")
    
    #setGlobals(args)
    nb = board
    token = defaultToken
    opT = opToken
    possibleChoices = findMoves(nb,token)
    if not possibleChoices:
        token, opT = opT, token
        possibleChoices = findMoves(nb,token)
    #No move made B-E
    printBoard(nb,possibleChoices)
    print("")
    print(nb + calcScore(nb))

    if possibleChoices:
        print(f"Possible moves for {token}: {possibleChoices}")
        print("")
    else:
        print("No moves possible")
        print("")
    
    #new move A-E
    #loop here
    for move in moves:
        if move >= 0:
            print(f"{token} plays to {move}") 
            nb = makeMove(nb, token, move)
            #swap tokens after the move
            token, opT = opT, token
            possibleChoices = findMoves(nb,token)
            if not possibleChoices:
                token, opT = opT, token
                possibleChoices = findMoves(nb,token)
            printBoard(nb, possibleChoices)
            print("")
            print(nb + calcScore(nb))

            if possibleChoices:
                print(f"Possible moves for {token}: {possibleChoices}")
                print("")
            else:
                print("No moves possible")
                print("")
    #othello 4 part w quick move

    if possibleChoices:
        print(f"my preferred move is: {quickMove(nb,token)}")


    
    
    
        #to here

def quickMove(board, token):
    cornerToEdges = {0: {1,2,3,4,5,6,7,8,16,24,32,40,48,56},
             7: {0,1,2,3,4,5,6,15,23,31,39,47,55,63},
             56: {0,8,16,24,32,40,48,57,58,59,60,61,62,63},
             63: {7,15,23,31,39,47,55,56,57,58,59,60,61,62}}
    edgeToCorner = {edgeInd: corner for corner in cornerToEdges for edgeInd in cornerToEdges[corner]}
    corners = {0, 7, 56, 63}
    aroundCorner = {1: 0, 8: 0, 9: 0, 6: 7, 14: 7, 15: 7, 48: 56, 49: 56, 57: 56, 54: 63, 55: 63, 62: 63}


    board = board.upper()
    token = token.upper()
    opT = {"O","X"} - {token}
    opT = "".join(opT)
    possibleChoices = findMoves(board,token)
    sortedMoves = []

    # move into corner always
    '''
    for c in corners:
        if c in possibleChoices:
            return c
    # if next to corner dont move
    for m in [1,8,9,6,14,15,48,49,57,62,54,55]:
        if m in possibleChoices and len(possibleChoices) > 1:
            possibleChoices.remove(m)
    move = random.choice([*possibleChoices])
    return move
'''
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
    
        sortedMoves.append((score, move))
    sortedMoves.sort(reverse=True)
    return sortedMoves[0][1]
        







def turn(b):
   cnt = 0
   for x in b:
        if(x == "."):
            cnt = cnt + 1
   if(cnt % 2 != 0):
        return "O"
   else:
        return "X"

def printBoard(b,possibleChoices):
    s=b
    if possibleChoices:
        for i in possibleChoices:
            s = s[:i] + "*" + s[i+1:]
    print("\n".join([s[x : x + side] for x in range(0,length,side)]))

def findMoves(b,token):
    b = b.upper()
    token = token.upper()
    index = 0
    choiceSet = set()
    global flippedSection
    flippedSection = []
    directions = [1,-1,8,-8,9,-9,7,-7]
    opT = {"X","O"} - {token.upper()}
    opT = "".join(opT)
    for i,s in enumerate(b):
        if s == token:
            for x in directions:
                index = i
                while 0<= index < length and b[index] != ".":
                    if ((index % side == 0 and x in [-1,-9,7]) or
                        (index % side == side - 1 and x in [1,-7,9] )):
                        break
                    index += x
                if 0 <= index < length and b[index] == "." and b[index - x] == opT:
                    flippedSection.append((i,index,x))
                    choiceSet.add(index)


    return choiceSet# ,flippedSection

def makeMove(b, token, move):
    b=b.upper()
    token = token.upper()
    seenDirection = set()
    for sect in flippedSection:
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
            
    
    return b

    


def calcScore(b):
    x = b.count("X")
    y = b.count("O")
    return f"  {x}/{y}"       
            
def condensePath(nums):
    nums = nums.replace("_", "0")
    if not nums.isnumeric():
        return
    for i in range(0,len(nums),2):
        if nums[i] != "-" and nums[i+1] != "-":
            moves.append(int(nums[i] + nums[i+1]))
        


#def setGlobals(s):
    
s = args
global side, length, board, defaultToken, moves, opToken#, flippedSection
#flippedSection = []
board = ""
defaultToken = "."
moves = []
#new way of input
for e in s:
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

opToken = tokens - {defaultToken}
opToken = "".join(opToken)
length = len(board)
side = int(length**0.5)
    
    
    
    #choiceSet = set() 

if __name__ == "__main__": main()

# Dev Kodre, Pd. 4, 2024