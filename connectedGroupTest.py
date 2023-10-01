import time
from othelloTournamentWINNINGV__7 import findMoves
from othelloTournamentWINNINGV__7 import evaluate
length = 64
side = 8
tokenToLanes = {}
for i in range(length):
    verts =[j for j in range(i%side,length,side)]
    start = i-(i%side)
    end = start + 8
    hrz = [j for j in range(start,end)]
    tokenToLanes[i]=(verts,hrz)

global nbrs 
nbrs = []
for i in range(64):
    s = set()
    if (i+1)%8 != 0 and i+1 < 64:
        s.add(i+1)
    if i%8 != 0 and i-1 >= 0:
        s.add(i-1)
    if i+8 < 64:
        s.add(i+8)
    if i-8 >= 0:
        s.add(i-8)
    nbrs.append(s)

def pm(brd,tkn, eTkn):
    edges = {0,1,2,3,4,5,6,7,56,57,58,59,60,61,62,63,8,16,24,32,40,48,15,23,31,39,47,55}
    count = 0
    tCount = 0
    seen = set()
    for i,n in enumerate(nbrs):
        tFlag = False
        if brd[i] == eTkn and i not in edges:
            for j in n:
                if brd[j] == "." and j not in seen:    
                    count +=1
                    if not tFlag:
                        tCount +=1
                        tFlag = True
                seen.add(j)
    return count/tCount

def stability(brd, tkn):
    eTkn = "XO".replace(tkn,"")
    total = 0
    visited = set()

    for i in tokenToLanes:
        if i not in visited and brd[i] == tkn:
            vt,hz = tokenToLanes[i]
            v = ''.join([brd[e] for e in vt])
            h = ''.join([brd[e] for e in hz])
            vCheck = False
            hCheck = False
            trimmedV = v.strip('.')
            #if trimmedV == v:
            if tkn not in trimmedV:
                pass
            elif '.' in trimmedV:
                pass
            elif eTkn in trimmedV:
                start = trimmedV.find(eTkn+tkn)
                end = trimmedV.find(tkn+eTkn)
                if (trimmedV == eTkn+tkn+eTkn or trimmedV == eTkn+tkn*2+eTkn or 
                    trimmedV == eTkn+tkn*3+eTkn or trimmedV == eTkn+tkn*4+eTkn or
                    trimmedV == eTkn+tkn*5+eTkn or trimmedV == eTkn+tkn*6+eTkn):
                    vCheck = True
                elif (v.find(tkn+eTkn) == 0 or v.find(tkn*2+eTkn) == 0 or v.find(tkn*3+eTkn) == 0 or
                      v.find(tkn*4+eTkn) == 0 or v.find(tkn*5+eTkn) == 0 or v.find(tkn*6+eTkn) == 0 or
                      v.find(tkn*7+eTkn) == 0):
                    vCheck = True
                
                else:
                    v = v[::-1]
                    if (v.find(tkn+eTkn) == 0 or v.find(tkn*2+eTkn) == 0 or v.find(tkn*3+eTkn) == 0 or
                      v.find(tkn*4+eTkn) == 0 or v.find(tkn*5+eTkn) == 0 or v.find(tkn*6+eTkn) == 0 or
                      v.find(tkn*7+eTkn) == 0):
                        vCheck = True
            else:
                vCheck = True

            trimmedH = h.strip('.')
            
            if tkn not in trimmedH:
                pass
            elif '.' in trimmedH:
                pass
            elif eTkn in trimmedH:
                start = trimmedH.find(eTkn+tkn)
                end = trimmedH.find(tkn+eTkn)
                if (trimmedH == eTkn+tkn+eTkn or trimmedH == eTkn+tkn*2+eTkn or 
                    trimmedH == eTkn+tkn*3+eTkn or trimmedH == eTkn+tkn*4+eTkn or
                    trimmedH == eTkn+tkn*5+eTkn or trimmedH == eTkn+tkn*6+eTkn):
                    hCheck = True
                elif (h.find(tkn+eTkn) == 0 or h.find(tkn*2+eTkn) == 0 or h.find(tkn*3+eTkn) == 0 or
                      h.find(tkn*4+eTkn) == 0 or h.find(tkn*5+eTkn) == 0 or h.find(tkn*6+eTkn) == 0 or
                      h.find(tkn*7+eTkn) == 0):
                    hCheck = True
                
                else:
                    h = h[::-1]
                    if (h.find(tkn+eTkn) == 0 or h.find(tkn*2+eTkn) == 0 or h.find(tkn*3+eTkn) == 0 or
                      h.find(tkn*4+eTkn) == 0 or h.find(tkn*5+eTkn) == 0 or h.find(tkn*6+eTkn) == 0 or
                      h.find(tkn*7+eTkn) == 0):
                        hCheck = True
            else:
                hCheck = True
            
            #if vCheck:
                #for i in vt:
                    #visited.add(i)
            #if hCheck:
                #for i in hz:
                    #visited.add(i)
            total += 0.5*(vCheck == True) + 0.5*(hCheck == True)
    return total
            





            
