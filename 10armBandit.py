import sys; args=sys.argv[1:]
import math,random

def bandit(testNum,armIdx,pullVal):
    global orderedSet,c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,scoreLst,ctLst,meanLst
    if testNum == 0:
        orderedSet = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        c0,c1,c2,c3,c4,c5,c6,c7,c8,c9 = 0,0,0,0,0,0,0,0,0,0
        scoreLst = [0,0,0,0,0,0,0,0,0,0]
        meanLst = [5,5,5,5,5,5,5,5,5,5]
        ctLst = [0,0,0,0,0,0,0,0,0,0]
        return 0
    else:
        ctLst[armIdx]+= 1
        scoreLst[armIdx]+=pullVal 

        #meanLst[armIdx]+= 1/ctLst[armIdx]*(pullVal-meanLst[armIdx])

        """if testNum < 50:  return testNum%10

        maxMean = -50
        for i in range(10):
            mean = scoreLst[i]/ctLst[i]
            if mean > maxMean:
                maxMean = mean
        
        for i in range(10):
            if scoreLst[i]/ctLst[i] == maxMean: return i"""
        return UCB(scoreLst,testNum,ctLst)

def UCB(sList, step,ctLst):
    means = [0,0,0,0,0,0,0,0,0,0]
    for i in range(10):
        if ctLst[i] != 0:
            means[i] = sList[i]/ctLst[i]
        else:
            return i
    ucbLst = [0,0,0,0,0,0,0,0,0,0]
    c = 0.835
    for i in range(10):
            #A       =    Q      + c*sqrt(ln(t)/N(t))
        ucbLst[i] = means[i] + c*((math.log(step)/ctLst[i])**0.5)

    
    maxUcb = max(ucbLst)
    for i in range(10):
        if ucbLst[i] == maxUcb:
            return i

"""bandits = []
for i in range(10):
    bandits.append(random.gauss(0, 1))
for j in range(10):
    armIdx = -1
    sum = 0
    for k in range(50):
        for i in range(1000):
            if i >0:
                sum += val
            val = random.gauss(bandits[armIdx],1)
            armIdx = bandit(i,armIdx,val)
    print(sum/50)"""

        



# Dev Kodre, Pd. 4, 2024





    

    