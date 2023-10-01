import sys; args = sys.argv[1:]
import math
import random
import time

#args = ["train_1.txt"]
#args = ['nn4weights.txt', 'x*x+y*y<1']
input = open(args[0], 'r').read().splitlines()
equation = args[1]

def makeSquareNetwork(input,equation):
    global weights, struct, condition, R
    weights = []
    struct = []
    if '=' in equation:
        condition = equation[7:9]
        R = float(equation[9:])**0.5
    else:
        condition = equation[7]
        R = float(equation[8:])**0.5
    
    for line in input:
        if '.' in line:
            weights.append([float(i) for i in line.split(", ")])
    struct.append(len(weights[-1]))
    for i in range(len(weights)-2,0,-1):
        struct.append(len(weights[i])//struct[-1])
    struct = [2] + struct[::-1] +[struct[0]]


def appendNetwork():
    global weights, struct, condition, R
    combinedWeights = [[]]
    struct = [l*2 for l in struct] + [1]
    struct[0] = 3; struct[-2] = 1

    weights[0] = [w/R for w in weights[0]]
    #first layer
    for i in range(len(weights[0])):
        if (i+1)%2 == 0:
            combinedWeights[0].append(0)
        combinedWeights[0].append(weights[0][i])
    for i in range(len(weights[0])):
        if i%2 == 0:
            combinedWeights[0].append(0)
        combinedWeights[0].append(weights[0][i])
    #next layers
    for i in range(1,len(weights)-1):
        combinedWeights.append([])
        layer = struct[i]//2
        for j in range(0,len(weights[i]),layer):
            combinedWeights[i]+= weights[i][j:j+layer]
            combinedWeights[i]+= [0]*layer
        for j in range(0,len(weights[i]),layer):
            combinedWeights[i]+= [0]*layer
            combinedWeights[i]+=weights[i][j:j+layer]
    combinedWeights.append(weights[-1]*2)

    #print(condition)
    if '>' in condition: 
        combinedWeights.append([(1+math.e)/(2*math.e)])
    else: 
        combinedWeights.append([(1+math.e)/2])
    
    return combinedWeights


def E(t,y):
    return 0.5*sum((t[k]-y[k])**2 for k in range(len(t)))
def dotProd(v1,v2):
    return sum(v1[i]*v2[i] for i in range(len(v1)))
def hadamardProd(v1,v2):
    return [v1[i]*v2[i] for i in range(len(v1))]

def setWeights(f,inputs):
    weights = []
    layers = []
    lines = []
    size = len(inputs)
    v= len(inputs)
    with open(args[0]) as file:
        lines = [line.strip() for line in file]
    for line in lines:
        if line == lines[-1]:
            tempLayer = line.split(" ")
            tempLayer = [float(e) for e in tempLayer]
            weights+=tempLayer
        else:
            tempLayer = line.split(" ")
            tempLayer = [float(e) for e in tempLayer]
            size = int(len(tempLayer)/size)
            tempLayer = [tempLayer[i:i+v] for i in range(0,len(tempLayer),v)]
            v = len(tempLayer)
            layers.append(size)
            weights+=tempLayer
    
    return weights,layers


def getInputs(s):
    global fileName,transferFunc,inputs
    #s=s.split(" ")
    fileName = s[0]
    transferFunc = s[1]
    inputs = s[2:]
    inputs = [float(e) for e in inputs]



def f(tf, x):
    if tf == "T1":
        return x
    if tf == "T2":
        if x>=0: return x
        else: return 0
    if tf == "T3":
        return 1/(1+math.e**(-x))
    if tf == "T4":
        return 2* 1/(1+math.e**(-x))-1

def F(x):
    return f("T3",x)

def dF(x):
    return x*(1-x)

def makeModel(inputs):
    global X_train, y_train, weights, nodes, struct, yL, pE
    pE = []
    yL = []
    struct = []
    nodes = []
    weights = []
    X_train = []
    y_train = []
    for line in inputs:
        numLine = line.split(',')
        weights.append([float(x) for x in numLine])
        #X_train.append(inp)
        #y_train.append(output)
    
    if len(struct) == 0:
        struct = [len(weights[0]),3,len(weights[-1]),len(weights[-1])]
    
    weight_nums = [x*y for x,y in zip(struct[:-1], struct[1:-1])]
    weight_nums.append(struct[-1])

    weights = [[random.random() for x in range(y)] for y in weight_nums]
    yL = [[0 for x in range(s)] for s in struct[1:]]
    pE = [[0 for x in range(s)] for s in struct[:-1]] 
    nodes = [[0 for x in range(s)] for s in struct]
    #nodes[0] = 


    
def feedForward(x):
    global nodes, yL
    for i,elem in enumerate(x):
        nodes[0][i] = elem
        
    for l in range(len(struct)-2):
        for idx,n in enumerate(nodes[l+1]):
            w = weights[l][struct[l]*idx:struct[l]*(idx+1)]
            yL[l][idx] = dotProd(nodes[l],w)
            nodes[l+1][idx] = F(yL[l][idx]) 
    
    nodes[-1] = hadamardProd(weights[-1],nodes[-2])
    yL[-1] = nodes[-1]
        
def backProp(lr, t):
    global pE, weights
    pE[-1] = [(t[ii]-nodes[-1][ii])*weights[-1][ii]*dF(nodes[-2][ii]) for ii in range(struct[-1])]
    #final layer (t - y) * weight in that layer
    for i in range(struct[-2]):
        weights[-1][i] += lr*(t[i]-yL[-1][i])*nodes[-2][i]
    
    for l in range(len(struct)-3, 0, -1):
        prevWN = len(weights[l])//len(pE[l])
        for i in range(len(pE[l])):
            pE[l][i] = dotProd([weights[l][j] for j in range(i, len(weights[l]), len(weights[l])//prevWN)], pE[l+1])*dF(nodes[l][i])
    
    for i in range(len(weights)-1):
        for j in range(len(nodes[i])):
            for k in range(len(pE[i+1])):
                weights[i][k*(len(weights[i])//len(pE[i+1]))+j] += lr*nodes[i][j]*pE[i+1][k]
    


    #for i,node in enumerate(nodes[-1]):
        #nodes[-1][i] = weights[-1][i]*nodes[-2][i]
        #yL[-1][i] = weights[-1][i]*nodes[-2][i]
def error():
    err = 0
    for x,y in zip(X_train, y_train):
        feedForward(x)
        err += E(y, nodes[-1])
    return err

def train(lr=0.3, epoch  = 40000):
    start_time=time.time()
    n = 0
    #while time.time()-start_time < 29.5 and get_error() >= 0.01:
    while n < epoch and error() >= 0.01:
        for x,y in zip(X_train, y_train):
            feedForward(x)
            backProp(lr, y) 
        n+=1   

"""
#args = "weightFile.txt T3 0.1 0.2 0.3 0.4 0.5".split(" ")
getInputs(args)
weights,layers = setWeights(fileName,inputs)
v1 = inputs
for e in layers:
    temp = []
    if isinstance(e,float):
        v1 = hadamardProd(v1, weights)
    else:
        for i in range(e):
            ws = weights.pop(0)
            temp.append(f(transferFunc,dotProd(v1,ws)))
        v1=temp
v1 = hadamardProd(v1, weights)
print(*v1)"""

    

#error final = 
"""for each weight in the final layer
    (t - y) * weight in that layer"""

#error n-1 = partial(wrt y)
"""for each weight in the second to last layer
    py = (t-y)of that node * xn(1-xn)"""

def main():
    makeSquareNetwork(input,equation)
    combinedNetwork = appendNetwork()
    #train()
    print(f'Layer counts:', ' '.join([str(x) for x in struct]))
    for w in combinedNetwork:
        print(' '.join([str(x) for x in w]))
    #print(f"Error: {error()}")

if __name__ == '__main__': main()



# Dev Kodre, Pd. 6, 2024