def connectedGroup(brd, tkn, i,vs):
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
    return group

def isStable(brd, group, tkn):
    #REMEMBER TO MAKE "ox" UPPERCASE
    eTkn = "xo".replace(tkn,"")
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
                        return False
                    j += -dx
    return True
def printBoard(b):        
    print("\n".join([b[x : x + 8] for x in range(0,64,8)]))
def upperBoard(b,group):
    for i in group:
        b = b[:i] +b[i].upper() + b[i+1:]        
    print("\n".join([b[x : x + 8] for x in range(0,64,8)]))

def stableCount(brd,tkn,eTkn):
    count = 0
    seen = set()
    blackList = set()
    #ndots = brd.count(".")
    for i,e in enumerate(brd):
        if e == tkn and i not in seen:
            flag = False
            deltaLen = len(seen)
            temp = set()
            seen.add(i)
            temp.add(i)
            for dx in [1,-1,8,-8]:#,9,-9,7,-7]:
                if flag: break
                x = i + dx
                
                while 0<=x<64 and brd[x] != eTkn and brd[x] != ".":
                    if ((x % 8 == 0 and dx in [1,9,-7]) or 
                        (x % 8 == 8 - 1 and dx in [-1,7,-9])):
                        break
                    seen.add(x)
                    temp.add(x)
                    x+=dx
                    
                if 0<=x<64 and brd[x] == ".":
                    j = x
                    while 0<=j<64:
                        if ((j % 8 == 0 and -dx in [1,9,-7]) or 
                        (j % 8 == 8 - 1 and -dx in [-1,7,-9])):
                            break
                        if brd[j] == eTkn:
                            #isStableCache[(brd, group, tkn)] = False
                            flag = True
                            seen = seen - temp
                            blackList.add(i)
                            break
                        j += -dx
                elif 0<=x<64 and brd[x] == eTkn:
                    f2 = False
                    j = i
                    while 0<=j<64:
                        if ((j % 8 == 0 and -dx in [1,9,-7]) or 
                        (j % 8 == 8 - 1 and -dx in [-1,7,-9])) and f2:
                            break
                        if brd[j] == eTkn and f2: break
                        if brd[j] == ".":
                            #isStableCache[(brd, group, tkn)] = False
                            flag = True
                            seen = seen - temp
                            blackList.add(i)
                            break
                        f2 = True
                        j += -dx
            
            if not flag:
                seen = seen - blackList
                deltaLen = len(seen) - deltaLen
                count+=deltaLen
    return count


