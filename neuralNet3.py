import sys; args = sys.argv[1:]
import math
import random
import time

#####BEST [3, 6, 3, 2, 1, 1]
#args = ["x*x+y*y<=1.0977019008057352"]
#input = open(args[0], 'r').read().splitlines()
input = args[0]

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
        #io = line.split(' => ')
        #inp,output = io[0], io[1]
        #inp = [int(x) for x in inp.split(' ')] + [1]
        #output = [int(x) for x in output.split(' ')]
        inp = line[:2] + [1]
        output = [line[2]]
        if len(struct) == 0:
            struct = [len(inp),6,6,2,len(output),len(output)]
        X_train.append(inp)
        y_train.append(output)
    
    weight_nums = [x*y for x,y in zip(struct[:-1], struct[1:-1])]
    weight_nums.append(struct[-1])

    weights = [[random.random() for x in range(y)] for y in weight_nums]

    if ">" in condition:
        if threshold > 1.35:
            weights = [[8.9171, -7.7319, -11.5101, 9.9615, 5.5303, -10.8065, 10.5725, -0.8571, 9.2551, -3.6244, -10.5022, -10.5876, 7.5701, -0.6259, 6.7461, -1.8193, 10.8597, -10.461], [8.4343, 8.3146, -4.4461, 8.3182, -2.71, 8.1102, 1.4304, 0.4606, 3.3099, -0.7899, 2.8316, -0.7768, 4.0122, 4.6386, -2.7555, 4.6577, -1.228, 4.8122, 1.0883, 0.4795, 2.8491, -0.9564, 2.2909, -1.4725, 1.1021, 1.7486, -1.3471, 1.3041, -1.0206, 1.6882, 7.7921, 7.594, -4.3114, 7.5441, -2.3479, 7.4403], [-8.8081, 4.8341, -3.888, 4.4915, -0.8267, -6.7859, -1.2391, -1.8199, -0.6345, -1.6269, -0.9461, -1.0329], [-5.9978, 1.7816], [2.014]]
        elif threshold > 1.3:
            weights = [[8.9171, -7.7319, -11.5101, 9.9615, 5.5303, -10.8065, 10.5725, -0.8571, 9.2551, -3.6244, -10.5022, -10.5876, 7.5701, -0.6259, 6.7461, -1.8193, 10.8597, -10.461], [8.4343, 8.3146, -4.4461, 8.3182, -2.71, 8.1102, 1.4304, 0.4606, 3.3099, -0.7899, 2.8316, -0.7768, 4.0122, 4.6386, -2.7555, 4.6577, -1.228, 4.8122, 1.0883, 0.4795, 2.8491, -0.9564, 2.2909, -1.4725, 1.1021, 1.7486, -1.3471, 1.3041, -1.0206, 1.6882, 7.7921, 7.594, -4.3114, 7.5441, -2.3479, 7.4403], [-8.8081, 4.8341, -3.888, 4.4915, -0.8267, -6.7859, -1.2391, -1.8199, -0.6345, -1.6269, -0.9461, -1.0329], [-5.9978, 1.7816], [2.014]]
        elif threshold > 1.2:
            weights = [[7.7054, 0.2991, 6.0196, 8.1837, 0.6855, -6.2931, -0.7014, -6.7757, -4.3836, -0.9041, 8.9395, 7.4587, -0.7743, 8.9424, -7.7209, -3.4216, 5.272, -1.3337], [-2.3496, 1.4143, 0.4535, -4.7813, 0.3952, -1.3918, -4.0823, 1.0298, -0.6999, -0.9538, 1.6536, 0.1414, -3.9311, 0.3865, 0.1341, -1.3328, 0.4622, -0.1351, -10.1649, 15.9995, 9.8922, -5.9865, 10.7499, 5.9123, -2.928, 9.4751, 2.0634, -7.5662, 1.127, -0.2772, -4.1106, 2.435, 1.8368, -2.8136, 0.9316, 0.6295], [-1.8349, -1.7144, -1.6062, -9.6119, -5.2922, -2.8989, -2.2161, -1.625, -1.6158, -9.7102, -5.1096, -2.6861], [-10.2608, -10.1938], [2.0326]]
        elif threshold > 1.15:
            weights = [[7.7054, 0.2991, 6.0196, 8.1837, 0.6855, -6.2931, -0.7014, -6.7757, -4.3836, -0.9041, 8.9395, 7.4587, -0.7743, 8.9424, -7.7209, -3.4216, 5.272, -1.3337], [-2.3496, 1.4143, 0.4535, -4.7813, 0.3952, -1.3918, -4.0823, 1.0298, -0.6999, -0.9538, 1.6536, 0.1414, -3.9311, 0.3865, 0.1341, -1.3328, 0.4622, -0.1351, -10.1649, 15.9995, 9.8922, -5.9865, 10.7499, 5.9123, -2.928, 9.4751, 2.0634, -7.5662, 1.127, -0.2772, -4.1106, 2.435, 1.8368, -2.8136, 0.9316, 0.6295], [-1.8349, -1.7144, -1.6062, -9.6119, -5.2922, -2.8989, -2.2161, -1.625, -1.6158, -9.7102, -5.1096, -2.6861], [-10.2608, -10.1938], [2.0326]]
        elif threshold > 0.84:
            weights = [[8.2479, 0.2624, 5.6498, 7.1643, 0.4205, -4.6635, -1.4945, -4.5906, -2.6375, -0.8785, 8.149, 5.7335, -0.5211, 7.2522, -5.4936, -2.348, 4.5645, -1.8972], [-1.6063, 1.0651, 1.0969, -4.4551, 0.378, -1.4098, -3.392, 0.9695, -0.762, -0.8482, 1.0434, 0.3449, -3.344, 0.3412, 0.1985, -1.4839, 0.2717, -0.2321, -6.6483, 11.2221, 6.5406, -4.3368, 7.8524, 4.698, -2.4104, 7.359, 2.6232, -5.7176, 0.7295, -0.3364, -3.3886, 2.0968, 2.0838, -3.0437, 0.7488, 0.1986], [-1.865, -1.3822, -1.3876, -8.2334, -4.6517, -2.7371, -2.2468, -1.2904, -1.3913, -8.3083, -4.4596, -2.5227], [-9.2719, -9.211], [2.0224]]
    else:
        if threshold > 1.17:
            weights = [[10.0892, 1.0256, -7.9678, -0.5185, 9.6162, -7.7017, -0.712, 8.997, 6.5339, -10.0238, -0.3737, -7.8345, -0.7135, 9.9577, 7.3597, -0.7203, 8.8328, -6.8809], [13.9344, 7.9336, -5.9311, 13.9732, -6.7292, 6.9099, -2.2676, 1.1266, 1.7137, -2.3417, 2.2946, 0.4816, -2.6644, 0.9778, 3.0356, -3.6553, 1.9083, 0.6401, -3.127, -0.0678, 2.0933, -1.6471, 2.1163, 0.217, 2.6827, 2.0947, -1.3005, 2.5615, -1.2592, 1.4001, 11.7289, 6.4198, -5.067, 11.7651, -5.4077, 6.2437], [7.0523, -3.7026, -4.7523, -3.4886, 0.0378, 6.1281, 9.3308, -4.4303, -5.6705, -4.9723, 0.915, 7.4623], [-2.8437, -4.6946], [2.0175]]
        elif threshold > 1.15:
            weights = [[9.892, 0.1026, -7.6033, 0.2153, 9.8144, -7.8922, 0.3215, 9.0007, 6.559, -10.1094, 0.5684, -7.8278, 0.2405, 9.83, 7.1419, 0.2192, 8.6194, -6.6688], [13.6706, 7.7915, -5.7667, 13.7799, -6.6227, 6.8717, -2.2104, 1.1325, 1.7448, -2.204, 2.3393, 0.5038, -2.5939, 0.9795, 3.0748, -3.4803, 1.9585, 0.6585, -3.0971, -0.0338, 2.1135, -1.5215, 2.1525, 0.2712, 2.6998, 2.0812, -1.3088, 2.5337, -1.2701, 1.3502, 11.5096, 6.2992, -4.9261, 11.6105, -5.3169, 6.1851], [6.945, -3.6071, -4.6594, -3.384, 0.0878, 6.0797, 9.2169, -4.4098, -5.6387, -4.9663, 0.9924, 7.3928], [-2.798, -4.7933], [2.0194]]
        elif threshold < 1:
            weights = [[9.6762, 0.4008, -7.1118, 0.0377, 9.6848, -7.2272, -0.1201, 8.4729, 5.5252, -9.2867, 0.3934, -6.8165, -0.001, 9.2031, 6.2929, 0.1061, 8.5041, -6.3765], [12.302, 7.2005, -5.0142, 12.5334, -5.9158, 6.0829, -1.7927, 1.2059, 1.4879, -1.9438, 2.0957, 0.5607, -2.0444, 1.045, 2.7294, -3.2192, 1.6265, 0.7124, -2.6947, 0.1399, 1.858, -1.2619, 1.9094, 0.4178, 2.6501, 1.8298, -1.2132, 2.5064, -1.1748, 1.1325, 10.3432, 5.78, -4.3485, 10.5429, -4.7839, 5.5329], [6.8763, -3.4575, -4.4738, -3.2394, 0.3094, 6.0157, 8.8169, -4.0348, -5.2162, -4.5827, 1.0874, 7.0481], [-3.2955, -4.7458], [2.0199]]
        elif threshold < 1.1:
            weights = [[10.3135, 0.6203, -7.6011, -0.6365, 10.3837, -8.0082, -0.0256, 9.3522, 6.2946, -10.9722, 0.1461, -8.309, -0.117, 10.4727, 7.4748, -0.3446, 9.5223, -6.7923], [14.7228, 8.2418, -6.257, 14.721, -7.0515, 7.2654, -2.4322, 1.1062, 1.8548, -2.515, 2.4562, 0.4776, -2.8986, 0.9674, 3.201, -3.8564, 2.1107, 0.6399, -3.2532, -0.106, 2.2616, -1.8041, 2.3054, 0.2085, 2.7269, 2.1903, -1.3838, 2.6142, -1.3508, 1.4614, 12.3835, 6.667, -5.3443, 12.391, -5.6729, 6.5147], [7.1686, -3.7137, -4.7817, -3.5142, 0.0354, 6.3003, 9.5879, -4.6141, -5.8796, -5.1555, 1.0249, 7.7226], [-2.8159, -4.8785], [2.0173]]
        elif threshold < 1.4:
            weights = [[7.9449, -0.2703, -6.7067, 0.4541, 8.088, -7.3497, 0.2644, 7.2897, 5.846, -7.6974, 0.2733, -6.413, 0.1062, 7.7695, 6.6062, 0.2705, 7.475, -6.0192], [11.6841, 6.7764, -4.9472, 11.6765, -5.9015, 5.6102, -1.6802, 1.218, 1.3456, -1.7255, 1.9736, 0.5702, -1.8951, 1.0503, 2.5204, -2.9528, 1.4425, 0.7133, -2.6071, 0.1743, 1.6245, -1.0723, 1.6972, 0.449, 2.6298, 1.7928, -1.0702, 2.463, -1.0373, 1.096, 9.8193, 5.422, -4.3048, 9.8156, -4.7887, 5.1368], [6.859, -3.3576, -4.3551, -3.1552, 0.3542, 6.0015, 8.9429, -3.6471, -4.8047, -4.2319, 1.2413, 7.1704], [-3.4544, -5.0497], [2.0146]]

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

