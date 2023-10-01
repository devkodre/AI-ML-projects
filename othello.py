import sys; args = sys.argv[1:]
import time
import re


def main():
    #args = ['....x...o..x..ox.oxx.oox.xoxxxox..xoxxxx..oxox.x.o.xxxx.o.xo..o.', 'x']
    setGlobals(args)
    if board:
        possibleChoices = findChoices(board,defaultToken)
    
        printBoard(board,possibleChoices)
        if possibleChoices:
            print(f"Possible moves: {possibleChoices}")
        else:
            print("No moves possible")
    else:
        print("No moves possible")
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
    
    for i in possibleChoices:
        b = b[:i] + "*" + b[i+1:]
    print("\n".join([b[x : x + side] for x in range(0,length,side)]))

def findChoices(b,token):
    index = 0
    choiceSet = set()
    for i,s in enumerate(b):
        if s == token:
            index = i
            while index % side != side-1 and 0<= index < length and b[index]!= ".":
                index -= 1
            if index % side != side-1:
                if b[index + 1] == opToken:
                    choiceSet.add(index)

            index = i
            while 0<= index < length and b[index]!= ".":
                index += 1
            
            if index % side != 0:
                if b[index - 1] == opToken:
                    choiceSet.add(index)

            index = i

            while 0<= index < length and b[index]!= ".":
                index -= side
            if 0<= index < length:
                if b[index + side] == opToken:
                    choiceSet.add(index)

            index = i

            while 0<= index < length and b[index]!= ".":
                index += side
            if 0<= index < length:
                if index - side >= 0 and b[index - side] == opToken:
                    choiceSet.add(index)

            index = i

            while 0<= index < length and b[index]!= ".":
                if index % side ==0:
                    break
                index -= side +1

            if 0<= index < length and index % side != side-1 and b[index] == ".":
                if b[index + side+1] == opToken:
                    choiceSet.add(index)
            
            index = i
            while index % side != side - 1 and 0<= index < length and b[index]!= ".":
                index -= side -1

                if 0<= index < length and index % side != 0 and b[index] == ".":
                    if index + side-1 < length and b[index + side-1] == opToken:
                        choiceSet.add(index)
            
            index = i

            while 0<= index < length and b[index]!= ".":
                index += side -1
            if 0<= index < length and index % side != side-1:
                if index - side+1 >= 0 and b[index - side+1] == opToken:
                    choiceSet.add(index)
            
            index = i

            while 0<= index < length and b[index]!= ".":
                index += side +1
            if 0<= index < length and index % side != 0:
                if index - side-1 >= 0 and b[index - side-1] == opToken:
                    choiceSet.add(index)
            
            index = i

    return choiceSet

            
            



def setGlobals(s):
    

    global side, length, board, defaultToken, moves, opToken

    tokens = {"X", "O"}
    if  s:
        if len(s[0])>1:
            board = s[0].upper()
        else:
            defaultToken = s[0]
            board = ('.'*27 + "ox......xo" + '.'*27).upper()

        if len(s)>1:
            defaultToken = s[1].upper()
        else:
            defaultToken = turn(board)
        if len(s)>2:
            moves = s[2]
    else:
        board = ('.'*27 + "ox......xo" + '.'*27).upper()
        defaultToken = 'X'


    
    opToken = tokens - {defaultToken}
    opToken = str(*opToken)
    length = len(board)
    side = int(length**0.5)
    
    
    
    #choiceSet = set() 

if __name__ == "__main__": main()

# Dev Kodre, Pd. 4, 2024