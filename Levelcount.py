width, height = 3, 3

def neighbors(puzzle):
  adjacent = set()
  emptyIndex = puzzle.index('_')
  col = emptyIndex % width
  row = emptyIndex // height
  if(col != width-1): 
    l = [*puzzle]
    l[emptyIndex] = l[emptyIndex + 1]
    l[emptyIndex + 1] = "_"
    adjacent.add("".join(l))
  if(col != 0):
    l = [*puzzle]
    l[emptyIndex] = l[emptyIndex - 1]
    l[emptyIndex - 1] = "_"
    adjacent.add("".join(l))
  if(row != height-1):
    l = [*puzzle]
    l[emptyIndex] = l[emptyIndex + width]
    l[emptyIndex + width] = "_"
    adjacent.add("".join(l))
  if(row != 0):
    l = [*puzzle]
    l[emptyIndex] = l[emptyIndex - width]
    l[emptyIndex - width] = "_"
    adjacent.add("".join(l))
  return adjacent

def solvelevelcount(puzzle):
    levellist = []
    currentlevel = [puzzle]
    parseMe = [puzzle]
    dctSeen = {puzzle:""} #seenNode: parent
    #stop = 4
    while currentlevel: # and stop != 0:
        levellist.append(len(currentlevel))
        currentlevel = []
        for itm in parseMe:
            for p in neighbors(itm):
                if p not in dctSeen:
                    currentlevel.append(p)
                    dctSeen.update({p: itm})
        parseMe = currentlevel
        #stop -= 1
    return levellist

levelcount = solvelevelcount("123_45678")
for idx in range(len(levelcount)):
    print("level " + str(idx) + ": " + str(levelcount[idx]))