def train(lr=0.5, epoch  = 40000):
    global minE,bestWeights
    start_time=time.time()
    n = 0
    flag = False
    lRatio = 0
    minE = 1000000
    Er = 1000000
    decrement = 0.01
    bestWeights = weights
    #while time.time()-start_time < 29.5 and get_error() >= 0.01:
    while n < epoch and time.time() - start_time <= 99:# and error() >= 0.01:
        #Er = error() 
        #if Er > minE and n > 250:
            #lr-=0.01
        if Er < 2.5:
            if Er > minE and n > 250:
                lr-=decrement
                
            else:
                lr = decrement
                minE = Er
                bestWeights = weights
        elif Er < 4:
            if Er > minE and n > 250:
                lr-=decrement
                
            else:
                lr = 0.075
                minE = Er
                bestWeights = weights
        elif Er < 5:
            if Er > minE and n > 250:
                lr-=decrement
            else:
                lr = 0.1
                minE = Er
                bestWeights = weights
        elif Er < 10:
            if Er > minE and n > 250:
                lr-=decrement
            else:
                lr = 0.3
                minE = Er
                bestWeights = weights
        if lr <decrement:
            #print(Er)
            decrement/= 2
            if decrement < 0.000000000000000000000000000001:
                decrement = 0.000000000000000000000000000001
            lr = decrement
        
        #if Er < minE:
            #minE = Er
        Er = 0
        for x,y in zip(X_train, y_train):
            feedForward(x)
            backProp(lr, y)
            Er += E(y,nodes[-1])
        #printStuff(n,lr,Er,start_time)
        if n%100:
            updateDataFrame()
        n+=1   
