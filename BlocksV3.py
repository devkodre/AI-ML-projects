import sys; args = sys.argv[1:]
import time
import re

# input
def setGlobals(s):
    
    global input, BOARDW, BOARDH, board, blocks, choices, ATPOSITION
    ATPOSITION = {}
    input = re.findall(r'\d+', str(s))

    BOARDW, BOARDH = int(input[1]), int(input[0]) # board width and height
    board = {y: ''.join(['.' for n in range(BOARDW)]) for y in range(BOARDH)}
    blocks = {int(index/2): (input[index], input[index + 1]) for index in range(2, len(input), 2)}
    replace = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    choices = {key: replace[key] for key in blocks}
    global USEDCHOICES
    USEDCHOICES = set()
    #global dotsBlocksAdded
    #dotsBlocksAdded = False


# helper methods:

# one time calls:
def isValid(w, h, blx):
    global DOTSREMAINING
    totalArea = w*h
    DOTSREMAINING = totalArea-sum([int(blx[key][0])*int(blx[key][1]) for key in blx])
    return False if DOTSREMAINING < 0 else True
    
def output(board, num):
    
    if DOTSREMAINING > 0:
        print(board)
        seen = set()
        outputList = []
        w = 0
        for row in board.values():
            for ch in row:
                if (ch != '.' and ch not in seen) or (ch == '.' and w not in seen):
                    if ch == '.':
                        outputList.append(ATPOSITION.get(w)), seen.add(w)
                    else:
                        outputList.append(ATPOSITION.get(ch)), seen.add(ch)
                w += 1
        outputStr = "Decomposition: " + "".join(str(dim[0]) + 'x' + str(dim[1]) + ' ' for dim in outputList)
        return outputStr[:-1]
    
    b = "".join(row for row in board.values())
    print(b)
    seen = set()
    outputList = []
    for row in board.values():
        for ch in row:
            if ch not in seen and ch != '.':
                outputList.append(ATPOSITION.get(ch)), seen.add(ch)
    outputStr = "Decomposition: " + "".join(str(dim[0]) + 'x' + str(dim[1]) + ' ' for dim in outputList)
    return outputStr[:-1]

# repeatedly called:
def canAdd(width, height, topleft, board):
    x, y = topleft
    if (x + width) > bWIDTH: # if adding block goes off the board width
    #if (x + width) > x + bWIDTH - x%bWIDTH - 1:
        return False
    elif (y + height) > bHEIGHT: # if adding block goes off the board height
    #elif (y + height) > len(board)*len(board[0]) - 1:
        return False
    elif board[y][x:x + width].count('.') < width: # if there is overlap
        return False
    return True

def addBlock(height, width, blockNum, topleft, board): # height, width, block id, location, board
    x, y = topleft # column/row
    if blockNum == 1000:
        ATPOSITION[x*y] = (height, width)
        return board
    else:
        marker = CHOICES[blockNum] # id to denote puzzle
        ATPOSITION[marker]=(height, width)

    # check if possible to add block:
    if canAdd(width, height, topleft, board): # if it is possible to add, add it
        boardCopy = board.copy() # copy necessary because it's a dict
        for dep in range(y, y + height): # modify each row
            boardCopy[dep] = board[dep][0:x] + marker*width + board[dep][x + width:]
        return boardCopy

    return False # if the block doesn't fit in this space


# method to find puzzle solution:
def solve(board, currentRow, choices, dotsBlocksAdded):
    #if DOTSREMAINING != 0 and sum(row.count('.') for row in board.values()) == DOTSREMAINING: # if the bottom row is filled then its solved
        #return board, True

    if sum(row.count('.') for row in board.values()) == DOTSREMAINING: # if the bottom row is filled then its solved
        return board, True

    if not dotsBlocksAdded:
        for i, vals in enumerate(board.values()):
            for j, v in enumerate(vals):
                if v == '.':
                    addBlock(1, 1, 1000, (i, j), board)
        dotsBlocksAdded = True

    if '.' in board[currentRow]: # if there's an empty space in current row its topleft
        nextOpenIndex = board[currentRow].find('.')
    else:
        while '.' not in board[currentRow]: # otherwise find row with empty space
            currentRow += 1
        nextOpenIndex = board[currentRow].find('.')

    for choice in choices:
        newChoices = choices.copy()
        newChoices.pop(choice) # copy of choices without choice
        height, width = int(BLOCKS[choice][0]), int(BLOCKS[choice][1])

        for rotation in range(2):
            if rotation == 0:
                newBoard = addBlock(height, width, choice,
                                    (nextOpenIndex, currentRow), board) # create board with added block
                if newBoard: # if it's actually made it's valid so pass it on
                    result, r = solve(newBoard, currentRow, newChoices, dotsBlocksAdded)
                    if r:
                        return result, True

            if height != width and rotation == 1: # if its not a square try rotating
                width, height = int(BLOCKS[choice][0]), int(BLOCKS[choice][1])
                newBoard = addBlock(height, width, choice,
                                    (nextOpenIndex, currentRow), board)
                if newBoard:
                    result, r = solve(newBoard, currentRow, newChoices, dotsBlocksAdded)
                    if r:
                        return result, True
    return board, False                                

# output
def main():
    str = args
    str = "56X56 32x11 32 10 28x14 28 7 28x6 21 18 21 18 21x14 21 14 17x14 14 4 10x7"
    start = time.time()
    setGlobals(str)
    if isValid(BOARDH, BOARDW, blocks):
        b = placeBlock(int(blocks[1][0]),int(blocks[1][1]),1,(0,0),board)
        if not b:
            b = placeBlock(int(blocks[1][1]),int(blocks[1][0]),1,(0,0),board)
        del choices[1]

        b = output(solve(b, 0, choices))
        print("Totaltime: {0:1.3g}s".format(time.time()-start))
        return b
    else:
        print("Totaltime: {0:1.3g}s".format(time.time()-start))
        return 'Blocks do not fit area.'
main()