import sys; args = sys.argv[1:]
import time
import re



def main():
    #args = "89x144 2x2 3x3 5x5 8x8 13x13 21x21 34x34 55x55 89x89"
    setGlobals(args)
    b = boardDct
    start = time.time()
    if isValid(bH, bW, blockSet):
        board, num = solve(b, 0, setOfChoices, minDOTS == 0)
        print(output(board, num))
    else: print("No solution")
    print("Totaltime: {0:1.3g}s".format(time.time()-start))

def setGlobals(s):
    global input, posDim, bW, bH, boardDct, blockSet, setOfChoices, minDOTS
    input = re.findall(r'\d+', str(s))

    posDim = {}
    bH, bW = int(input[0]), int(input[1]) 
    boardDct = {y: ''.join(['.' for n in range(bW)]) for y in range(bH)}

    blockSet = {int(index/2): (input[index], input[index + 1]) for index in range(2, len(input), 2)}
    minDotsNum = (bW*bH)-sum((int(input[i])*int(input[i+1])) for i in range(2, len(input), 2))   
    if minDotsNum > 0:
        for i in range(len(blockSet.keys())+1, len(blockSet.keys()) + minDotsNum+1):
            blockSet[i] = ('1', '1')

    choices = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    setOfChoices = {key: choices[key] for key in blockSet}

    
def output(board, num):
    if num == False:
        return 'No Solution'
    if minDOTS > 0:
        seen = set()
        outputList = []
        i = 0
        for row in board.values():
            for ch in row:
                if (ch != '.' and ch not in seen) or (ch == '.' and i not in seen):
                    if ch == '.': outputList.append(posDim.get(i)), seen.add(i)
                    else: outputList.append(posDim.get(ch)), seen.add(ch)
                i += 1
        outputStr = "Decomposition: " + "".join(str(dim[0]) + 'x' + str(dim[1]) + ' ' for dim in outputList)
        return outputStr[:-1]
    
    b = "".join(row for row in board.values())
    seen = set()
    outputList = []
    for row in board.values():
        for ch in row:
            if ch not in seen and ch != '.':
                outputList.append(posDim.get(ch)), seen.add(ch)
    outputStr = "Decomposition: " + "".join(str(dim[0]) + 'x' + str(dim[1]) + ' ' for dim in outputList)
    return outputStr[:-1]

def isPossible(width, height, topleft, board):
    x, y = topleft
    return (x + width) <= bW and (y + height) <= bH and board[y][x:x + width].count('.') >= width

def addBlock(height, width, blockNum, topleft, board):
    x, y = topleft 
    if blockNum == 1000:
        posDim[x*y] = (height, width)
        return board
    else:
        id = setOfChoices[blockNum] 
        posDim[id]=(height, width)

    if isPossible(width, height, topleft, board): 
        boardCopy = board.copy() 
        for toFill in range(y, y + height): boardCopy[toFill] = board[toFill][0:x] + id*width + board[toFill][x + width:]
        return boardCopy

    return False 

def isValid(bW, bH, blx): 
    global minDOTS
    minDOTS = bW * bH
    return False if (minDOTS-sum([int(blx[key][0])*int(blx[key][1]) for key in blx])) < 0 else True

def solve(board, rowNum, choices, dotsBlocksAdded):

    #if sum(row.count('.') for row in board.values()) == 0: 
        #return board, True

    if len(choices) == 0: return board, True

    while '.' not in board.get(rowNum): 
        rowNum += 1
    index = board.get(rowNum).find('.')

    for choice in choices:
        newChoices = choices.copy()
        newChoices.pop(choice) 
        height, width = int(blockSet[choice][0]), int(blockSet[choice][1])

        for rotation in range(2):
            if rotation == 0:
                newpzl = addBlock(height, width, choice, (index, rowNum), board) 
                if newpzl: 
                    result, r = solve(newpzl, rowNum, newChoices, dotsBlocksAdded)
                    if r: return result, True

            if height != width and rotation == 1: 
                width, height = int(blockSet[choice][0]), int(blockSet[choice][1])
                newpzl = addBlock(height, width, choice, (index, rowNum), board)
                if newpzl:
                    result, r = solve(newpzl, rowNum, newChoices, dotsBlocksAdded)
                    if r: return result, True
    return board, False                                

if __name__ == "__main__": main()

# Dev Kodre, Pd. 4, 2024