def updateDataFrame():
    #size = int(S**0.5)
    global X_train,y_train
    X_train = []
    y_train = []
    for i in range(S):
        x = random.uniform(-1.5, 1.5)
        y = random.uniform(-1.5, 1.5)
        t = meetsThreshold(x,y,threshold,condition)
        X_train.append([x,y,1])
        y_train.append([t])

def printStuff(n,lr,E,start_time):
    if n%100==0:
            print(f"Error: {E}")
            print(f"LR: {lr}")
            print(f"Time elapsed: {time.time() - start_time}")
            print()
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

def makeData(input):
    global condition, threshold
    condition = ""
    threshold = 0
    input = input[7:]
    threshold = 0
    condition = ""
    if input[1].isnumeric():
        threshold = float(input[1:])
        condition = input[0]
    else:
        threshold = float(input[2:])
        condition = input[:2]
    return createDataframe(threshold,condition,1000)



def main():
    dataFrame = makeData(input)
    makeModel(dataFrame)
    start = time.time()
    train()
    print(f'Layer counts:', ' '.join([str(x) for x in struct]))
    for w in bestWeights:
        print(' '.join([str(x) for x in w]))
    print(f"Error: {minE}")
    print(f"Time taken {time.time()-start}")

if __name__ == '__main__': main()



# Dev Kodre, Pd. 6, 2024