import sys; args = sys.argv[1:]
import math
import random
import time

#G6 V-1R23 E0=5
"""args = {
    "G19 V4R88",
    "G8 V5R28",
    "G6W1 V3R55",
    "G11",
    "G6W3 E1=4 V3R9",
    "G13 V8R18 V2R82",
    "G25 V0,4,24,20R12",
    "G14W7 E1:6S= E10E~ V4R10",
    "G25 V11,6,16,11B V17R8",
    "G9 V4,7,3,6B V0R90 E4=1 E4=5",
    "G15 V6,7,2B V1R13 E6,6=11,5"
    'GG70R89 V67R59B V44,30,57,46,51,13,4,28,24,17,26,38RB'
}"""
#args = 'G14 E11E= E0W= E2E= E4E= E13E= E1W= E6E= V7R74'.split(" ")

def setGlobals(input):
    global grid, vertexMap, width, gridCopy, size, height, reward,ogNbrs,jumps,bSquares
    bSquares = set()
    jumps = []
    ogNbrs = []
    vertexMap = {}
    for splice in input:
        if "G" in splice:
            width = 0
            reward = 0
            size = ""
            if splice[1].isnumeric():
                i = 1
                while i < len(splice) and splice[i].isnumeric():
                    size += splice[i]
                    i+=1
                size = int(size)
            elif splice[1] == "G":
                i = 2
                while i < len(splice) and splice[i].isnumeric():
                    size += splice[i]
                    i+=1
                size = int(size)
            elif splice[1] == "N":
                return

            if "W" in splice:
                w = ""
                i = splice.find("W") + 1
                while i < len(splice) and splice[i].isnumeric():
                    w += splice[i]
                    i+=1
                width = int(w)
        
            if "R" in splice:
                r = ""
                i = splice.find("R") + 1
                while i < len(splice) and splice[i].isnumeric():
                    r += splice[i]
                    i+=1
                reward = int(r)

            

            if width == 0:
                width = findWidth(size)
            grid = [[(0,False) for x in range(width)] for y in range(size//width)]
            #if reward != 0:
                #grid = [[(reward,True) for x in range(width)] for y in range(size//width)]
            #else:
                
            
            height = size//width
            
            gridCopy = [i for i in range(size)]
            

            
            for i in range(height*width):
                x = []
                if i%width > 0: x.append(i-1)
                if i%width < width-1: x.append(i+1)
                if i//width > 0: x.append(i-width)
                if i//width < height-1: x.append(i+width)
                vertexMap[i] = [grid[i//width][i%width][0], grid[i//width][i%width][1], x] 
                ogNbrs.append([*x])

        if "V" in splice:
            if "R" not in splice and "B" not in splice:
                continue
            directive = ""
            endIndex = 0
            #splices = splice.split(",")
            #for i in range(len(splice) - 1, -1, -1):
                #directive = splice[i] + directive
                #if splice[i].isalpha():
                    #endIndex = i
                    #break
            
            if 0< splice.find("R") and  0< splice.find("B"):
                endIndex = min(splice.find("R"),splice.find("B"))

            elif 0< splice.find("R"):
                endIndex = splice.find("R")
            else:
                endIndex = splice.find("B")
            directive = splice[endIndex:]
            
            splices = splice[1:endIndex].split(",")
            seen = set()
            for slice in splices:

                if slice.isnumeric() or (slice[0] == '-' and slice[1:].isnumeric()):
                    if int(slice) not in seen:
                        assignVertex(int(slice),directive)
                        seen.add(int(slice))
                else:
                    vSlice = extractSlice(slice)
                    for vertex in gridCopy[vSlice]:
                        if vertex not in seen:
                            assignVertex(vertex, directive)
                            seen.add(vertex)

            if "B" in directive:
                for vertex in seen:

                    neighbors = []
                    i = vertex
                    if i%width > 0: neighbors.append(i-1)
                    if i%width < width-1: neighbors.append(i+1)
                    if i//width > 0: neighbors.append(i-width)
                    if i//width < height-1: neighbors.append(i+width)
                    nbrs = [*neighbors]

                    for nbr in nbrs:
                        if nbr not in seen and nbr not in bSquares:
                            vertexMap[nbr][2].remove(vertex)
                            neighbors.remove(nbr)
                        else:
                            if vertex not in vertexMap[nbr][2]:
                                vertexMap[nbr][2].append(vertex)
                                vertexMap[vertex][2].append(nbr)
                    vertexMap[vertex][2] = [*({*vertexMap[vertex][2]}.intersection(bSquares))]
                    for nbr in neighbors:
                        if 0 <= nbr < size:
                            vertexMap[vertex][2].append(nbr)
                            vertexMap[nbr][2].append(vertex)
                    for vertex in vertexMap:   
                        vertexMap[vertex][2] = [*{*vertexMap[vertex][2]}]
                bSquares|=seen
        #E[]
        if "E" in splice:
            if 0< splice.find("R"):
                endIndex = splice.find("R")
            else: endIndex = len(splice)

            if"+~" in splice:
                vSplice = splice[splice.find("+~")+2:endIndex]
                eType = "+~"
            elif "+" in splice:
                vSplice = splice[splice.find("+")+1:endIndex]
                eType = "+"
            elif "~" == splice[1]:
                vSplice = splice[splice.find("~")+1:endIndex]
                eType = "~"
            else:
                vSplice = splice[1:endIndex]
                eType = "d"

            directive = splice[endIndex:]

            if any(c in vSplice for c in "NSEW"):
                direction = vSplice[-2]
                cType = vSplice[-1]
                edges = extractDirSlice(vSplice[:-2],direction)
                seen = set()
                for vs,ve in edges:
                    if isinstance(vs,int) and isinstance(ve,int) and (vs,ve) not in seen:
                        assignEdge(vs,ve,eType,cType,directive)
                        seen.add((vs,ve))
                
                continue


            elif "=" in vSplice:
                startSlices, endSlices = vSplice.split("=")[0],vSplice.split("=")[1]
                cType = "="
            elif "~" in vSplice:
                startSlices, endSlices = vSplice.split("~")[0],vSplice.split("~")[1]
                cType = "~"

            

            startSlices = startSlices.split(",") 
            endSlices = endSlices.split(",")
            seen = set()
            for start,end in zip(startSlices,endSlices):
                if start.isnumeric() or (start[0] == '-' and start[1:].isnumeric()):
                    if (int(start),int(end)) not in seen:
                        assignEdge(int(start),int(end),eType,cType,directive)
                        seen.add((int(start),int(end)))
                else:
                    vStart = extractSlice(start)
                    vEnd =  extractSlice(end)
                    for vs,ve in zip(gridCopy[vStart],gridCopy[vEnd]):
                        if (vs,ve) not in seen:
                            assignEdge(vs,ve,eType,cType,directive)
                            seen.add((vs,ve))

def assignEdge(start,end,eType,cType,directive):
    global vertexMap,grid
    if directive:
        pass
    else:
        if eType == "d":
            if end in vertexMap[start][2]:
                vertexMap[start][2].remove(end)
            else:
                vertexMap[start][2].append(end)
            if cType == "=":
                if start in vertexMap[end][2]:
                    vertexMap[end][2].remove(start)
                else:
                    vertexMap[end][2].append(start)

        elif eType == "+":
            if end not in vertexMap[start][2]:
                vertexMap[start][2].append(end)
            if cType == "=":
                if start not in vertexMap[end][2]:
                    vertexMap[end][2].append(start)
        
        elif eType == "~":
            if end  in vertexMap[start][2]:
                vertexMap[start][2].remove(end)
            if cType == "=":
                if start in vertexMap[end][2]:
                    vertexMap[end][2].remove(start)

            
def extractDirSlice(s,d):
    dNames = "NSEW"
    directions = [-width,width,1,-1]
    sl = extractSlice(s)
    if sl:
        start = gridCopy[sl]
    else:
        start = gridCopy[int(s)]
    end = []
    if isinstance(start,list):
        for vertex in start:
            if vertex + directions[dNames.find(d)] in ogNbrs[vertex]:
                end.append(vertex + directions[dNames.find(d)])
        return zip(start,end)
    else:
        if start + directions[dNames.find(d)] in ogNbrs[start]:
            end = start + directions[dNames.find(d)]
        return zip([start],[end])


def extractSlice(s):
    if s.count(":") == 1:
        if s[:s.find(":")] == "":
            a = None
        else:
            a = int(s[:s.find(":")])
        
        if s[s.find(":")+1:] == "":
            b = None
        else:
            b = int(s[s.find(":")+1:])
        return slice(a,b)
    elif s.count(":") == 2:
        if s[s.find(":")+1:s.find(":",s.find(":")+1)] == "":
            b = None
        else:
            b = int(s[s.find(":")+1:s.find(":",s.find(":")+1)])

        if s[:s.find(":")] == "":
            a = None
        else:
            a = int(s[:s.find(":")])
        
        if s[s.find(":",s.find(":")+1)+1:] == "":
            c = None
        else:
            c = int(s[s.find(":",s.find(":")+1)+1:])

        return slice(a, b, c)

            
def findWidth(n):
    factors = []
    for factor in range(1, int(n ** 0.5) + 1):
        if n % factor == 0:
            factors.append(factor)
    return n//factors[-1]

def assignVertex(vertex,directive):
    global vertexMap,grid
    if "R" in directive:
        if "B" in directive:
            d = directive.replace("B","")
        else:
            d = directive
        if len(d) > 1:
            if vertex in vertexMap:
                a = vertexMap[vertex][0] = int(d[1:])
            else:
                a = int(d[1:])
        else:
            if vertex in vertexMap:
                a = vertexMap[vertex][0] = reward
            else:
                a  = reward
        if vertex in vertexMap:
            vertexMap[vertex][1] = True

        grid[vertex//width][vertex%width] = (a, True)

    """if "B" in directive:
        if vertex in vertexMap:
            for v in vertexMap:
                if vertex in vertexMap[v][2]:
                    vertexMap[v][2].remove(vertex)

            if vertex in vertexMap:
                del vertexMap[vertex]
        else:
            vertexMap[vertex] = [0,False,[]]
            otherVs = [1+vertex,-1+vertex,width+vertex,-width+vertex]
            for n in otherVs:
                if 0<= n < size:
                    vertexMap[vertex][2].append(n)
                    vertexMap[n][2].append(vertex)"""
        

                
def isPrime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True
                

def getEndingPoints():
    vertices = []
    #for vertex in vertexMap:
        #if vertexMap[vertex][1] == True:
            #vertices.append(vertex)
    #return vertices
    count = 0
    for subLists in grid:
        for vertex in subLists:
            if vertex[1] == True:
                vertices.append(count)
            count+=1
    return vertices

def updateDirections(gen,directions,seen):
    for pair in gen:
        vertex, neighbor = pair
        directions[neighbor].add(getDirection(vertex,neighbor))
        seen.add(neighbor)

#           ^
#         J N L
#   < W - | + | - E >
#         7 S r
#           v
#                       . (for other solution / no solution )

def getDirection(vertex,neighbor):
    global jumps
    if width != 1:
        if neighbor-vertex == 1 and neighbor in ogNbrs[vertex]:
            return "W"
        if neighbor-vertex == -1 and neighbor in ogNbrs[vertex]:
            return "E"
    else:
        if neighbor-vertex == 1 and neighbor in ogNbrs[vertex]:
            return "N"
        if neighbor-vertex == -1 and neighbor in ogNbrs[vertex]:
            return "S"
    if neighbor-vertex == width and neighbor in ogNbrs[vertex]:
        return "N"
    if neighbor-vertex == -width and neighbor in ogNbrs[vertex]:
        return "S"
    jumps.append((vertex,neighbor))
    return "."

def printGrid(directions):
    g = ""
    for s in directions:
        if "." in s and len(s) > 1:
            s.remove(".")
        if s == "." or len(s) == 1:
            g+= str(*s)
        elif len(s) == 2:
            if "." in s: s.remove(".")
            if "N" in s:
                if "E" in s:
                    g+=("L")
                elif "S" in s:
                    g+=("|")
                elif "W" in s:
                    g+=("J")
            elif "S" in s:
                if "E" in s:
                    g+=("r")
                elif "W" in s:
                    g+=("7")
            else:
                g+=("-")
        
        elif len(s) == 3:
            if "." in s: s.remove(".")
            if s == {"N","E","S"}:
                g+=(">")
            elif s == {"N","E","W"}:
                g+=("^")
            elif s == {"N","W","S"}:
                g+=("<")
            elif s == {"W","E","S"}:
                g+=("v")
        elif len(s) == 4:
            if "." in s: s.remove(".")
            g+=("+")
        
    print("Policy:")
    print("\n".join([g[x : x + width] for x in range(0,size,width)]))
    if jumps:
        #print("Jumps: ",end="")
        printJumps(jumps)
        #print(*[jump for jump in jumps])

def printJumps(jumps):
    start=[]
    end = []
    start = ""
    end = ""
    for i,jump in enumerate(jumps):
        start+=str(jump[1])
        end+=str(jump[0])
        if i != len(jumps)-1:
            start+=","
            end+=","
    print(start+">"+end)

        

def evaluateGrid():
    seen = set()
    directions = [set() for i in range(size)]
    queue = [getEndingPoints()]
    for vertex in queue[0]:
        directions[vertex].add("*")
        seen.add(vertex)
    
    queue[0] = {*queue[0]}
    
    for vertexGen in queue:
        if len(vertexGen) == 0: break
        q = set()
        for vertex in vertexGen:    
            gen = []
            if vertex not in vertexMap: continue
            for neighbor in getNeighbors(vertex):#vertexMap[vertex][2]:
                if neighbor in seen or vertexMap[neighbor][1] == True:
                    continue
                gen.append((vertex,neighbor))

            for pair in gen:
                vertex, neighbor = pair
                directions[neighbor].add(getDirection(vertex,neighbor))
                q.add(neighbor)
        queue.append(q)
        seen = seen | q
    for i,dSet in enumerate(directions):
        if len(dSet) == 0:
            directions[i].add(".")
    printGrid(directions)


def getNeighbors(vertex):
    nbrs = []
    for v in vertexMap:
        if vertex in vertexMap[v][2]:
            nbrs.append(v)
    return nbrs
        #if "V" in splice:


setGlobals(args)
evaluateGrid()

# Dev Kodre, Pd. 4, 2024