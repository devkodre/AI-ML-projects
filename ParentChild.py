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
    parent = set()
    dctNodes={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
    stop = 4
    while currentlevel and stop != 0:
        levellist.append(len(currentlevel))
        currentlevel = []
        for itm in parseMe:
            neighborlst = neighbors(itm)
            print(neighborlst)
            for p in neighborlst:
                if len(neighborlst) == 2:
                    if len({*neighborlst}.union(dctSeen)) == 0:
                        dctNodes[1]+=1
                    if len({*neighborlst}.union(dctSeen)) == 1:
                        dctNodes[2]+=1
                    if len({*neighborlst}.union(dctSeen)) == 2:
                        dctNodes[3]+=1
                if len(neighborlst) == 3:
                    if len({*neighborlst}.union(dctSeen)) == 0:
                        dctNodes[4]+=1
                    if len({*neighborlst}.union(dctSeen)) == 1:
                        dctNodes[5]+=1
                    if len({*neighborlst}.union(dctSeen)) == 2:
                        dctNodes[6]+=1
                    if len({*neighborlst}.union(dctSeen)) == 3:
                        dctNodes[7]+=1
                if len(neighborlst) == 4:
                    if len({*neighborlst}.union(dctSeen)) == 0:
                        dctNodes[8]+=1
                    if len({*neighborlst}.union(dctSeen)) == 1:
                        dctNodes[9]+=1
                    if len({*neighborlst}.union(dctSeen)) == 2:
                        dctNodes[10]+=1
                    if len({*neighborlst}.union(dctSeen)) == 3:
                        dctNodes[11]+=1
                    if len({*neighborlst}.union(dctSeen)) == 4:
                        dctNodes[12]+=1
                if p not in dctSeen:
                    currentlevel.append(p)
                    dctSeen.update({p: itm})
                    parent.add(p)
        parseMe = currentlevel
        stop -= 1
    return dctNodes

nodes = solvelevelcount("1234_5678")
for key in nodes:
    print("level " + str(nodes[key]) + ": " + str(nodes[key]))