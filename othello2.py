import sys; args = sys.argv[1:]


def main():
    #args = ['...ox.oxox.o..ox.oxxxxox.ooxxxoxo.xoxxxxx.oxox.x.x.xxxx.o.xo..o.', 'o', 'E8']
    #args = ['19','34','41']
    #args = "37 45 44 43 51 21 46 59 26 42 20 19 10 18 49 56 34 29 9 2 14 7 22 15 13 6 41 48 1 0 12 5 58 57 11 3 33 40 25 50 52 60 23 31 32 24 53 38 54 17 39 30 8 16 4 63 55 47 61 62".split(" ")
    #args = ["....................x......xxx....xxxxx.....xo..................", "D6", "e7"]
    setGlobals(args)
    nb = board
    token = defaultToken
    opT = opToken
    possibleChoices,flippedSections = findChoices(nb,token,opT)
    if not possibleChoices:
        token, opT = opT, token
        possibleChoices,flippedSections = findChoices(nb,token,opT)
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
            nb = makeMove(nb, move, token, flippedSections)
            #swap tokens after the move
            token, opT = opT, token
            possibleChoices,flippedSections = findChoices(nb,token,opT)
            if not possibleChoices:
                token, opT = opT, token
                possibleChoices,flippedSections = findChoices(nb,token,opT)
            printBoard(nb, possibleChoices)
            print("")
            print(nb + calcScore(nb))

            if possibleChoices:
                print(f"Possible moves for {token}: {possibleChoices}")
                print("")
            else:
                print("No moves possible")
                print("")
    
    
        #to here


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

def findChoices(b,token,opT):
    index = 0
    choiceSet = set()
    flippedSection = []
    directions = [1,-1,8,-8,9,-9,7,-7]
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


    return choiceSet,flippedSection

def makeMove(b, move, token, flippedSection):
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
            



def setGlobals(s):
    

    global side, length, board, defaultToken, moves, opToken
    board = ""
    defaultToken = "."
    moves = []
    for e in s:
        if len(e) > 3:
            board = e.upper()
        elif e[0] == '-':
            moves.append(int(e))
        elif len(e)>1 or e in {'0','1','2','3','4','5','6','7','8','9'}:
            if e.isnumeric():
                moves.append(int(e))
            else:
                moves.append(ord(e[0].upper()) - 65 + 8*(int(e[1])-1))
        else:
            defaultToken = e.upper()
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