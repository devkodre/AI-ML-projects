# Dev Kodre pd 4
import sys; args = sys.argv[1:]
import math
import random
import time
import matplotlib.pyplot as plt

#####BEST [3, 6, 3, 2, 1, 1]
#args = ["x*x+y*y<=1.0977019008057352"]
#input = open(args[0], 'r').read().splitlines()
#input = args[0]
input = open('mnist_train.csv', 'r').read().splitlines()
testInput = open('mnist_test.csv', 'r').read().splitlines()
file = open("accuracy.txt", "w")
global size
size = len(testInput)

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
        return 1/(1+math.e**(x*-1))
    if tf == "T4":
        return 2* 1/(1+math.e**(-x))-1

def F(x):
    return f("T3",x)

def dF(x):
    return x*(1-x)
def processData(line):
    line = line.split(',')
    output = []
    for i in range(10):
        if i == int(line[0]):
            output.append(1) 
        else:
            output.append(0)
    inp = [int(x)/255 for x in line[1:]] + [1]
    return inp, output

def getTestData(testInput):
    global X_test, y_test
    X_test = []
    y_test = []
    for line in testInput:
        inp,output = processData(line)
        X_test.append(inp)
        y_test.append(output)


def makeModel(inputs):
    global X_train, y_train, weights, nodes, struct, yL, pE,accuracyVals,timeVals
    accuracyVals = []
    timeVals = [] 
    pE = []
    yL = []
    struct = []
    nodes = []
    weights = []
    X_train = []
    y_train = []
    

    for line in inputs:
        inp,output = processData(line)
        #io = line.split(' => ')
        #inp,output = io[0], io[1]
        #inp = [int(x) for x in inp.split(' ')] + [1]
        #output = [int(x) for x in output.split(' ')]
        #inp = line[:2] + [1]
        #output = [line[2]]
        if len(struct) == 0:
            struct = [len(inp),300,100,len(output),len(output)]
        X_train.append(inp)
        y_train.append(output)
    
    weight_nums = [x*y for x,y in zip(struct[:-1], struct[1:-1])]
    weight_nums.append(struct[-1])

    weights = [[random.uniform(-1,1) for x in range(y)] for y in weight_nums]

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

def train(lr=0.5, epoch  = 3):
    global minE,bestWeights,decrement, eMatrix,lrMatrix,dMatrix,a,maxA, pastAccuracies
    pastAccuracies = []
    maxA = -100
    a = 0
    lrMatrix = [lr,lr,lr,lr,lr,lr,lr,lr,lr,lr]
    start_time=time.time()
    n = 0
    flag = False
    lRatio = 0
    minE = 1000000
    eMatrix = [minE,minE,minE,minE,minE,minE,minE,minE,minE,minE]
    Er = 1000000
    decrement = 0.001
    dMatrix = [decrement,decrement,decrement,decrement,decrement,decrement,decrement,decrement,decrement,decrement]

    bestWeights = weights
    #while time.time()-start_time < 29.5 and get_error() >= 0.01:
    while n < epoch:#and time.time() - start_time <= 99:
        Er = 0
        ct = 0
        for x,y in zip(X_train, y_train):
            feedForward(x)
            backProp(lr, y)
            e = E(y,nodes[-1])
            #if ct > 500:
                #lr = changeLearningRate(e, y)

            Er += e
            if ct%500 == 0 and ct != 0:
                updateGraph(ct,lr)
                if len(pastAccuracies) == 5:
                    pastAccuracies.pop(0)
                    if max(pastAccuracies) - min(pastAccuracies) < 0.05 and sum(pastAccuracies)/5 < 90:
                        if lr < 1:
                            lr+=0.1
                pastAccuracies.append(a)
                

                if a > 0.8 and a <= maxA:
                    lr-= 0.05
                    if lr < 0.05:
                        lr = 0.05
                else:
                    maxA = a
                #print(nodes)
            else:
                print(ct, e, lr)
                
            ct+=1 
        #printStuff(n,lr,Er,start_time)
        #if n%100:
            #updateDataFrame()
        n+=1   
