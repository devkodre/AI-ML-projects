import sys; args = sys.argv[1:]
import time
import re

# input
#str = sys.argv[1:]
def setGlobals(s):
    
    global input, BOARDW, BOARDH, board, blocks, choices, ATPOSITION
    ATPOSITION = {}
    input = re.findall(r'\d+', str(s))

    BOARDW, BOARDH = int(input[1]), int(input[0]) # board width and height
    board = {y: ''.join(['.' for n in range(BOARDW)]) for y in range(BOARDH)}
    blocks = {int(index/2): (input[index], input[index + 1]) for index in range(2, len(input), 2)}
    replace = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    choices = {key: replace[key] for key in blocks}


def isValid(w, h, blx):
    global DOTSREMAINING
    totalArea = w*h
    DOTSREMAINING = totalArea-sum([int(blx[key][0])*int(blx[key][1]) for key in blx])
    return False if DOTSREMAINING < 0 else True


def printBoard(b):
    for key in b: 
        print(' '.join(b[key])) 
    if BOARDW > 30 or BOARDH > 30:
        print('\n')
    else:
        print('')


def output(board):
    if board == False:
        return 'No solution.'
    seen = set()
    outputList = []
    for row in board.values():
        for ch in row:
            if ch not in seen and ch!='.':
                outputList.append(ATPOSITION.get(ch)), seen.add(ch)
    outputStr = "Decomposition: " + "".join(str(dim[0]) + 'x' + str(dim[1]) + ' ' for dim in outputList)
    return outputStr[:-1]


def solve(board, currentRow, choices):
    if isValid(BOARDH, BOARDW, blocks):
        b = placeBlock(int(blocks[1][0]),int(blocks[1][1]),1,(0,0),board)
        if not b:
            b = placeBlock(int(blocks[1][1]),int(blocks[1][0]),1,(0,0),board)
        del choices[1]
        return output(solve1(b, currentRow, choices))
    else:
        return 'Blocks do not fit area.'



def isPossible(w, h, topLeftCorner, board):
    x, y = topLeftCorner
    if (x + w) > BOARDW: 
        return False
    elif (y + h) > BOARDH: 
        return False
    elif board[y][x:x + w].count('.') < w: 
        return False
    return True


def placeBlock(h, w, n, topLeftCorner, board):
    x, y = topLeftCorner 
    marker = choices[n] 
    ATPOSITION[marker]=(h, w)

    if isPossible(w, h, topLeftCorner, board): 
        boardCopy = board.copy() 
        for dep in range(y, y + h): 
            boardCopy[dep] = board[dep][0:x] + marker*w + board[dep][x + w:]
        return boardCopy

    return False 
def findNextChoice(board, rowNum):
    if '.' in board[rowNum]: 
        return board[rowNum].find('.'), rowNum
    else:
        while '.' not in board[rowNum]: 
            rowNum += 1
        return board[rowNum].find('.'), rowNum
    


def solve1(board, rowNum, choices):
    if sum(row.count('.') for row in board.values()) == DOTSREMAINING: 
        return board

    index, rowNum = findNextChoice(board,rowNum)
    

    for choice in choices:
        newChoices = choices.copy()
        newChoices.pop(choice) 
        height, width = int(blocks[choice][0]), int(blocks[choice][1])

        for rotation in range(2):
            if rotation == 0:
                newBoard = placeBlock(height, width, choice,
                                    (index, rowNum), board) 
                if newBoard: 
                    if len(choices) < 3 :printBoard(newBoard)
                    result = solve1(newBoard, rowNum, newChoices)
                    if result:
                        return result

            if height != width and rotation == 1: 
                width, height = int(blocks[choice][0]), int(blocks[choice][1])
                newBoard = placeBlock(height, width, choice,
                                    (index, rowNum), board)
                if newBoard:
                    if len(choices) < 3 :printBoard(newBoard)
                    result = solve1(newBoard, rowNum, newChoices)
                    
                    if result:
                        return result
    return False # no solution

def main():
    str = args
    str = "56X56 32x11 32 10 28x14 28 7 28x6 21 18 21 18 21x14 21 14 17x14 14 4 10x7"
    start = time.time()
    setGlobals(str)
    print(solve(board, 0, choices))
    print("Totaltime: {0:1.3g}s".format(time.time()-start))

if __name__ == "__main__": main() 

# Dev Kodre, Pd. 4, 2024