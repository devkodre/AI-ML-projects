import sys; args = sys.argv[1:]
import math




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
print(*v1)


#error final = 
"""for each weight in the final layer
    (t - y) * weight in that layer"""

#error n-1 = partial(wrt y)
"""for each weight in the second to last layer
    py = (t-y)of that node * xn(1-xn)"""





# Dev Kodre, Pd. 6, 2024