def edgeStability(brd, tkn, eTkn):
    # check vertical
    horizontals = [[0,1,2,3,4,5,6,7],[56,57,58,59,60,61,62,63]]
    verticals = [[0,8,16,24,32,40,48,56],[7,15,23,31,39,47,55,63]]
    hv = horizontals + verticals

    #case 1 ox.
    #case 2 oxo
    #case 3 .xo
    #case 4 xxx


    vDx = [-8,8]
    hDx = [-1,1]
    total = 0
    totalTkns = 0
    for h in hv:
        prev = 0
        c1 = False
        c2 = False
        c3 = False
        c4 = False
        sfCount = 0
        for i in h:
            if brd[i] == tkn:
                sfCount +=1
            if brd[i] == tkn and brd[prev] == eTkn:
                c1 = True
            if brd[i] == eTkn and c1:
                c2 = True
            if brd[i] == "." and c1 and not c2:
                sfCount = 0
                break

            if brd[prev] == "." and brd[i] == tkn:
                c3 = True
            if brd[i] == "." and c3:
                c4 = True
            if brd[i] == eTkn and c3 and not c4:
                sfCount = 0
                break
            prev = i
        total+=sfCount
    
    for h in hv:
        for i in h:
            if brd[i] != ".":
                totalTkns +=1

    return total/totalTkns


def isStableEdge(brd,tkn, eTkn, edge):
    edgeString = [brd[i] for i in edge]
    if tkn in edgeString and eTkn in edgeString: return False, 0
    if tkn not in edgeString: return False, 0
    return True, edgeString.count(tkn)

def edgeStability2(brd, tkn, eTkn):
    # check vertical
    tkn = tkn.lower()
    eTkn = eTkn.lower()
    horizontals = [[0,1,2,3,4,5,6,7],[56,57,58,59,60,61,62,63]]
    verticals = [[0,8,16,24,32,40,48,56],[7,15,23,31,39,47,55,63]]
    hv = horizontals + verticals
    myTotal = 0
    eTotal = 0
    total = 0
    for edge in hv:
        eString = "".join([brd[i] for i in edge]).lower()
        if eTkn in eString and tkn in eString:
            continue
        if eTkn not in eString and tkn not in eString:
            continue
        if tkn*3 in eString or tkn*4 in eString or tkn*5 in eString or tkn*6 in eString:
            myTotal+=1
            if brd[edge[0]] == tkn or brd[edge[7]] == tkn or tkn*7 in eString or tkn*8 in eString:
                myTotal+=1
        if eTkn*3 in eString or eTkn*4 in eString or eTkn*5 in eString or eTkn*6 in eString:
            eTotal+=1
            if brd[edge[0]] == eTkn or brd[edge[7]] == eTkn or eTkn*7 in eString or eTkn*8 in eString :
                eTotal+=1
    
    if myTotal == 0:
        if eTotal == 1:
            return -75
        if eTotal == 2:
            return -50
        if eTotal == 3:
            return -25
        if eTotal == 4:
            return 5
        else: return 0
    if myTotal == 1:
        if eTotal == 1:
            return 0
        if eTotal == 2:
            return 20
        if eTotal == 3:
            return 45
        else: return 75
    if myTotal == 2:
        if eTotal == 1:
            return -20
        if eTotal == 2:
            return 0
        else:
            return 50
    if myTotal == 3:
        if eTotal == 1:
            return -45
        else:
            return 25
    if myTotal == 4:
        return -5
    return 0

        
    


            