"""def updateDataFrame(): 
    #size = int(S**0.5)
    global X_train,y_train
    X_train = []
    y_train = []
    for i in range(S):
        x = random.uniform(-1.5, 1.5)
        y = random.uniform(-1.5, 1.5)
        t = meetsThreshold(x,y,threshold,condition)
        X_train.append([x,y,1])
        y_train.append([t])"""
def changeLearningRate(Er,y):
    global minE,decrement,eMatrix,lrMatrix,dMatrix
    index = y.index(1)
    #print(index)


    if Er > eMatrix[index]:
        lrMatrix[index]-=dMatrix[index]
    else:
        minE = Er
        eMatrix[index] = Er

    if lrMatrix[index] <dMatrix[index]:
            #print(Er)
        dMatrix[index]/= 2
        if dMatrix[index] < 0.0000000000000000000000000000000001:
            dMatrix[index] = 0.0000000000000000000000000000000001
        lrMatrix[index] = dMatrix[index]
    return lrMatrix[index]
def accuracy():
    ct = 0
    for x,y in sampled_data:
        feedForward(x)
        max = -10
        index = -1
        for i, n in enumerate(nodes[-1]):
            if n > max:
                max = n
                index = i
        if index == y.index(1):
            ct+=1
    return ct/s

def updateGraph(ct,lr):
    file = open("accuracy.txt", "a")
    global accuracyVals, timeVals,start,a
    print("Getting Accuracy")
    a = accuracy()
    accuracyVals.append(a)
    print("Done")
    t = time.time() - start
    timeVals.append(t)
    """plt.plot(timeVals, accuracyVals)
    plt.xlabel('Time')
    plt.ylabel('Accuracy')
    plt.title('Accuracy vs. Time')
    plt.show()
    delta = time.time()
    while time.time() - delta < 10:
        pass
    start+=10
    plt.close()"""
    print(f"Accuracy: {a*100}%")
    file.write(f"Accuracy: {int(a*100)}%: Time: {int(t)}s: BackProp: {ct}: Past 3 Accuracies: {pastAccuracies}: LR: {lr}\n")
    print("")

def display():
    plt.plot(timeVals, accuracyVals)
    plt.xlabel('Time')
    plt.ylabel('Accuracy')
    plt.title('Accuracy vs. Time')
    plt.show()

        

def printStuff(n,lr,E,start_time):
    if n%1==0:
            print(f"Error: {E}")
            print(f"LR: {lr}")
            print(f"Time elapsed: {time.time() - start_time}")
            #print(f"Accuracy: {accuracy()}")
def meetsThreshold(x,y,threshold,condition):
    if condition == '<':
        return int(x*x+y*y < threshold)
    elif condition == '<=':
        return int(x*x+y*y <= threshold)
    elif condition == '>':
        return int(x*x+y*y > threshold)
    else:
        return int(x*x+y*y >= threshold)


def createDataframe(threshold, condition,size):
    global S
    dataframe = []
    x = -1.5
    size= int(size**0.5)
    S = size**2
    while x <= 1.5:
        y=-1.5
        while y <=1.5:
            t = meetsThreshold(x,y,threshold,condition)
            #if t == 0:
                #print(x,y)
            dataframe.append([x,y, t])
            y+=3/size
        x+=3/size
    return dataframe






def main():
    global start,sampled_data, s
    #dataFrame = makeData(input)
    makeModel(input)
    getTestData(testInput)
    s = 500
    sampled_data = random.sample(list(zip(X_test, y_test)), s)
    start = time.time()
    train()
    print(f'Layer counts:', ' '.join([str(x) for x in struct]))
    #for w in bestWeights:
        #print(' '.join([str(x) for x in w]))
    print(f"Error: {minE}")
    print(f"Time taken {time.time()-start}")
    file.close()
    display()

if __name__ == '__main__': main()



# Dev Kodre, Pd. 4, 2024