def ac(brd,tkn,eTkn):
    aroundCorner = {1: 0, 8: 0, 9: 0, 6: 7, 14: 7, 15: 7, 48: 56, 49: 56, 57: 56, 54: 63, 55: 63, 62: 63}
    aroundEdgeToEdge = {1:[0,1,2,3,4,5,6,7], 6:[0,1,2,3,4,5,6,7], 8:[0,8,16,24,32,40,48,56], 48:[0,8,16,24,32,40,48,56],
                        57:[56,57,58,59,60,61,62,63], 62:[56,57,58,59,60,61,62,63], 15:[7,15,23,31,39,47,55,63], 55:[7,15,23,31,39,47,55,63]}
    acScore = 0
    macScore = 0
    eacScore = 0
    
    for e in [[1,8,9],[6,14,15],[48,49,57],[54,55,62]]:
        s = [brd[i] for i in e]
        s.append(brd[aroundCorner[e[0]]])
        if "." not in s: continue
        for i in e:
            if brd[i] == tkn:
                if i in [9,14,54,49]:
                    if brd[aroundCorner[i]] == tkn:
                        pass
                    elif brd[aroundCorner[i]] == eTkn:
                        eacScore+=19
                    else:
                        eacScore+=20
                else:
                    if brd[aroundCorner[i]] == tkn:
                        pass
                    elif brd[aroundCorner[i]] == eTkn:
                        if isSafeAC(tkn,eTkn,"".join([brd[j] for j in aroundEdgeToEdge[i]]),i):
                            eacScore+=19
                        else:
                            eacScore+=20
                    else:
                        if eTkn not in [brd[j] for j in aroundEdgeToEdge[i]]:
                            pass
                        else:
                            eacScore+=20

            elif brd[i] == eTkn:
                if i in [9,14,54,49]:
                    if brd[aroundCorner[i]] == eTkn:
                        pass
                    elif brd[aroundCorner[i]] == tkn:
                        macScore+=19
                    else:
                        macScore+=20
                else:
                    if brd[aroundCorner[i]] == eTkn:
                        pass
                    elif brd[aroundCorner[i]] == tkn:
                        if isSafeAC(eTkn,tkn,"".join([brd[j] for j in aroundEdgeToEdge[i]]),i):
                            macScore+=19
                        else:
                            macScore+=20
                    else:
                        if tkn not in [brd[j] for j in aroundEdgeToEdge[i]]:
                            pass
                        else:
                            macScore+=20
            
    
    if macScore + eacScore != 0:
        acScore = 100*(macScore - eacScore)/(macScore + eacScore)
    return acScore

def isSafeAC(tkn,eTkn, edgeString, i):
    es = edgeString[1:len(edgeString)-1]
    if eTkn not in es: return False
    #xo path
    if i not in [1,57,15,8]:
        es = es[::-1]
    if tkn+eTkn not in es: return False
    dot = es.find(".")
    if dot == -1:
        if es.find(tkn+eTkn): return True
        return False
    else:
        if dot < es.find(tkn+eTkn): return False
        return True

def dfc(brd,tkn, moves):
    dfcScore = 0
    board = [[brd[i*8 + j] for j in range(8)] for i in range(8)]
    
    dMoves = [(m%8,m//8) for m in moves]
    midpoint = dMoves[0]
    for i in range(1,len(dMoves)):

        ix, iy = dMoves[i]
        midpoint = (midpoint[0] + ix)/2,(midpoint[1] + iy)/2
    center_x, center_y = midpoint
    for i in range(8):
        for j in range(8):
            if board[i][j] == tkn:
                distance_from_center = ((i-center_x)**2 + (j-center_y)**2)**0.5
                weight = max(0, 1 - distance_from_center/8)
                #weight = distance_from_center
                dfcScore+=weight
    return dfcScore

    #ox path


s = '........O.......OO.XXXO.OX.XXXX..OXXOXXX..OXOXXO..OXXX...XXXXX..'.replace("*",".")
#s = 'x'*32 + 'oooooooo' + '.' + 'x'*6 + 'o' + 'x'* 8 + 'o'*8
printBoard(s)
print("")
"""upperBoard(s, connectedGroup(s, 'x', 0, set()))
print("")
t = time.time()
upperBoard(s, stability(s, 'x'))
print(time.time()-t)
print("")
t = time.time()
print(stableCount(s,'x','o'))
print(time.time()-t)"""
m = findMoves(s,'x')[0]
#print(dfc(s,'o',m)/s.count('o'))
#print(pm(s,'x'))
#print(s.count('o'))
print(evaluate(s.upper(),'O',5,True))


