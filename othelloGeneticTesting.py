import sys; args = sys.argv[1:]
import time
import random
#Min Score: -2; move sequence: [0, 8, 49, 57, 9, 56, 48, 62, 1, 14, 7, 6, 60, 59, 63, 54]
#args = '..xx*x..x.xxoxx.xxxooxxxxxxxoxoxxxxxxoxoxxxxxxoox.xxx.*o..xxxx.* x'.replace("*",'.').split(" ")
#args = '192029'.split(" ")
global timeLimit
timeLimit = 0
class Strategy():   
    logging = True
    def best_strategy(self, board, player, best_move, running,time_limit):
        time.sleep(1)
        t = time.time()
        if board == '...........................ox......xo...........................':
            best_move.value = 19
            return
        elif board == '...........................ox......xx.......x...................':
            best_move.value = 29
            return
        elif board == '...................x.......xx......xo...........................':
            best_move.value = 34
            return
        elif board == '..........................xxx......xo...........................':
            best_move.value = 20
            return
        elif board == '...........................ox......xxx..........................':
            best_move.value = 43
            return
        elif board in theoryDct:
            best_move.value = theoryDct[board]
            return
        global timeLimit

        timeLimit = time_limit
        m = findMoves(board,player)[0]
        if len(m) == 1:
            best_move.value = int(*m)
        print(time_limit)
        best_move.value = quickMove(board, player,t, time_limit)
        #print(time_limit)
        return
        """print("reached")
        if running.value:
                global timeLimit

                timeLimit = time_limit
                best_move.value = quickMove(board, player,t, time_limit)
                print(time_limit)
                return"""
                


def main():
    nb = board
    token = defaultToken
    opT = opToken
    nb, token, opT = nb.upper(), token.upper(), opT.upper()
    possibleChoices, flippedSection = findMoves(nb,token)
    if not possibleChoices:
        token, opT = opT, token
        possibleChoices, flippedSection = findMoves(nb,token)
    #No move made B-E
    if (not moves and not verbose) or  verbose:
        printBoard(nb,possibleChoices)
        print("")
        print(nb + calcScore(nb))

        if possibleChoices:
            print(f"Possible moves for {token}: {possibleChoices}")
            print("")
        else:
            #print("No moves possible")
            print("")

    #if not moves:
        #moves.append(quickMove(nb,token))
    
    #new move A-E
    #loop here
    for move in moves:
        if move >= 0:
            if (move == moves[len(moves)-1] and  not verbose) or verbose:
                print(f"{token} plays to {move}") 
            nb = makeMove(nb, token, move, flippedSection)
            #swap tokens after the move
            token, opT = opT, token
            possibleChoices, flippedSection = findMoves(nb,token)
            if not possibleChoices:
                token, opT = opT, token
                possibleChoices, flippedSection = findMoves(nb,token)
            if (move == moves[len(moves)-1] and  not verbose) or verbose:
                printBoard(nb, possibleChoices, move)
                print("")
                print(nb + calcScore(nb))

                if possibleChoices:
                    print(f"Possible moves for {token}: {possibleChoices}")
                    print("")
                else:
                    #print("No moves possible")
                    print("")
                    #break

            #moves.append(quickMove(nb,token))
    #othello 4 part w quick move

    """if possibleChoices:
        t = time.time()
        print(f"my preferred move is: {quickMove(nb,token,t,1)}")
        a = nb.count(".")
        print(f"brd count: {a}")
        #for e in evaluateCache2:
            #ab = alphabeta(e[0].upper(), e[1].upper(), -10000, 10000, abCache,6,5)
            #print("('" + e[0] + "'" + "," + "'" + e[1] + "'" + ")" + ":" + str(ab[0]) +",")
        print("")
        print("")
        for i in range(200):
            brd, tkn = createRandom()
            if (brd, tkn) not in evaluateCache2:
                ab = alphabeta(brd.upper(), tkn.upper(), -10000, 10000, abCache,6,5)
                print("('" + brd + "'" + "," + "'" + tkn + "'" + ")" + ":" + str(ab[0]) +",") 
            evaluateCache2[(brd,tkn)] = ab[0]
        print("")
        print(TERMINALalphabeta(nb, token, -65,65, abCache))
        print(time.time()-t)
        if nb.count(".") < hl:
            ab =TERMINALalphabeta(nb, token, -65,65, abCache)
            print(f"Min Score: {ab[0]}; move sequence: {ab[1:]}")
        else:
            ab =alphabeta(nb, token, -10000,10000, abCache)
            print(f"Min Score: {ab[0]}; move sequence: {ab[1:]}")"""
    t = time.time()
    #print(hill_climbing(500,weights1))
    print(geneticAlgorithm(100))
    print(time.time()-t)


#global WEIGHTS
#WEIGHTS = []
global we
we = []
def playGame(strategy,control,token,controlNum = -1, strategyNum = -1):
    global abCache, evaluateCache, makeMoveCache, orderCache,moveCache
    if len(abCache) > 500000:
        abCache = {}
    if len(evaluateCache) > 500000:
        evaluateCache = {}
    if len(makeMoveCache) > 500000:
        makeMoveCache = {}
    if len(orderCache) > 500000:
        orderCache = {}
    if len(moveCache) > 500000:
        moveCache = {}


    
    flag = False
    #n = random.randrange(6,20)
    brd = ('.'*27 + "ox......xo" + '.'*27).upper()
    tkn = 'X'
    while brd.count('.') != 0:
        global we
        if tkn == token:
            we = strategy#[e for e in strategy]
            num = strategyNum
        else:
            we = control#[e for e in control]
            num = controlNum
        choices, fs = findMoves(brd, tkn)
        t=time.time()
        mv = quickMove(brd,tkn,t,2,num)
        if choices:
            flag = False
            brd = makeMove(brd,tkn,mv,fs)
        else:
            if flag: break
            flag = True
        tkn = "XO".replace(tkn,"")
    return brd

weight_ranges = [(-100, 100), (-200, 200), (300, 900), (-100, 100), (-100, 100), (-100, 500), (-150, 150), (-100, 100)]
wr2 = (-100,100)

#weights1 = [-35, 78.922, 601.724, 0, 45, 274.396, 60, 10,
                #-20, 0*178.922, 601.724, 0, 15, 74.396, 30, 10,
                #0*-20, 78.922, 601.724, 0, 0, 54.396, 30, 10,
                #0,  158.922, 801.724, 10, 0, 174.396, 30, 10]

weights1 = [-5,50,0,40,0,0,0,
            -5,60,200,50,0,0,0,
            -5,60,0,0,-10,20,0,
            -10,60,100,0,0,10,0,
            -10,40,0,0,0,10,0]



#weights2 = [-119.48610738026288, 45.578024445775355, 660.4188934536332, 188.37032879867246, 2.2238916144038114, 183.79909067700282, 20.443657744535642, 0.7071072381501267, 86.35611286507054, -53.15479546708378, 533.4381721930304, -115.93233795995866, 6.825324735281889, 192.16400530728725, 101.18619232958827, -0.4077071221842095, 168.9899219390522, 175.19773482964098, 1061.4037777840388, 166.66773215243688, 166.5880101056066, 211.11683087658952, 122.82912008728933, 91.30543105527951, -23.758979417280813, 182.39607718490188, 937.0466552104297, 149.66930515895382, -188.32111878301617, 188.2073725786239, -127.04425467631745, 52.02305991498427]
weights2 = [-5,50,0,10,0,0,0,
            -5,60,200,50,0,0,0,
            -5,60,0,0,-10,20,0,
            -5,60,100,10,10,0,0,
            0,0,0,0,0,0,0]


#weights3 = [-27.637694403780774, -168.11234889181202, 401.775295398147, -34.8796032976559, -136.06425112048424, 377.4499530312147, -56.48792946029275, -45.833036578646905, 1.9717948895773816, 97.61917077646751, 473.1248997176478, -115.72152283432628, -38.66566074596395, 459.0283686788568, 104.3802354907314, -52.44873025177872, 149.67744092996065, -138.43664407815575, 452.1310031281448, 156.75185660880197, -158.59756412691556, 418.03738056312955, 59.2786223368006, -37.56677975980334, 45.24696314949267, 199.7950972241547, 708.6317442024651, 115.54251255680754, 42.95048256084232, 412.6579445678732, 138.06549507898427, 25.367430418375744]
weights3 = [0,50,0,10,0,0,0,
            -10,60,200,50,0,0,0,
            -10,60,0,0,-10,20,0,
            0,60,100,10,10,0,0,
            -5,30,100,10,20,20,0]


#weights4 = [-139.2396019601405, -177.38930510173208, 284.0632954334342, 28.568015768183436, -13.7002257247442, 325.7794247071176, 112.70005887055899, 81.75486475227031, -78.88779776430893, 35.13894246082309, 852.9518600079293, -119.53374835260121, 144.36032922373653, 399.9180337676078, 53.12559698733632, 80.17307885759182, -69.4323786358878, 120.36515851907326, 954.3031613174212, 175.12675987362346, 1.1537140123330507, 123.52620996595336, -25.242609177028285, 92.33039301167821, 227.76652453578086, 168.68498633232926, 539.6276608484148, -90.79013187173982, -195.9460330365809, 326.99225008091923, 33.95771467870001, 100.42736594023118]
weights4 = [47.94661360115683, -20.815184527888192, -3.7484108685636524, -99.10598863081722, 79.13387250730713, 97.84098840030268, -46.61587634714879, -29.964463209597668, 60.01495740206295, -30.048157530153418, 61.33309164517918, 13.030102546270339, 36.50285514083563, 10.420368298233852, 48.461416334292224, -31.367088091815432, -70.75799541188627, 89.41025024615035, -33.52166917717361, -30.990084620723522, 18.97803577441229, -55.08660177775921, -17.951595893933273, 3.3520470467099983, 35.75904503275768, 72.38520965373706, -2.845850185527119, -54.25301232276185, -2.0182898502859827, 60.096292846415615, 14.539093268872548, 68.19972370198971, 55.510667069118114, -71.66843319441378, -88.97728918528087]
#weights5 = [1, 1, 1, 1, 1, 1, 1, 1,
            #-1, 2, 3, 4, 3, 2, 1, 0,
            #4, 1.922, 5.724, 4, 2, 3.396, 4, 5,
            #-1,1.922, 2.724, 5, 6, 7.396, 9, 4]
weights5 = [21.913873884106508, 9.700558552595536, 6.013212840433286, 71.31956076773548, -20.12361796291692, 57.925838025085625, -69.72979136341574, -95.5042442420076, 38.25196749727886, -8.726503132027247, -0.8345927533711869, 57.59557106541514, -8.879077695149155, -95.14297028755885, -25.14482805422176, -61.0413802744394, -78.55750115502323, 108.61415002953696, -12.599158302332185, -23.540952224549997, 21.072790269433263, -6.49103678768914, -98.18652852585382, 39.51689238270981, -8.28434266142784, -54.60961403107113, 41.33036434150645, 40.7068010038319, 82.56319566267598, -31.285936190898113, -30.500174601076164, -32.2424074531797, -50.04000596575429, 31.57516158938709, 12.945683182974276]

weights = [-35,0,601.724,15,15,374,60,20]

def evaluateWeights(strategy):
    global abCache, evaluateCache, makeMoveCache, orderCache,moveCache
    abCache= {}

    #evaluateCache = {}
    #makeMoveCache = {}
    #orderCache = {}
    #moveCache = {}

    tkn = 'X'
    eTkn = "XO".replace(tkn,"")
    brd = playGame(strategy,weights1,tkn,0,5)
    #printBoard(brd,{})
    f1 = (brd.count(tkn)-brd.count(eTkn))
    if f1 < 0:
        f1 *=2
    else:
        f1*=0.4

    brd = playGame(strategy,weights1,eTkn,0,5)
    f1b = (brd.count(eTkn)-brd.count(tkn))
    if f1b < 0:
        f1b *=2
    else:
        f1b*=0.4
    
    brd = playGame(strategy,weights2,tkn,1,5)
    #printBoard(brd,{})
    f2 = (brd.count(tkn)-brd.count(eTkn))
    if f2 < 0:
        f2 *=2
    else:
        f2*=0.3
    
    brd = playGame(strategy,weights2,eTkn,1,5)
    #printBoard(brd,{})
    f2b = (brd.count(eTkn)-brd.count(tkn))
    if f2b < 0:
        f2b *=2
    else:
        f2b*=0.3
    
    #printBoard(brd,{})
    brd = playGame(strategy,weights3,tkn,2,5)
    f3 = (brd.count(tkn)-brd.count(eTkn))
    if f3 < 0:
        f3 *=2
    else:
        f3*=0.3
    
    brd = playGame(strategy,weights3,eTkn,2,5)
    #printBoard(brd,{})
    f3b = (brd.count(eTkn)-brd.count(tkn))
    if f3b < 0:
        f3b *=2
    else:
        f3b*=0.3

    brd = playGame(strategy,weights4,tkn,3,5)
    f4 = (brd.count(tkn)-brd.count(eTkn))
    if f4 < 0:
        f4 *=2
    else:
        f4*=0.2
    
    brd = playGame(strategy,weights4,eTkn,3,5)
    f4b = (brd.count(eTkn)-brd.count(tkn))
    if f4b < 0:
        f4b *=2
    else:
        f4b*=0.2

    """brd = playGame(strategy,weights5,tkn)
    f5 = (brd.count(tkn)-brd.count(eTkn))
    if f5 < 0:
        f5 *=2
    else:
        f5*=0.2
    
    brd = playGame(strategy,weights5,eTkn)
    f5b = (brd.count(eTkn)-brd.count(tkn))
    if f5b < 0:
        f5b *=2
    else:
        f5b*=0.2"""
    
    fitnessScore = (f1+f2+f3+f4+f1b+f2b+f3b+f4b)/200
    return fitnessScore

def hill_climbing(iterations,ws):
    strategy = ws
    currentScore = evaluateWeights(strategy)

    # set the maximum and initial step size for each weight change
    max_step_size = 1000
    step_size = max_step_size

    

    for j in range(len(strategy)):
        # make a copy of the current weights to test potential changes
        new_weights = strategy.copy()
        step_size = max_step_size 
        # iterate through each weight to test different adjustments
        for i in range(iterations):
            status["abCache"] = 0
            print("-"*(i%20))
            if i%20==0 and i!= 0:
                print(f"Iteration {i}: score = {currentScore}, weightVal = {strategy[j]}, weightIdx = {j}, step = {step_size}")
            tkn = "OX"[random.randint(0, 1)]

            # test adding step_size to the weight
            new_weights[j] += step_size
            score = evaluateWeights(new_weights)
            if score > currentScore:
                # if the new weight improves the score, keep it and increase the step size
                strategy = new_weights
                currentScore = score
                step_size = min(max_step_size, step_size * 2)
            else:
                global abCache
                abCache= {}
                # otherwise, test subtracting step_size from the weight
                new_weights[j] -= 2 * step_size
                score = evaluateWeights(new_weights)
                if score > currentScore:
                    strategy = new_weights
                    currentScore = score
                    step_size = min(max_step_size, step_size * 2)
                else:
                    # if neither adjustment improves the score, reduce the step size and try again
                    new_weights[j] += step_size
                    step_size *=0.75
                    if step_size <1 :
                        break

        # print the current score and weights for each iteration
        print(f"Iteration {i}: score = {currentScore}, weights = {strategy}")
    
    return new_weights


    
    


def createPopulation():
    tkn = "OX"[random.randint(0, 1)] # choose mutation factor uniformly between 0.1 and 0.2
    new_weights = []
    for j in range(5):
        for i in range(7):
            # compute the range of valid values for this weight
            #weight_range = weight_ranges[i]
            weight_range = wr2
            # compute the range of valid mutations for this weight
            mutation_range = (weight_range[0], weight_range[1])
            # compute the mutation amount based on the mutation factor and the mutation range
            mutation = random.uniform(*mutation_range)# * mutation_factor
            # add the mutation to the current weight value
            new_weight = mutation
            # clamp the new weight value to the range of valid values
            #new_weight = max(weight_range[0], min(new_weight, weight_range[1]))
            new_weights.append(new_weight)
    return new_weights, tkn
    

def mutate_weights(weights, mutation_rate=0.25):
    new_weights = []
    for w in weights:
        if random.random() < mutation_rate:
            new_weights.append(random.uniform(-0.1, 0.1) * w + w)
        else:
            new_weights.append(w)
    return new_weights

def geneticAlgorithm(population_size):
    strategyLst = []
    for i in range(population_size):
        strategyLst.append(createPopulation())
    population = []
    n = 0
    for i,s in enumerate(strategyLst):
        print("-"*(n%10))
        fitnessScore = 0
        strategy, tkn = s
        eTkn = "XO".replace(tkn,"")
        brd = playGame(strategy,weights1,tkn,0,i+5)
        #printBoard(brd,{})
        f1 = (brd.count(tkn)-brd.count(eTkn))
        if f1 < 0:
            f1 =2 * (-f1)**0.5
        else:
            f1 =0.4 * f1**0.5
        brd = playGame(strategy,weights2,tkn,1,i+5)
        #printBoard(brd,{})
        f2 = (brd.count(tkn)-brd.count(eTkn))
        if f2 < 0:
            f2 =2 * (-f2)**0.5
        else:
            f2 =0.3 * f2**0.5
        #printBoard(brd,{})
        brd = playGame(strategy,weights3,tkn,2,i+5)
        f3 = (brd.count(tkn)-brd.count(eTkn))
        if f3 < 0:
            f3 =2 * (-f3)**0.5
        else:
            f3 =0.3 * f3**0.5

        brd = playGame(strategy,weights4,tkn,3,i+5)
        f4 = (brd.count(tkn)-brd.count(eTkn))
        if f4 < 0:
            f4 =2 * (-f4)**0.5
        else:
            f4 =0.2 * f4**0.5

        brd = playGame(strategy,weights5,tkn,4,i+5)
        f5 = (brd.count(tkn)-brd.count(eTkn))
        if f5 < 0:
            f5 =2 * (-f5)**0.5
        else:
            f5 =0.2 * f5**0.5
        fitnessScore = (f1+f2+f3+f4+f5)/100
        if n%10==0 and n!= 0:
            global status
            a = status["abCache"]
            print(f"population: {len(population)}")
            print(f"Cache Size: {len(abCache)}")
            print(f"abCached: {a}")
            status["abCache"] = 0
        n+=1
        population.append((fitnessScore,strategy,tkn))
    
    for p in population:
        print(f"Score: {p[0]}")
        print(f"weights: {p[1]}")
        print("")

    #sample_size = 16
    #tournament_group = random.sample(population, sample_size)
    newGen = []
    #tournament_group = sorted(tournament_group, key=lambda x: x[0], reverse=True)
    for ix in range(100):
        for i in range(population_size-2):
            if i% 5 == 0:
                print("-"*(i%20))  # 100 generations
            sample_size = 20
            tournament_group1 = random.sample(population, sample_size)
            tournament_group1 = sorted(tournament_group1, key=lambda x: x[0], reverse=True)

            tournament_group2 = []

            while len(tournament_group2) < len(tournament_group1):
                val = random.choice(population)
                if val not in tournament_group1 and val not in tournament_group2:
                    tournament_group2.append(val)

            tournament_group2 = sorted(tournament_group2, key=lambda x: x[0], reverse=True)

            s1, parent1,_ = tournament_group1[0]
            s2, parent2,_ = tournament_group2[0]
            idx = 1

            while random.random() > 0.75 and idx < len(tournament_group1):
                s1, parent1,_ = tournament_group1[idx]
                idx+=1

            idx = 1
            while random.random() > 0.75 and idx < len(tournament_group2):
                s2, parent2,_ = tournament_group2[idx]
                idx+=1
            
            offsprings = []
            for h in range(1):
                offspring = []
                #threshold = min(s1,s2)
                for j in range(len(parent1)):
                    if random.random() < 0.5:
                        offspring.append(parent1[j])
                    else:
                        offspring.append(parent2[j])
                # Mutate offspring before adding to population
                offspring = mutate_weights(offspring)
                offsprings.append(offspring)
            if i%20 == 0 and i != 0:
                print(f"BestOne: {population[0][1]}")
                print(i)
                print(f"Gen{ix}")
                
            for offspring in offsprings:
                fitnessScore = 0
                strategy, tkn = offspring, "OX"[random.randint(0, 1)]
                eTkn = "XO".replace(tkn,"")
                brd = playGame(strategy,weights1,tkn,0,i+5)
                f1 = (brd.count(tkn)-brd.count(eTkn))
                if f1 < 0:
                    f1 *=2
                else:
                    f1*=0.4
                brd = playGame(strategy,weights2,tkn,1,i+5)
                #printBoard(brd,{})
                f2 = (brd.count(tkn)-brd.count(eTkn))
                if f2 < 0:
                    f2 *=2
                else:
                    f2*=0.3
                #printBoard(brd,{})
                brd = playGame(strategy,weights3,tkn,2,i+5)
                f3 = (brd.count(tkn)-brd.count(eTkn))
                if f3 < 0:
                    f3 *=2
                else:
                    f3*=0.2

                brd = playGame(strategy,weights4,tkn,3,i+5)
                f4 = (brd.count(tkn)-brd.count(eTkn))
                if f4 < 0:
                    f4 *=2
                else:
                    f4*=0.2

                brd = playGame(strategy,weights5,tkn,1,i+5)
                f5 = (brd.count(tkn)-brd.count(eTkn))
                if f5 < 0:
                    f5 *=2
                else:
                    f5*=0.2
                fitnessScore = (f1+f2+f3+f4+f5)/100
                #if fitnessScore > threshold:
                newGen.append((fitnessScore, offspring, "OX"[random.randint(0, 1)]))
                # Keep population size fixed by removing lowest fitness individuals
        newGen.append(population[0])
        newGen.append(population[1])
        newGen = sorted(newGen, key=lambda x: x[0], reverse=True)
        population = newGen

    population = sorted(population, key=lambda x: x[0], reverse=True)
    return population
        
def update(s):
    global status
    if s in status:
        status[s]+=1
    else:
        status[s]=0

        #to here


global t1,t2,t3,t4,t5,top
top = 5
t1 = 4/5; t2 =  3.9/5; t3 = 0.7/5; t4 = 2.45/5; t5 = 3.2/5
def alphabeta(brd,tkn, alpha, beta, abCache,n=5,timeLeft = 0, secondBest = False,w = []):
    n-=1
    eTkn = "XO".replace(tkn,"")
    if n <= 0: 
        if timeLimit < 5:
            return [evaluate(brd,tkn,timeLimit,w)]
        t= time.time()
        if t-timeLeft >= t1*timeLimit or n < -2:
        #if timeLeft-t >= t1*timeLeft or n < -3:
            return [evaluate(brd,tkn, timeLimit,w)]
        if t-timeLeft <= t2*timeLimit and n< -1 and len(findMoves(brd,tkn)[0]) < 5:
        #if timeLeft-t <= t2*timeLeft and n< -1 and len(findMoves(brd,tkn)[0]) < 5:
            pass
        if t-timeLeft < t3*timeLimit:
        #elif timeLeft-t < t3*timeLeft:
            pass
        elif t-timeLeft <= t4*timeLimit and len(findMoves(brd,tkn)[0]) < 11:
        #elif timeLeft-t <= t4*timeLeft and len(findMoves(brd,tkn)[0]) < 11:
            pass
        elif t-timeLeft <= t5*timeLimit and len(findMoves(brd,tkn)[0]) < 7:
        #elif timeLeft-t <= t5*timeLeft  and len(findMoves(brd,tkn)[0]) < 7: 
            pass
        else:
            return [evaluate(brd,tkn,timeLimit,w)]
    possibleMoves, flippedSections= findMoves(brd,tkn)

    #if len(possibleMoves) <= 2: n+=1

    if (brd, tkn,alpha,beta,w) in abCache:
        update("abCache")
        return abCache[(brd, tkn,alpha, beta,w)]

    if not possibleMoves:
        if not findMoves(brd,eTkn)[0]:
            return [evaluate(brd,tkn,timeLimit,w)]

        if (brd, eTkn,-beta,-alpha,w) not in abCache:
            abCache[(brd, eTkn,-beta,-alpha,w)] = alphabeta(brd,eTkn,-beta,-alpha,abCache,n,timeLeft,secondBest,w)
        ab = abCache[(brd, eTkn,-beta,-alpha,w)]

        if -ab[0] < alpha: return [alpha-1]
        return [-ab[0]] + ab[1:] + [-1]
    
    bestSoFar = [alpha-1]

    for mv in orderMoves(brd,tkn,possibleMoves,flippedSections,timeLimit,n):
        #print(str(mv) + "  " + tkn)
       
        newBrd = makeMove(brd,tkn,mv,flippedSections)
        #printBoard(newBrd,{},mv)
        if (newBrd, eTkn,-beta,-alpha,w) not in abCache:
            abCache[(newBrd, eTkn,-beta,-alpha,w)] = alphabeta(newBrd,eTkn,-beta,-alpha,abCache,n,timeLeft,secondBest,w)
        ab = abCache[(newBrd, eTkn,-beta,-alpha,w)]
        score = -ab[0]
        if score < alpha: continue
        if score > beta: return[score]
        bestSoFar = [score] + ab[1:] + [mv]
        alpha = score + 1
    
    if (alpha != -10000 or alpha != -10001) and beta != 10000:
        abCache[(brd, tkn,alpha,beta,w)] = bestSoFar
    return bestSoFar

def evaluate(brd, tkn, tl, w):
    #if (brd, tkn) in evaluateCache:
        #return evaluateCache[(brd, tkn)]
    if brd.count(tkn) == 0:
        return -100
    aroundCorner = {1: 0, 8: 0, 9: 0, 6: 7, 14: 7, 15: 7, 48: 56, 49: 56, 57: 56, 54: 63, 55: 63, 62: 63}
    aroundEdgeToEdge = {1:[0,1,2,3,4,5,6,7], 6:[0,1,2,3,4,5,6,7], 8:[0,8,16,24,32,40,48,56], 48:[0,8,16,24,32,40,48,56],
                        57:[56,57,58,59,60,61,62,63], 62:[56,57,58,59,60,61,62,63], 15:[7,15,23,31,39,47,55,63], 55:[7,15,23,31,39,47,55,63]}
    #verticals = [[0,8,16,24,32,40,48,56],[7,15,23,31,39,47,55,63]]

    eTkn = "XO".replace(tkn,"")
    tct = brd.count(tkn)
    ect = brd.count(eTkn)
    if ect == 0: return 100000
    """table_weights = [120, -20, 20, 5, 5, 20, -20, 120,     
                    -20, -70, -5, -5, -5, -5, -70, -20,     
                    20, -5, 15, 3, 3, 15, -5, 20,     
                    5, -5, 3, 3, 3, 3, -5, 5,    
                    5, -5, 3, 3, 3, 3, -5, 5,     
                    20, -5, 15, 3, 3, 15, -5, 20,     
                    -20, -70, -5, -5, -5, -5, -70, -20,     
                    120, -20, 20, 5, 5, 20, -20, 120]"""

    table_weights = [20, -3, 11, 8, 8, 11, -3, 20,     
                    -3, -7, -4, 1, 1, -4, -7, -3,     
                    11, -4, 2, 2, 2, 2, -4, 11,     
                    8, 1, 2, 5, 5, 2, 1, 8,    
                    8, 1, 2, 5, 5, 2, 1, 8,     
                    11, -4, 2, 2, 2, 2, -4, 11,     
                    -3, -7, -4, 1, 1, -4, -7, -3,     
                    20, -3, 11, 8, 8, 11, -3, 20]

    if brd[0] == tkn:
        table_weights[1]=3
        table_weights[9]=7
        table_weights[8]=3
        if eTkn in brd[1] or eTkn in brd[8]:
            table_weights[0] == -10
    if brd[7] == tkn:
        table_weights[6]=3
        table_weights[14]=7
        table_weights[15]=3
        if eTkn in brd[6] or eTkn in brd[15]:
            table_weights[7] == -10
    if brd[56] == tkn:
        table_weights[48]=3
        table_weights[49]=7
        table_weights[57]=3
        if eTkn in brd[48] or eTkn in brd[57]:
            table_weights[56] == -10
    if brd[63] == tkn:
        table_weights[62]=3
        table_weights[55]=7
        table_weights[54]=3
        if eTkn in brd[62] or eTkn in brd[54]:
            table_weights[63] == -10

    corners = {0, 7, 56, 63}
    

    #printBoard(brd, {})
    #print("")
    
    if "." not in brd:
        return 100*(brd.count(tkn)-brd.count(eTkn))/64
    score = -100
    #coin parity
    cpScore = 100* (tct-ect)/(tct+ect)
    #cpScore = brd.count(tkn)-brd.count(eTkn)
    #mobility
    moves,_ = findMoves(brd,tkn)
    eMoves,_ = findMoves(brd,eTkn)
    mobScore = 0
    pm = potentialMobility(brd, eTkn)
    pmE = potentialMobility(brd, tkn)

    edges = [0,1,2,3,4,5,6,7,56,57,58,59,60,61,62,63,8,16,24,32,40,48,15,23,31,39,47,55]
    pmct = 0
    pmEct = 0
    for t in brd:
        if t==tkn and t not in edges:
            pmct+=1
        if t==eTkn and t not in edges:
            pmEct +=1

    pm/=pmct
    pmE/=pmEct

    pmScore = 0
    if pm + pmE != 0:
        pmScore = 100 * (pm-pmE)/(pm + pmE)

    
    if len(moves) > 0 or len(eMoves) > 0:
        mobScore = 100 * (len(moves)-len(eMoves))/(len(moves)+len(eMoves))
    
    #if brd.count(".") > 37:
        #return (pmScore*174 + mobScore* 178)/(174+178)
        #mobScore = len(moves)-len(eMoves)
    #corners
    numCorners = len(corners.intersection(moves))*0.91
    eNumCorners = len(corners.intersection(eMoves))*0.91
    numCorners = 0
    cScore = 0
    if numCorners + (brd[0] == tkn) + (brd[7] == tkn) + (brd[56] == tkn) + (brd[63] == tkn) + (
        eNumCorners + (brd[0] == eTkn) + (brd[7] == eTkn) + (brd[56] == eTkn) + (brd[63] == eTkn)) != 0:

        cScore = 100*(numCorners + (brd[0] == tkn) + (brd[7] == tkn) + (brd[56] == tkn) + (brd[63] == tkn) 
         - (eNumCorners + (brd[0] == eTkn) + (brd[7] == eTkn) + (brd[56] == eTkn) + (brd[63] == eTkn)))/(
             numCorners + (brd[0] == tkn) + (brd[7] == tkn) + (brd[56] == tkn) + (brd[63] == tkn) + (
            eNumCorners + (brd[0] == eTkn) + (brd[7] == eTkn) + (brd[56] == eTkn) + (brd[63] == eTkn)))

    if cScore != 0:
        if brd[0] == tkn:
            if eTkn in brd[1] or eTkn in brd[8]:
                cScore -=10
        if brd[7] == tkn:
            if eTkn in brd[6] or eTkn in brd[15]:
                cScore -=10
        if brd[56] == tkn:
            if eTkn in brd[48] or eTkn in brd[57]:
                cScore -=10
        if brd[63] == tkn:
            if eTkn in brd[62] or eTkn in brd[54]:
                cScore -=10
        
        if brd[0] == eTkn:
            if tkn in brd[1] or tkn in brd[8]:
                cScore +=5
        if brd[7] == eTkn:
            if tkn in brd[6] or tkn in brd[15]:
                cScore +=5
        if brd[56] == eTkn:
            if tkn in brd[48] or tkn in brd[57]:
                cScore +=5
        if brd[63] == eTkn:
            if tkn in brd[62] or tkn in brd[54]:
                cScore +=5

    #cScore = numCorners + (brd[0] == tkn) + (brd[7] == tkn) + (brd[56] == tkn) + (brd[63] == tkn)
    #cScore -= eNumCorners + (brd[0] == eTkn) + (brd[7] == eTkn) + (brd[56] == eTkn) + (brd[63] == eTkn)
    #stability
    
    """stable = stableCount(brd,tkn,eTkn)
    eStable = stableCount(brd,eTkn,tkn)
    sScore = 0
    stable = stable/ tct
    eStable = eStable/ ect
    if stable or eStable:
        sScore = 100*(stable - eStable)/(stable + eStable)"""

    #edge Stability

    """edge = edgeStability(brd,tkn,eTkn)
    eEdge = edgeStability(brd,eTkn,tkn)
    eScore = 0
    if edge + eEdge != 0:
        eScore = 100*(edge - eEdge)/(edge + eEdge)"""
    
    eScore, eDiff = edgeStability2(brd,tkn,eTkn)
    
    #More edgeStability

    m = dfc(brd,tkn)
    em = dfc(brd,eTkn)
    m/=pmct
    em/=pmEct
    msScore = 0
    if m + em != 0:
        msScore = 100*(m - em)/(m + em)
    
    

    
    tScore = 0
    eTScore = 0
    for i in range(64):#[1,8,9, 6,14,15, 48,49,57, 54,55,62]:
        if brd[i] == tkn:
            tScore += table_weights[i]
        if brd[i] == eTkn:
            eTScore += table_weights[i]
    
    #tScore/= tct
    #eTScore/= ect

    if tScore + eTScore != 0:
        tScore = 100*(tScore - eTScore)/(tScore + eTScore)
    else:
        tScore = 0

    acScore = 0
    macScore = 0
    eacScore = 0
    for e in aroundCorner:
        if brd[e] == tkn:
            if brd[aroundCorner[e]] == ".":
                if e not in [9,14,54,49] and e in aroundEdgeToEdge and eTkn not in [brd[i] for i in aroundEdgeToEdge[e]]: continue
                else: eacScore += 20
                #eacScore += 20
            elif e not in [9,14,54,49] and brd[aroundCorner[e]] == eTkn:
                macScore += 1
            elif e not in [9,14,54,49] and brd[aroundCorner[e]] == tkn:
                macScore += 20
            else:
                eacScore += 20
        if brd[e] == eTkn:

            if brd[aroundCorner[e]] == ".":
                if e not in [9,14,54,49] and e in aroundEdgeToEdge and tkn not in [brd[i] for i in aroundEdgeToEdge[e]]: continue
                else: macScore += 20
                #macScore += 20
            elif e not in [9,14,54,49] and brd[aroundCorner[e]] == tkn:
                eacScore += 1
            elif e not in [9,14,54,49] and brd[aroundCorner[e]] == eTkn:
                eacScore += 20
            else:
                macScore += 20
    
    if macScore + eacScore != 0:
        acScore = 100*(macScore - eacScore)/(macScore + eacScore)
    
        """WEIGHTS = [-35, 0*78.922, 601.724, -15, 45, 274.396, 60, 20,
                -20, 78.922, 501.724, -15, 15, 254.396, 60, 20,
                0, 158.922, 601.724, 5, 0, 154.396, 60, 20,
                0,  158.922, 801.724, 5, 0, 174.396, 60, 20]"""

    """WEIGHTS = [-35, 0*78.922, 601.724, -15, 45, 274.396, 60, 20,
                0*-20, 178.922, 501.724, -10, 15, 254.396, 30, 20,
                0*-20, 78.922, 601.724, 0, 0, 254.396, 30, 20,
                0,  158.922, 801.724, 10, 0, 174.396, 30, 20]"""
    
    WEIGHTS = [-35, 0*78.922, 501.724, 0, 45, 274.396, 90, 0*10,
                -20, 58.922, 501.724, 0, 15, 54.396, 90, 0*10,
                -5, 78.922, 501.724, 5,0, 74.396, 90, 0*20,
                0,  78.922, 501.724, 15, 0, 74.396, 90, 0*20]
    w1, w2, w3, w4, w5, w6, w7, w8 = WEIGHTS[0],WEIGHTS[1],WEIGHTS[2],WEIGHTS[3],WEIGHTS[4],WEIGHTS[5],WEIGHTS[6],WEIGHTS[7]
    if brd.count(".") <= 50: 
        w1, w2, w3, w4, w5, w6, w7, w8 = WEIGHTS[8],WEIGHTS[9],WEIGHTS[10],WEIGHTS[11],0*WEIGHTS[12],WEIGHTS[13],WEIGHTS[14],WEIGHTS[15]
        #if eDiff < -0.275:
            #w4+=10
    if brd.count(".") <= 40: 
        w1, w2, w3, w4, w5, w6, w7, w8 = WEIGHTS[16],WEIGHTS[17],WEIGHTS[18],WEIGHTS[19],0*WEIGHTS[20],WEIGHTS[21],WEIGHTS[22],WEIGHTS[23]
        #if eDiff < -0.275:
            #w2+=75
    if brd.count(".") <= 20: 
        w1, w2, w3, w4, w5, w6, w7, w8 = WEIGHTS[24],WEIGHTS[25],WEIGHTS[26],WEIGHTS[27],WEIGHTS[28],WEIGHTS[29],WEIGHTS[30],WEIGHTS[31]
        #if eDiff < -0.275:
            #w4+=100
    if brd.count(".") <= 10: 
        w1, w2, w3, w4, w5, w6, w7, w8 = 5,178,500,35,45,0,0,0


    if pmScore > 25:
        w1-=we[0]
        w2+=we[1]
        w3+=we[2]
        w4+=we[3]
        w5+=we[4]
        w6+=we[5]
        w7+=we[6]
    if msScore <-10 and pmScore < -20:
        w1-=we[7]
        w2+=we[8]
        w3+=we[9]
        w4+=we[10]
        w5+=we[11]
        w6+=we[12]
        w7+=we[13]
    if eDiff > 2:
        w1-=we[14]
        w2+=we[15]
        w3+=we[16]
        w4+=we[17]
        w5+=we[18]
        w6+=we[19]
        w7+=we[20]
        
    if mobScore <-20:# and brd.count(".") > 10:
        w1-=we[21]
        w2+=we[22]
        w3+=we[23]
        w4+=we[24]
        w5+=we[25]
        w6+=we[26]
        w7+=we[27]

    if mobScore > 40 and brd.count(".") > 10:
        w1-=we[28]
        w2+=we[29]
        w3+=we[30]
        w4+=we[31]
        w5+=we[32]
        w6+=we[33]
        w7+=we[34]
        

  

    tW = w1+w2+w3+w4+w5+w6+w7+w8
    #tW = w1+w2+w3+w5+w6+w7
    score = (cpScore*w1 + mobScore*w2 + cScore*w3 + eScore*w4 + msScore*w5 + pmScore*w6 + acScore*w7 + tScore*w8)
    #score = (cpScore*w1 + mobScore*w2 + cScore*w3 + tScore*w5 + pmScore*w6 + acScore*w7)/tW
    #if tl == 1:
        #print(time.time()-TIME)
    
    evaluateCache[(brd, tkn)] = score

    return score

def dfc(brd,tkn):
    dfcScore = 0
    board = [[brd[i*8 + j] for j in range(8)] for i in range(8)]
    center_x, center_y = 3.5,3.5
    for i in range(8):
        for j in range(8):
            if board[i][j] == tkn:
                distance_from_center = ((i-center_x)**2 + (j-center_y)**2)**0.5
                weight = max(0, 1 - distance_from_center/8)
                dfcScore+=weight
    return dfcScore

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
        if "x.x" in eString or "o.o" in eString: continue
        eString.replace(".","")
        length = len(eString)
        total += length
        if length > 1:
            if "ox" in eString or "xo" in eString: continue
            elif tkn in eString: myTotal+= length
            elif eTkn in eString: eTotal+= length
    
    if total != 0: return 100*(myTotal - 0)/total, myTotal
    return 0, 0

def stability2(board_str, token):
    # Convert the board string to a 2D list of characters
    board = [[board_str[i*8 + j] for j in range(8)] for i in range(8)]

    stability_score = 0
    n = len(board)
    center_x, center_y = (n-1)/2, (n-1)/2

    for i in range(n):
        for j in range(n):
            if board[i][j] == token:
                adjacent_tokens = get_adjacent_tokens(board, i, j)
                potential_flips = sum([potential_flips for x, y, potential_flips in adjacent_tokens])
                stability = potential_flips + 1
                distance_from_center = ((i-center_x)**2 + (j-center_y)**2)**0.5
                # give more weight to positions closer to the center of the board
                weight = max(0, 1 - distance_from_center/n)
                stability_score += stability * weight

    return stability_score


def get_adjacent_tokens(board, i, j):
    n = len(board)
    directions = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if not (dx == 0 and dy == 0)]
    adjacent_tokens = []
    for dx, dy in directions:
        x = i + dx
        y = j + dy
        if 0 <= x < n and 0 <= y < n:
            adjacent_tokens.append((x, y, count_potential_flips(board, i, j, dx, dy)))
    return adjacent_tokens

def count_potential_flips(board, i, j, dx, dy):
    n = len(board)
    token = board[i][j]
    flips = 0
    x = i + dx
    y = j + dy
    while 0 <= x < n and 0 <= y < n:
        if board[x][y] == token:
            return flips
        elif board[x][y] == '.':
            return 0
        else:
            flips += 1
        x += dx
        y += dy
    return 0

def edgeStability(brd, tkn, eTkn):
    # check vertical
    horizontals = [[0,1,2,3,4,5,6,7],[56,57,58,59,60,61,62,63]]
    verticals = [[0,8,16,24,32,40,48,56],[7,15,23,31,39,47,55,63]]
    hv = horizontals + verticals

    #case 1 ox.
    #case 2 oxo
    #case 3 .xo
    #case 4 xxx

    total = 0
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
                #sfCount = 0
                return 0

            if brd[prev] == "." and brd[i] == tkn:
                c3 = True
            if brd[i] == "." and c3:
                c4 = True
            if brd[i] == eTkn and c3 and not c4:
                #sfCount = 0
                return 0 
            prev = i
        if sfCount > 1:
            total+=sfCount


    """for h in hv:
        for i in h:
            if brd[i] == tkn:
                totalTkns +=1
            if brd[i] == eTkn:
                totalEtkns += 1

    if totalTkns == 0: return 0
    if totalEtkns > 0 or totalTkns > 1:
        return total/totalTkns
    else: return 0"""
    return total



                



def TERMINALalphabeta(brd,tkn, alpha, beta, abCache):
    eTkn = "XO".replace(tkn,"")
    if "." not in brd: 
        return [brd.count(tkn)-brd.count(eTkn)]
    possibleMoves, flippedSections= findMoves(brd,tkn)

    if (brd, tkn,alpha,beta) in abCache:
        return abCache[(brd, tkn,alpha,beta)]

    if not possibleMoves:
        if not findMoves(brd,eTkn)[0]:
            return [brd.count(tkn)-brd.count(eTkn)]

        if (brd, eTkn,-beta,-alpha) not in abCache:
            abCache[(brd, eTkn,-beta,-alpha)] = TERMINALalphabeta(brd,eTkn,-beta,-alpha,abCache)
        ab = abCache[(brd, eTkn,-beta,-alpha)]

        if -ab[0] < alpha: return [alpha-1]
        return [-ab[0]] + ab[1:] + [-1]
    
    bestSoFar = [alpha-1]
    for mv in orderMoves(brd,tkn,possibleMoves,flippedSections):
        newBrd = makeMove(brd,tkn,mv,flippedSections)

        if (newBrd, eTkn,-beta,-alpha) not in abCache:
            abCache[(newBrd, eTkn,-beta,-alpha)] = TERMINALalphabeta(newBrd,eTkn,-beta,-alpha,abCache)
        ab = abCache[(newBrd, eTkn,-beta,-alpha)]
        score = -ab[0]
        if score < alpha: continue
        if score > beta: return[score]
        bestSoFar = [score] + ab[1:] + [mv]
        alpha = score + 1
    
    abCache[(brd, tkn,alpha,beta)] = bestSoFar
    return bestSoFar

global stabilityCache, groupCache, isStableCache
stabilityCache, groupCache, isStableCache = {}, {}, {}

def stability(brd, tkn):
    if (brd, tkn) in stabilityCache:
        return stabilityCache[(brd, tkn)]

    stableDisks = []
    visited = set()
    for i,s in enumerate(brd):
        if s == tkn and i not in visited:
            group = connectedGroup(brd, tkn, i, set())
            if isStable(brd, group, tkn):
                stableDisks += group
                visited |= {*group}
    stabilityCache[(brd, tkn)] = stableDisks
    return stableDisks

def connectedGroup(brd, tkn, i,vs):
    if (brd, tkn, i) in groupCache:
        return groupCache[(brd, tkn, i)]
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
    groupCache[(brd, tkn, i)] = group
    return group

def isStable(brd, group, tkn):
    #if (brd, group, tkn) in isStableCache:
        #return isStableCache[(brd, group, tkn)]
    #REMEMBER TO MAKE "ox" UPPERCASE
    eTkn = "XO".replace(tkn,"")
    for i in group:
        for dx in [1,-1,8,-8,9,-9,7,-7]:
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
                        #isStableCache[(brd, group, tkn)] = False
                        return False
                    j += -dx
    #isStableCache[(brd, group, tkn)] = True
    return True

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


#global pmCache 
#pmCache = {}
def potentialMobility(board, eTkn):
    tkn = "XO".replace(eTkn,"")
    edges = {0,1,2,3,4,5,6,7,56,57,58,59,60,61,62,63,8,16,24,32,40,48,15,23,31,39,47,55}
    #if (board, eTkn) in pmCache:
        #return pmCache[(board,eTkn)]
    directions = [1,-1,8,-8]#,9,-9,7,-7]
    count = 0
    c2 = 0
    if board.count(".") < 32:
        for i in range(64):
            if board[i] == "." and i not in edges:
                for e in directions:
                    if 0<= i + e < 64 and board[i+e] == eTkn:
                        if (((i + e) % 8 == 0 and e in [1,9,-7]) or 
                        ((i + e) % 8 == 8 - 1 and e in [-1,7,-9])):
                            continue
                        else:
                            if e in {1,-1,8,-8}:
                                count += 2
                            else:
                                count+=1
                            break
        #pmCache[(board,eTkn)] = count
        return count
    else:
        for i in range(64):
            if board[i] == eTkn and i not in edges:
                c2=0
                flag = False
                for e in directions:
                    if 0<= i + e < 64 and board[i+e] == ".":
                        if (((i + e) % 8 == 0 and e in [1,9,-7]) or 
                        ((i + e) % 8 == 8 - 1 and e in [-1,7,-9])):
                            continue
                        else:
                            count += 2
                            flag = True
                            c2=0
                            break
                    """if 0<= i + e < 64 and not flag and board[i+e] == tkn:
                        if (((i + e) % 8 == 0 and e in [1,9,-7]) or 
                        ((i + e) % 8 == 8 - 1 and e in [-1,7,-9])):
                            continue
                        else:
                            c2+=1"""
                count+=c2


        #count = count/board.count(eTkn)
        #pmCache[(board,eTkn)] = count
        return count

def isStableEdge(brd,tkn, eTkn, edge):
    edgeString = [brd[i] for i in edge]
    if tkn in edgeString and eTkn in edgeString: return False, 0
    if tkn not in edgeString: return False, 0
    return True, edgeString.count(tkn)

def checkStability(brd, tkn, eTkn):
    h1, h2 =   [1,2,3,4,5,6],[57,58,59,60,61,62]  
    v1, v2 =   [8,16,24,32,40,48],[15,23,31,39,47,55]
    edges = []
    edges.append(h1)
    edges.append(h2)
    edges.append(v1)
    edges.append(v2)
    total = 0
    for edge in edges:
        isStable, count = isStableEdge(brd,tkn,eTkn, edge)
        if isStable:
            if edge == h1:
                _, c2 = isStableEdge(brd, tkn, eTkn, [i+8 for i in edge])
                total += count + c2
            elif edge == h2:
                _, c2 = isStableEdge(brd, tkn, eTkn, [i-8 for i in edge])
                total += count + c2
            elif edge == v1:
                _, c2 = isStableEdge(brd, tkn, eTkn, [i+1 for i in edge])
                total += count + c2
            elif edge == v2:
                _, c2 = isStableEdge(brd, tkn, eTkn, [i-1 for i in edge])
                total += count + c2
    return total
            









def turn(b):
   cnt = 0
   for x in b:
        if(x == "."):
            cnt = cnt + 1
   if(cnt % 2 != 0):
        return "O"
   else:
        return "X"

def printBoard(b,possibleChoices, mv = None):
    s=b
    if possibleChoices:
        for i in possibleChoices:
            s = s[:i] + "*" + s[i+1:]
    s = s.lower()
    if mv:
        s = s[:mv] + s[mv].upper() + s[mv+1:]
        
    print("\n".join([s[x : x + side] for x in range(0,length,side)]))

def findMoves(b,token):
    b = b.upper()
    token = token.upper()
    index = 0
    choiceSet = set()
    #global flippedSection 
    flippedSection = []
    directions = [1,-1,8,-8,9,-9,7,-7]
    opT = {"X","O"} - {token.upper()}
    opT = "".join(opT)
    if (b, token) in moveCache:
        return moveCache[(b, token)]
    for i,s in enumerate(b):
        if s == ".":
    #for i in dotSet:
            for x in directions:
                index = i
                flag = False
                while 0<= index < length:
                    if ((index % side == 0 and x in [-1,-9,7]) or
                        (index % side == side - 1 and x in [1,-7,9] )):
                        break
                    if 0<= index < length and b[index] == token: break
                    if 0<= index < length and flag and b[index] == ".": break
                    flag = True
                    index += x
                if 0 <= index < 64 and b[index] == token and b[index - x] != ".":

                    flippedSection.append((index,i,-x))
                    choiceSet.add(i)
    moveCache[(b, token)] = (choiceSet,flippedSection)
    


    return choiceSet,flippedSection
global makeMoveCache
makeMoveCache = {}
def makeMove(b, token, move, flippedSection):
    #dotSet.remove(move)
    if (b,token,move) in makeMoveCache: return makeMoveCache[(b,token,move)]
    b=b.upper()
    token = token.upper()
    seenDirection = set()
    start = 0
    for sect in flippedSection:#[move]:
        firstOccurance = False
        if move == sect[1] and sect[2] not in seenDirection:
            start, end, direction = sect
            while end != start:
                if b[end] != token:
                    if b[end] != ".":
                        firstOccurance = True
                    b = b[:end] + token + b[end+1:]
                    
                elif firstOccurance: 
                    break
                end -= direction
            seenDirection.add(direction)        
    makeMoveCache[(b,token,move)] = b
    return b

def quickMove(board, token, time = 0,tl = 1,w = -1):
#set globals
    
    
    flag = True
    if board in theoryDct:
        return theoryDct[board]
    global hl
    if tl == 1: hl = 7
    elif tl == 2: hl = 12
    elif tl == 4: hl = 12
    elif tl == 5: hl = 13

    if tl == 1 and board.count(".") > hl:
        i=5
        #if len(findMoves(board,token)[0]) > 6:
        #    i = 2
        ab = alphabeta(board.upper(), token.upper(), -1000000, 1000000, abCache,i,time, w=w)
        print("('" + board + "'" + "," + "'" + token + "'" + ")" + ":" + str(ab[0]) +",")
        return ab[-1]
    board = board.upper()
    token = token.upper()
    if 0 < board.count(".") <hl:
        if len(findMoves(board,token)[0]) > 8 and tl <=6:
            hl -= 1
        else:
            return TERMINALalphabeta(board, token, -65, 65, abCache)[-1]
    if tl == 1:
        n = 2
    if tl < 4:
        n = 4
    else:
        n = 5
    ab = alphabeta(board, token, -1000000, 1000000, abCache,n,time,w=w)
    #print(ab)
    #print(f"n = {n}")
    return ab[-1]


def orderMoves(board, token, possibleChoices,fs,tl = 100, n = 10):
    if (board, token) in orderCache:
        return orderCache[(board, token)]
    table_weights = [20, -3, -1, -1, -1, -1, -3, 20,     
                    -3, -7, -4, -2, -2, -4, -7, -3,     
                    -1, -4, -1, 2, 2, -1, -4, -1,     
                    -1, -2, 2, 2, 2, 2, -2, -1,    
                    -1, -2, 2, 2, 2, 2, -2, -1,     
                    -1, -4, -1, 2, 2, -1, -4, -1,     
                    -3, -7, -4, -2, -2, -4, -7, -3,     
                    20, -3, -1, -1, -1, -1, -3, 20]
    cornerToEdges = {0: {1,2,3,4,5,6,7,8,16,24,32,40,48,56},
             7: {0,1,2,3,4,5,6,15,23,31,39,47,55,63},
             56: {0,8,16,24,32,40,48,57,58,59,60,61,62,63},
             63: {7,15,23,31,39,47,55,56,57,58,59,60,61,62}}
    edgeToCorner = {edgeInd: corner for corner in cornerToEdges for edgeInd in cornerToEdges[corner]}
    corners = {0, 7, 56, 63}
    aroundCorner = {1: 0, 8: 0, 9: 0, 6: 7, 14: 7, 15: 7, 48: 56, 49: 56, 57: 56, 54: 63, 55: 63, 62: 63}
    edges = [0,1,2,3,4,5,6,7,56,57,58,59,60,61,62,63,8,16,24,32,40,48,15,23,31,39,47,55]
    horizontals = [[0,1,2,3,4,5,6,7],[56,57,58,59,60,61,62,63]]
    h1, h2 =   [1,2,3,4,5,6],[57,58,59,60,61,62]  
    v1, v2 =   [8,16,24,32,40,48],[15,23,31,39,47,55]
    verticals = [[0,8,16,24,32,40,48,56],[7,15,23,31,39,47,55,63]]
    dc = board.count(".")


    
    opT = {"O","X"} - {token}
    opT = "".join(opT)
    sortedMoves = []

    for move in possibleChoices:
        safeEdgeFlag = False
        score = 0
        score+= table_weights[move]
        if move in corners:
            score += 70

        elif move in edgeToCorner:
            if board[edgeToCorner[move]] == token:
                score += 3
        if move in edges and tl == 1 and dc < 37:
                if move in h1:
                    a = [board[i] for i in h1]
                    if opT not in a and token in a:
                        score += 2
                    #if dc < 37:
                        safeEdgeFlag = True
                    #else: score-=2
                elif move in h2:
                    a = [board[i] for i in h2]
                    if opT not in a and token in a: 
                        score += 2
                    #if dc < 37:
                        safeEdgeFlag = True
                    #else: score-=2
                elif move in v1:
                    a = [board[i] for i in v1]
                    if opT not in a and token in a: 
                        score += 2
                    #if dc < 37:
                        safeEdgeFlag = True
                    #else: score-=2
                elif move in v2:
                    a = [board[i] for i in v2]
                    if opT not in a and token in a: 
                        score += 2
                    #if dc < 37:
                        safeEdgeFlag = True
                    #else: score-=2
        #if move in edges and tl != 1:
            #score -= 2
        #else:
        if move not in edges:
            for n in [1,-1,8,-8]:#,9,-9,7,-7]:
                if move+n >= 0 and move+n < length and board[move+n] == '.': 
                    if dc < 37: score -= 9
                    else: score -= 19
                if move+n >= 0 and move+n < length and board[move+n] == opT: 
                    score += 2
                if move+n >= 0 and move+n < length and board[move+n] == token: 
                    score += 2
        if move in aroundCorner and not safeEdgeFlag:
            if board[aroundCorner[move]] == '.':
                score = -70
            elif board[aroundCorner[move]] == opT:
                score = -69
        #mobility
        """newB = makeMove(board,token,move,fs)

        eChoices,_ = findMoves(newB,opT)
        choices,_ = findMoves(newB,token)
        if eChoices or choices:
            score += 4*(len(choices) - len(eChoices)) / (len(choices) + len(eChoices))"""
        sortedMoves.append((score, move))

    
        
    
    sortedMoves.sort(reverse=True)
    moves = [t[1] for t in sortedMoves]
    
    if tl < 2:
        #if n <= 1 and len(moves) >= 4:
           #moves =  [moves[i] for i in range(4)]
        if len(moves) >= 8:
            moves = [moves[i] for i in range(len(moves)*2//7)]
        elif len(moves) >= 4:
            moves = [moves[i] for i in range(len(moves)*1//4)]
    #elif len(moves) >= 10:
        #moves = [moves[i] for i in range(len(moves))]

    orderCache[(board, token)] = moves
    return moves

def calcScore(b):
    x = b.count("X")
    y = b.count("O")
    return f"  {x}/{y}"       
            
def condensePath(nums):
    nums = nums.replace("_", "0")
    #if not nums.isnumeric():
        #return
    for i in range(0,len(nums),2):
        if nums[i] != "-" and nums[i+1] != "-":
            moves.append(int(nums[i] + nums[i+1]))
        


#def setGlobals(s):
s = args
global side, length, board, defaultToken, moves, opToken, nmCache,verbose,abCache, status, moveCache, hl
global dotSet, orderCache, evaluateCache, theoryDct, score, evaluateCache2
score = 0
theoryDct = {

'...........................ox......xo...........................':19,
'...................x.......xx.....ooo...........................':45,
'...................xo......ox.....oox........x..................':18,
'..................xxo......xx.....oooo.......x..................':21,
'............o.....xxox.....xo.....oooo.......x..................':13,
'...........oox....xoxx.....oo.....oooo.......x..................':3,
'...x.o.....oox....xoxx.....oo.....oooo.......x..................':29,
'...........................ox......xx.......x...................':29,
'..................x........xoo.....xx.......x...................':26,
'..................xx......oxoo.....xx.......x...................':43,
'..................xxx.....oxxo.....xx......ox...................':10,
'..........o......xxxx.....xxxo.....xx......ox...................':34,
'..........o......xoxx....xxxxo....oxx......ox...................':21,
'..........ox.....xxxoo...xxxxo....oxx......ox...................':12,
'..x.......xoo....xxxoo...xxxxo....oxx......ox...................':33,
'...................x.......xx.....oooo.......x..................':44,
'...................xo......ox.....ooxo......xx..................':43,
'...................xo......xx.....oxxo.....xxo.......o..........':46,
'...................xo.....oxx.....ooxx.....xoxx......o..........':42,
'...................xo.....oxx.....oxxx....oxoxx...o..o..........':52,
'...................xoo....oxo.....ooxx....oxxxx...o.xo..........':29,
'...................xoo....oxox....ooox....oxoxx...o.oo......o...':51,
'....................o.....xxo......xo...........................':45,
'....................o.....xxo......xo.......ox..................':37,
'....................o.....xoo.....oxxx......ox..................':29,
'....................o.....xxxx....oxxx......ooo.................':51,
'....................o.....xxxx....oxxx.....oooo....x............':42,
'...................x.......xx.....ooxo......oo.......o..........':42,
'...................x.......xx.....oxxo....o.oo....o..o..........':33,
'...................x....o..xx....oxxxo....o.oo....o..o..........':46,
'...................x....o..xx....oxxxx....o.oooo..o..o..........':61,
'...................x....o.oxx....oooxx....o.oxoo..o..x.......x..':52,
'...................xo......xo......xo...........................':29,
'..................ooo......oxx.....xo...........................':37,
'..................ooo......oox.....xox......o...................':21,
'..................ooox.....oooo....xoo......o...................':45,
'..................ooox.....oooo....xooo.....ox..................':43,
'..................ooooo....oooo....xooo....xxx..................':31,
'..................ooooo....oooox...xooo....xxx.o................':23,#COMMENT OUT THIS
'..................ooooox...oooxx...xooo....xxxoo................':13,
'.............x....oooxxx...ooxxx...xoxo....xoooo....o...........':51,
'..................ox.......ox......xo...........................':26,
'..................ooo.....xxo......xo...........................':11,
'...........x......oxo.....ooo.....ooo...........................':33,
'...o.......o......ooo.....xoo....xooo...........................':42,
'...o.......o......ooo.....xoo...ooooo.....x.....................':40,
'...o.......o......ooo.....xoo...oxooo...o.x.....o...............':29,
'...o.......o......ooo.....xxox..oxoooo..o.x.....o...............':41,
'...o.......o......ooo.....xxox..oxxooo..oooo....o...............':44,
'...o.......o......ooo...o.xxox..ooxxoo..oooox...o...............':45,
'..................ooooo....oooo....xxoxx...xxo.......o..........':46,
'..................ooooo....oooo....xooxx...xoxx.....oo..........':13,
'.....o.......o....ooooo....oooo....xooxx...xoox.....oo..........':60,
'.....o.......o....ooooo....oooo....xooxx...xoox.....oo......xo..':62,
'.....o.......o....ooooo....oooo....xooxx...oxox...o.ox......xxx.':42,
'.....o.......o....ooooo....oooo....xooox..xxxooo..o.ox......xxx.':55,
'.....o.......o....ooooo....oooo....oooox..xoooox..ooox.x....xxx.':58,
'.....o.......o....ooooo....oooo....oooox.oooooox..xoox.x..x.xxx.':40,
'.....o.......o....ooooo....oooo...oooooxxxxoxxxx..xoox.x..x.xxx.':59,
'.....o.......o....ooooo....oooo...oooooxxoxoxxxxo.xoxx.x..xxxxx.':25,
'...................x.......xx......xo...........................':34,
'...................x.......xx.....oox.......x...................':20,
'...................xo......xx.....oxx......xx...................':37,
'...................xo.....xxx.....oxoo.....xx...................':18,
'..................ooo.....oox....xxxoo.....xx...................':29,
'..................ooox....ooxo...xxxoo.....xx...................':41,
'............x.....oxxx....xoxo...xoxoo...o.xx...................':25,
'............x.....oxxx..xxxxxo...ooxoo...o.xx...................':10,
'..........o.x.....ooxx..xxxxoo..xxxxoo...o.xx...................':5,
'.....o....o.o.....ooxxx.xxxxox..xxxxxo...o.xx...................':45,
'...................xo......xo.....oxox.....ooxx.....oo..........':42,
'...................xo.....ooo.....ooox....xxoxx.....oo..........':51,
'...................xo.....ooo.....ooox....xoxxx....ooo.....o....':17,
'.................x.xo.....xooo....oxoo....xoxox....ooo.....o....':38,
'.................x.xo.....xoooo...oxxox...xooox....ooo.....o....':50,
'.................x.xo....oooooo...oxxox...xxoox...xooo.....o....':18,
'.................xxxo....oxxooo..ooooox...oxoox...xooo.....o....':21,
'.................xxxxx...oxxoooo.oooooo...oxoox...xooo.....o....':24,
'.................xxxxx..xxxxoooo.ooooooo..oxooo...xooo.....o....':22,
'...................xo......oo.....oxoo....x.oo.......o..........':26,
'...................xo.....xoo.....xooo....xooo.......o..........':51,
'...................xo....oooo.....xxoo....xxoo.....x.o..........':18,
'..................xxo....oxoo....ooooo....xxoo.....x.o..........':29,
'..................xxo....oxxxx...oooxo....xooo.....xoo..........':41,
'..................xxo....oxxxx...oxoxo...xxooo.....ooo.....o....':50,
'..................xxo....oxoxx...oooxo...oxxoo..o.xooo.....o....':40,
'.x........x.......oxx.....oxxo.....xx......ox...................':21,
'.x........x.......xooo....xxxo....xxx......ox...................':37,
'.x........xx......xxoo....xxoo....xxxo.....ox...................':42,
'.x........xx......xxoo....xxxo....xoxx....oox.x.................':33,
'.x........xx......xxxo....xxxx...oooxxx...oox.x.................':3,
'.x.o......xo......xoxo....xoxx..xxxxxxx...oox.x.................':13,
'..........................xxx......xo...........................':20,
'....................o.....xxo......xx........x..................':44,
'....................o.....xxo......xxx......ox..................':34,
'....................o.....xxxx....oxxx......ox..................':46,
'....................o.....xxxx....oxxx......xoo....x............':43,
'....................o.....xxxx....xxxx....xoooo....x............':30,
'....................o.....xxxxo...xxxxx...xoooo....x............':21,
'....................oo....xxxoo...xxxox...xoxoo....x.x..........':52,
'...................xo......xxo....oxxo.....xxox......o..........':38,
'...................xo......xxo....oxxxx...oooox......o..........':52,
'...........................ox......xxx..........................':43,
'..................x........xx......oxx.....o....................':19,
'..................xo......xxx......oxx.....o....................':29,
'..................xo......xxxo....xxxx.....o....................':17,
'..........x......oxx......xxxo....xxxx.....o....................':20,
'..........xx.....ooxo.....xxxo....xxxx.....o....................':42,
'..........xx.....oxxo....xxxxo....oxxx....oo....................':33,
'..........xxx....oxxx....oxxxo...ooxxx....oo....................':44,
'...................x.......xx.....oox........x..................':37,
'...................x.......xx.....ooxo......xx..................':20,
'..................xxo......xx.....ooxo......xx..................':21,
'..................xxoo....xxo.....oxxo......xx..................':25,
'.................xxxoo...oxoo.....oxxo......xx..................':43,
'...................xo......xx.....oxxo.....xxx..................':53,
'...................xo......xx.....oxxo.....xxx..................':53,
'...................xo......xx.....oxxx.....xxxx......o..........':29,
'...................xo......xxo....oxxxx....xxox......o..........':42,
'...................xo......xxo....oxxxx...oooxx......x.......x..':30,
'............x......xx......xxoo...oxxox...oooxx......x.......x..':21,
'...................xo.....oooo....ooxxx....xoox......o..........':52,
'...................xo.....oooo....oooxx....xoxx.....oo......o...':51,
'...................xo.....oooo....oooxx....oxxx...oooo......o...':18,
'..................xxo.....oxooo...ooxox....ooxx...oooo......o...':13,
'............ox....xoo.....oxooo...ooxox....ooxx...oooo......o...':61,
'....................o.....xxxx....oxxx......xxo......x..........':43,
'....................o.....xxxx....oxxx.....oxoo.....xx..........':21,
'....................oo....xxxo....oxxxx....oxxo.....xx..........':30,
'....................oo....xxxoo...oxxxo....xxxo...x.xx..........':19,
'...................ooo....xxooo...xxxoo...xxxxo...x.xx..........':61,
'...................ooo.x..xxoox...xxxxo...xxxoo...x.xo.......o..':31,
'..................ooo.....ooxx....oxxo.....xx...................':21,
'..................oooo....ooxo....oxxx.....xx.x.................':42,
'..................oooo....oooo...xxxxx....oxx.x.................':51,
'.................xoooo....xooo...xxxxx....oox.x....o............':25,
'...........x.....xoxoo...ooxoo...xoxxx....oox.x....o............':45,
'...........x.....xxxoo...xoooo..xxoxoo....oooox....o............':12,
'...........xo....xxooo...xxxxxx.xxoxoo....oooox....o............':38,
'...........x......oxo....oooo......xo...........................':29,
'...........xo.....ooo....oooox.....xo...........................':21,
'...........xo.....ooox...oooox.....xoo..........................':45,
'...........xo.....ooox...ooooo.....xooo......x..................':13,
'...........xxx....ooox...ooooo.....oooo.....ox..................':34,
'...o.......oox...xxoxoo..ooooooo..xoooo.....ox..................':23,
'...oo......ooo...xxooo...xxooooo.xxooxoo.xxoooo...oooo.....oo...':10,
'...oo.....xooo..oooooo...oxoxooo.xoooxoo.xxoooo...oooo.....oo...':24,
'..ooo.....oooo..oxoooo..xxxoxooo.xoooxoo.xxoooo...oooo.....oo...':8,
'..ooo...x.oooo..xxoooo..xxooxooo.ooooxooooooooo...oooo.....oo...':58,
'..ooo...x.oooo..xxoooo..xxooxooo.ooooxooooooxoo...oxoo...oooo...':62,
'..........x.x......xxo.x..xxxooo..xxxoo...xxooo...xooo.....oxo..':4,
'....o.....x.o......xoo.x..xxooox..xxxxxx..xxoox...xoox.....oxo..':17,
'....ox....x.x....o.xoo.x..oxooox..xoxxxx..xxoox...xoox.....oxo..':11,
'....ox....xox....o.oooxx..oooxxx..xoxxxx..xxoox...xoox.....oxo..':6,
'....ooo...xoxx...o.oxxxx..oxoxxx..xoxxxx..xxoox...xoox.....oxo..':18,
'..........ooo....xoooo...xoxxox.xxxxxxxx..oxoox...xox........x..':41,
'..........ooo....xoooo...xooxox.xxoxxxxx.oxxoox...xxx.......xx..':55,
'..........ooo....xoooo...xoooox.xxoxxoxx.oxxxxxx..xxx..o....xx..':31,
'..........ooo....xoooo.x.xooooxoxxoxxxxo.oxxxxxo..xxx..o....xx..':15,
'..........ooo..o.xoooo.o.xooooxoxxoxxxxoxxxxxxxo..xxx..o....xx..':49,
'..x.......xxo..o.xxoxo.o.xxooxxoxxxoxxxoxxxxxxxo.oxxx..o....xx..':13,
'..x.......xxoo.o.xxooo.o.xxooxxoxxxoxxxoxxxxxxxo.xxxx..ox...xx..':3,
'..xo......xooo.o.xxxxxxo.xxooxxoxxxoxxxoxxxxxxxo.xxxx..ox...xx..':1}

evaluateCache2 = {
('....o......oo.....ooox...oooox.....xox.......x..................','x'):1.6168271237748202,
('..x.o.....ooo.....ooxx...oooox.....xox.......x..................','x'):0.9886815609163404,
('..x.o.....oooo....ooox...oooox.....xxx.....x.x..................','x'):2.1159190400954797,
('..x.ooo...oooo....ooox...oooox.....xxx.....x.x..................','x'):46.08584791418994,
('.oooooo...oxxo....oxox...ooxox.....xxx.....x.x..................','x'):-9.449519984593955,
('.oooooo...oxoo....ooox...ooxox...o.xxx..o..x.x..................','x'):-9.806405809132604,
('.oooooo...oxoo....xoox...xoxox..xo.oxx..o.ox.x..................','x'):-12.532198784316005,
('.oooooo...oxoo....xoox...xxoox..xxoxxx..ooox.x..................','x'):-10.993760111825255,
('.oooooo...oxoo....xoox..ooooox..xooxxx..xoox.x..x...............','x'):-11.232470683115285,
('.oooooo...oxoo..x.xoox..xxooox..xoxoox..xoooox..x...............','x'):-11.146376712375776,
('.oooooo...oxoo..x.xoox..xxooox..xoxoox..xoooox..x.o.x...........','x'):-6.700687208058753,
('.oooooo...oxoo..x.xoox..xxooox..xxxxoo..xxxoooo.xxo.x...........','x'):-40.476098563970865,
('.oooooo...oxoo..xxxoox..xxxoox..xxxooo..xxooooo.xoo.x...o.......','x'):-39.655832176744205,
('ooooooo..oxxoo..xxooox..xxxoox..xxxooo..xxooooo.xoo.x...o.......','x'):-28.240360912111406,
('ooooooo.xxxxoo..xxooox..xxxooo..xxxoooo.xxooooo.xoo.x...o.......','x'):-25.295928689244835,
('ooooooo.xxxxoo..xxooox..xxxooo..xxxoooo.xxooooo.xxo.x...ooo.....','x'):-26.51220996423453,
('ooooooo.xxxxoo..xxooox..xxxooo..xxxoooo.xxooooo.xxx.o...ooox.o..','x'):-23.944289722933615,
('ooooooo.xxxxoo..xxoxox..xxxxoo..xxxxooo.xxxxooo.xxxxo...oooooo..','x'):-25.015622000258862,
('ooooooooxxxxxxo.xxoxoo..xxxxoo..xxxxooo.xxxxooo.xxxxo...oooooo..','x'):-18.965213873734875,
('ooooooooxxxxxxooxxoxoo.oxxxxoo..xxxxooo.xxxxooo.xxxxo...oooooo..','x'):-32.4546598475152,
('....................XXX....OXXO....OXOO....OOO.....OOX....O.OX..','X'):5.729655694839196,
('....................O.....XXOO...XXXOXX.XXXOX.....XXOX....XOOO..','X'):-10.452880683127137,
('.....................X.....OXX.....XXXXX.OOXXO.....X.O.......O..','O'):-1.4747143211045586,
('...........................OOOX....OOX....XOXO....XXXO.....OX...','O'):1.9473743495056104,
('..........XXX.....XXOXO...XXXOO....XXOOX...XXOX.....XX......X...','O'):20.924893897025783,
('..........................OOX.....XOXX.....OOO..................','X'):3.381277591579566,
('...................XXX....OOXO.....OXO......OO.....OX...........','X'):-0.6789871945540138,
('...........................OOO....XXXXX...XXX......OX...........','O'):6.443105627257049,
('.............O.....X.OX....XXXO...XXXXXO...X.X.....XXO.....X.O..','O'):12.47844647770579,
('.....................X.....OXX....OXOX...OOOX.....OXOX.....O.O..','X'):2.0566120680426514,
('.............O..OX..OO..OXXOOO..OXOXOOO.OXOXXOX...XOOO.....OOO..','X'):8.394959872780895,
('.........................XXOOO..OOOOOO..XOXXOO....O.O......O....','X'):16.09008298389785,
('.....................X....OOXO...XOXXO...XOOXO....OX.O....X..O..','X'):-1.840297163116779,
('...................XXXX..OOXXXX..OOXXXX..OOXOOOO..XOO......XO...','X'):-0.7216385538899879,
('.....X.......X....XXOOO...XOXO..XOXOOX...XXOOX....XXXX....XXXX..','X'):-12.55697473648162,
('...................X.X....XXXOO...XXXOO...OOO.O...OOXO....O.O...','X'):8.617508933133422,
('..........................XXX....OOOXO...OOOX.....XXX.....X.O...','O'):-0.6596355805961476,
('....................XO....OXOOO...XOXOOO..XXXOOX..XXXO....OOO...','X'):0.6637735621278956,
('...........................OOOX....OOXX...XOXOXO..XXOOX...XOOXXX','O'):-53.05832463129573,
('...................OXXXX...OOXXX...OXOOX...XOO....XXO...........','O'):-3.602080637623131,
('.........................OXXX.....XXX...OOOOOO.....OOO....XOOO..','X'):-4.3366679216505135,
('....................O......OO.....XXOX.....XOO......O.......O...','X'):7.106817159765214,
('...................XX.....OOOO...XOXOO...OOX.O....X.............','X'):2.0929543654168556,
('....X.......XX.....XXOO..XXXOOO...XXOOX...OXOXXX..OOOX....OOO...','O'):9.996480692084544,
('.....................X.....OOOO....OXO.....OOX.......X..........','X'):4.871711076066291,
('.............O....OOOO.....OXXX...OOXXXX.O.OXO....OOOX.....OOO..','X'):13.370336532165746,
('...................XXX.....XXXX....XOXO...XXOOO....O.X....OX....','X'):-11.986099010084645,
('..........................OOOO....XOOO....XXXO.....X............','O'):-3.535416230753166,
('...........................OOO....XXXX....OXX.......X...........','O'):1.4204220395926417,
('.....................XX....OXXO....XXOO...XOXOO.....OO......OO..','O'):-2.400983993895035,
('......................X..OOOOOX..OOOOOX..XOOOXX...OOOX....XXXO..','O'):1.4100628273999114,
('..................X.XX..OXXXXXX.XXXXXXXO.XOXOOO....OOO....OOOO..','O'):9.543779940231092,
('...................OX......OOO.....OXO....XXXXX......X......X...','O'):4.777561661534828,
('.................XO.O..OXXXOO.O.XXOXOOOOXOOXXXO...OO.X....XXXXX.','O'):-23.764903333852395,
('..........O.......OOOOO...OOOOO...OOXOOXXXXXOXXX...XXX....OXXO..','X'):20.763689778618897,
('...........................OX.....XXXX....XXXXO...XOOO....XOO...','X'):-5.183539121280512,
('.....................XXX..OOOOXO...OXXX..OOOOOX.................','O'):-10.609752514524578,
('...................X......OXX.....OXXX....OXXOO...OX.O.......O..','O'):-2.3154804428076194,
('.....................X.....OXX.....XXX....XOOO.....OOO..........','X'):0.9525840771527505,
('..........................OOOO....XXXXX....XOO.....X.O.......O..','O'):-0.5574548136217037,
('..........................XXX.....XXXXXX.XXXXXX....XXX....XXX...','O'):-100,
('.........................OXXX...XOOXX...OOOOXO....X.OX....XXXXX.','O'):3.9699466721472176,
('...................XXX..OOOOOOO.OOXOOOO..XXOOXOO..OXXX....OOOO..','X'):2.675629700996637,
('......................X...XXXXX.O.OOOOXXXOOOXXXO..OOOX.....OXX..','X'):-18.45026011405,
('................O..OOO...O.OOOOXXXOOXXOX..XOXXOX..XXOO....XXXX..','X'):69.91322916111453,
('.....X.....XXX....XXXX...XXXXXXO...OXXOO...XOOOO..XXOO....OOOO..','O'):77.1989505864896,
('...........................OX.....OXX....OOOX......O............','X'):7.198551994117254,
('....................XX.....XXOX...XOOO..XXXOXOO...XXOO....XOOO..','O'):4.33090218105279,
('...................XXXO....XXXO....XXXOX..XO.XO...OX.X..........','X'):-5.5163104213751515,
('.................O..XX..XXOXXXXX.XOOOXX.XXXOOOOO..XXO.....XOOO..','X'):-19.948035934580176,
('....................OX.....OXX.....XOX....XXXX......OX.....O....','O'):6.2632051331578396,
('..................X.OX...XXXXXX.XXOXXXX..XOOXXX...OX.O....O..O..','O'):21.25561121217099,
('.............O.....XOXO....OXXX...OOXXX..OOOX.X.................','O'):-6.5971313934624405,
('...................XXX.....XXO.....XOXO...XOXOX...OOOX.....OX...','O'):12.535604359716663,
('.....................XX....OOXO...OOOO....XOOOO......X..........','X'):2.7743434894701133,
('...........X......OXXOO...XXXXO...XXOOXOXXXXXXXX..XXXO....X.OOO.','O'):2.800497385346373,
('............X......XXO....XOXO....OXOOX..OOOOOO...OXXO....OOOO..','O'):-5.960108460241846,
('.....................X.....OXXX....OOXO....OOX......XX.......X..','O'):-1.4187709868050555,
('.............X....OOXXOO..XOXXXO..OOXXXX.OOOXOXO...OOX.....OOO..','X'):5.673764611658466,
('...................XXX.....XOX.....XOO....XOOOO......X..........','O'):7.86158164105069,
('...................XXX.....XXX....OOXX....XOXO......X...........','O'):12.940791125552071,
('....................OX.....OOX.....XXO.....X.XO......X..........','X'):-6.787751810494969,
('...................XXX.....XXX....OXOOO....X.X.....XXX.....X....','O'):5.828023040010326,
('..XXX.....XXX.....XXXX....XOXOOO.XXXOOO..OO.OOXX..O.............','O'):0.3819563607299786,
('......................X....OOXX...XXXXX...XXOXX...XXO.......O...','O'):11.455249158216423,
('...................OOOO...OOOOO.XXXXOXO..OOOOOX.....OX..........','X'):9.6232119722655,
('.............X......XX....XXOOX..XXXXXXXXXXXOOO...XOXO....OOOO..','X'):-24.19023141782647,
('....................XXO....XXX...OXXOXX..XOXOXXX..XOOX....X.O...','O'):11.338850174800212,
('...........................OOO....XOOXX..XXOXXX...OXXX.....OX...','X'):-9.235946315333459,
('...........................OOOX...XXO.X...XXOXX...XXXO....XXOO..','O'):14.737129201584999,
('...X.......XXX.....OXXXX..OOOOXX..OOXXXX..OXXXXX..XX.O....X.....','O'):8.880726713938454,
('..................XOOOO.OOOOOOO..OXOXOOO...XOOO...XOO...........','X'):18.390896560861272,
('...................XO......OOOOO.XXXOOOOXXXXOOO...XXOX...XXXXXX.','O'):2.7446033331411885,
('...........................OX......OOOO.XXXXXOX...OOO......OXX..','O'):-3.938844023895679,
('....O......OOO.....OOOOO..XXXXOX..OXOOXX..OOOOOX....XX.....XXX..','X'):61.26952877091117,
('...................XXX....OXXO...OOOOOOO...OXOO....OXO......X...','X'):2.378402721331924,
('....................XX.....OXXO....OXOX....OO......OX...........','X'):-2.3549945639353775,
('....................OX.....OXO.....XXXOX..XO.X.O...O.X..........','X'):-2.1160151885237175,
('....................O....XXOOOOOOXXXXXO.XOXXXX....OOXX....OOXX..','O'):-5.37601118633139,
('...................OOO.....OOO....OOXXX..OOOXXX......X......XO..','X'):8.881591915266394,
('.....................X....XXXX.....XXX...OOOOOO......O.......O..','X'):2.4076267318152973,
('....................X.....OXXX..OOOOOOXO.OXXOX.X..OOXX....OOOX..','O'):-3.152328719374338,
('...................OOOOX.XXOOXXX.XXOOXO..OXOXOO...OXXX.....XXX..','O'):-8.543844398380932,
('...........XXX.....XXX.....XOX.....XOX...OOOOOO......O.......O..','X'):-4.300879570091529,
('.....................X.....OXX.....OXX.....OOO..................','X'):1.0299430755255898,
('...........................OX.....OXX....OOOX......XO......X....','X'):2.0556920478120304,
('...........................OOO....XXOOX...XXOOO...XO.X....O.X...','X'):-2.4359976189318084,
('..........................XXXO....OOOO....XOXX.....X......XXX...','X'):-12.846752671770535,
('.....................X.....OXX.....OXX.....XOOOO..XO.......O....','O'):-0.6525323959333816,
('...........................OX......OX....OOOOO....XXXO......X...','X'):6.915707655567419,
('............XO.....XXX..XXXXXXXX.XOXXO.X.OXOOOOX...XOO....OOXO..','O'):3.324273290780747,
('...........................OOO....XXOO....XOOXX...OXOX.....XXO..','O'):1.6380326320250487,
('.........................OOOOOX..OOXOXXXXXXXXXX...O.OO....O..O..','O'):-5.782303906916117,
('...........................OOO....XXOO.....OOO..................','X'):7.321461763091322,
('..........................XOOO....XXO.....XXO......OX........X..','O'):-1.3661551743935483,
('.........................OOOOO...OOXOX...OOOXX.....O.X....OOO...','X'):8.49251401468123,
('.....................X....XXXXX...XXOXO.XXXXXOO...XXOO....XXO...','O'):7.955155914927576,
('...................XXX.....XOX.....OOO....OOOOO....X.X..........','X'):-4.331212684355016,
('.............O.......OXO..OOOOXX..OOOOXX.OOOOXOX..OOOO....XXO...','X'):75.76320041409582,
('..........................XXXO....XXOXX.OOOOXXX...XXXX....XXX...','O'):10.104270404980053,
('..................OXX......OXX.OXOOOOOXOOXOXXXXX..XXOX...XXXXXX.','O'):6.169465831115566,
('..................O.X...XXOOXO..XOXOOO...XOXXOOO..O.XO....O..O..','X'):5.4035315069200385,
('...................XO....XXXXO..O.OOOXO.XOXXXXX...XX.O....XOOO..','O'):1.0165124810587238,
('.............X.......XX....OOXX..OOOXXX..XXXOXXX..XOOO.....XOO..','O'):12.127271522333805,
('..................XO.XXXOOOOOXXXXOXXXXXX..OOXOOO..OOOO......OO..','O'):-13.140806596882825,
('...................XXX.....XXX.....XOX....XXXX....OXXX..........','O'):19.84748505853395,
('....X......XX.....OXX.....OXXOOO..OOXXOO...XXOOO...X............','X'):0.3369453582340678,
('..........................OOX.....OOXXX...OXOX....OOXO....O.....','O'):-4.090866624130316,
('..................OXXX....XOXO...XOXOO...OXX.O.....OOO..........','X'):6.743145526446906,
('.....................X....XOOOO...XOOOOO..XOOX....XXX...........','O'):6.039061561032469,
('...........OX....OOOXXO....OXXOO..XOXXOOXXXXXXOX..XOXX......OX..','O'):-0.5648169673109471,
('..........................XXX.....XXXO...OOOO......O.......OX...','X'):4.345715903662328,
('.....................X.....OXXXX...XOXX...XOOXO...OOXX....XXXX..','O'):3.2606636700379146,
('...................XXX.....XXX.....XOX.......X.......X..........','O'):11.037796109711628,
('................O.X.....OOXXX.O.XOOXXXXXXXOOX.X...XXOX....XXXO..','X'):-15.44244197229696,
('..........................XXXXX...OOXX...OOOOO.....OXO....XO....','O'):0.1290422131546935,
('.........................X.OOO...OXOXOXX..OXOOX...XOXX.....OXX..','O'):-1.6366660128442148,
('..................OXXX....OXOOO...XXXXXX.XOO.O....OXOO....OX.O..','X'):-7.832836811919498,
('...........O.......OOO.XOOOXOOOO.OXOXXOO..OXXXX....XXX....XXXX..','X'):64.86914522411152,
('.....................X...O.OOOO..XOXXO..XXXOO.....XOOX....XOOO..','X'):2.150189324865285,
('..........................XOOO....XXO.....XXOO.....OO.......O...','X'):7.660762734636311,
('...................XXX.....XXX....OOOX.......X.......X..........','X'):100,
('....................O...OOOOOXOO.OOOXX.OOOOXOXXO..XXXX....OXX...','X'):8.977596527353697,
('........................OOOOOO...OOOOOO.XXOXXXOO..XOXX....XXXX..','X'):66.49070624209622,
('....................XXX....OXXXO...XXXOO...XXOXO....OX.....O.X..','X'):-15.16564274762121,
('...........................OOO....XXO.....XXOO....XOX.....O.OX..','X'):-0.2863697088511107,
('...................OX.....OOOXXX..XOOOXX...XOXOX...XXO.....XXX..','O'):3.0658614718921307,
('....................O.....XXO.....XXO.....OXOO.....XX...........','O'):0.02456180997567758,
('...........................OOO.....OO.X...XOOXOO..XXX.....XXXX..','O'):-12.989543065483039,
('....................XX.....OXX.....OOX.....O.OOO................','X'):2.9623467105632004,
('..........................XXXXX...OOOO....OXOXX...OO......OX....','X'):-9.233489038629363,
('...................XXX.....XXOO...XXOX..XXXOOXX...XXOX....XXX...','O'):17.24673530034123,
('...................XO......XO.....XXOOO....OXX.......X..........','O'):3.045615024833932,
('......................XO..XXXXO..OOOXOX..XOOOXX....OX........X..','X'):-9.347938213101088,
('..........................OOOO....OOO....OOOO.....XOX.....X..X..','X'):11.636996060023359,
('.....................X....XXXOX....XOX.X.OOOOOOO..OO.O......OO..','X'):-6.932568860383685,
('.............O.....X..OXOOOXXOXOXOXXXXO..OOOXOXX..OOOO.....OOO..','O'):-16.003159392918256,
('...................OOOO....OXXOX..OOXOXX..XOX.XX..XXX...........','O'):-10.241082851136316,
('....................OOO..OOOOOO..OOOOOO.XXXOXOX...XXXX....XXXO..','X'):16.99462283581685,
('..................OXX.....OXXX....OOOOOO.....O..................','X'):7.5499306171153,
('...................OXX...XXXXX..OOOOOX...OOO......O.............','X'):4.428167892834645,
('....................OOO...XXOOO..OXOOOO..X.O.X.......X..........','X'):6.705130657728806,
('..........X.......XXXXX..XXXXXXO.XXXOXXO.XOOOOOO..OXXX....O..X..','O'):82.65335063687358,
('....................X....OOOOO....XXOO....X.OO....XO......X.....','X'):8.681678543837924,
('...........................OX....X.OOOO..OXOOOX...OOOX.....OOO..','X'):3.6845737734966955,
('..................OOOOO..XXXXOXX.OXOXX...OOXXX.....XX.......X...','O'):-1.2330963005461952,
('....................OX.....OOX.....XOX....XXXOO....X.X..........','O'):8.13175550965738,
('....................XO.....OOOX....OOOO....OXOOO...X............','X'):0.19463179372752157,
('.....................X.....OXX.....XXX....XOOO..................','O'):5.204406174679818,
('...........................OX......OO.....XXXO....XO............','X'):-1.1140995855546174,
('..........................XXXXX.OXXXOOO.XOXXXO....OX......OOX...','O'):9.94455068488806,
('..................OOXXO.XXXXXXO.OXXOOXOO.OXXXXX....OXX....OOXX..','O'):-2.9595190418062733,
('..........................XOOO....XXOX....OXX......XO...........','O'):-1.8116857985040875,
('..........................XOOO.....XOOO..OOOXO....OOOX.....OXX..','X'):15.036980851624213,
('....................X......OXO.....XOX.......OOO................','X'):1.4985757531264,
('...................X.X....XXXX...XOXXX....OOOOO...OXXX..........','X'):-12.984949208591548,
('.....................XX....OOXX....XXOXX.....XO......X..........','X'):-9.234864854054612,
('...................XXX.....XXX.....XXX....OXXX.....O.X......O...','X'):-4.0538664197686085,
('....................XO.....OOO.....OXX...OOOX...................','X'):8.824020080023098,
('.................O..X.OOXO.XXOOO.OXOXXOOOOOXXOO...XOXO....XXXO..','O'):-14.994219298965104,
('..........................OOX.....OXXX....OOOO....O.............','X'):10.515889676540125,
('.................O.......XOOOO...XOOO...XXXOO.....XXO.....XXX...','O'):-10.039660963432652,
('..................O.O.X.XXOOXXXX.OOXOXXX.OOOOOOX..OOOO....XOO...','X'):4.076113720500369,
('...................OO.....XOOXX....OOX....XXXXXX..XXO.....XOOO..','O'):8.981763635369143,
('......................X...OOOXX...OOXX..XXXXXXX....XOX.....XXO..','O'):13.80319994686374,
('....................OO.....OOO.....OXXX...XXO.....XX.......X....','O'):0.6062038797245812,
('...........................OOO.....OX.....XXX.....XO............','X'):2.030386010045377,
('..................OOOOX...XOXOXO..XXOXXX..X..OOO................','O'):-9.19666437866492,
('.....................X...OOOXXO..OOXOX..XXOOOX....OOXX....OOX...','O'):3.1179604115687853,
('.....O......OO...OOOXOOX..OOOOXO...OOOOO...OOOOO....OX.....OX...','X'):25.168297030563547,
('.....................X....OOXXX...OXOXO..XXXOOOO..XXOO....OOO...','O'):-0.6519185266673724,
('...................XXX.....OXXO....OOXO....O.XX......X..........','O'):6.712090716466699,
('.....................XO...XXXO...OOXOX.....X.X.....X.X..........','O'):4.6623917765948475,
('.....................X...OOOXX..XOOOOX..XXOOXXXX...X.X....X.....','O'):8.08243254400566,
('...........................OOO...OOOOX.....OX.......OX..........','X'):14.020493790952901,
('...........................OX....OOOO......OXO.......X..........','X'):1.816267788556487,
('...........................OOO....XOO.....XXO.....X.O.......O...','X'):2.182109254867704,
('..........................XXX...O.XXXO..XOXXXOX...OXXO.....XXO..','X'):-9.005989445220548,
('....................OX...XXXXOOO..XXOOO...XXXOX...XXO.....OOOO..','X'):-9.370069749865543,
('...................XO.....OOX..O..OOOXOXXXOOXOX...OOOX.....OOO..','X'):1.988266348010618,
('..........................OOOOO...OXXOO...OXOOO...OOX.......OX..','X'):82.23789464912214,
('...................XOOO....XOO....XXOXO....XOOX...XOO......O....','X'):2.7677845296366557,
('...................OOOOX.XXXXXXX.OXOOXOO..XXXOOO..XXOX....XXXX..','O'):1.1755093571766901,
('...........................OOO....XOO......OX......OX...........','X'):7.8665099532269185,
('.....X......OX.....OOO...XXXXXOO.OOXOXOO.OOOXXXO..XXO.....X.O...','X'):3.496028884531917,
('..................OXXX.....OXX.....XOOO..OOXXO....XXX.......XO..','O'):-2.664783922841901,
('.................O.XO....OOXO.....OOOO...XXXOO....XXO.....XXX...','X'):12.52134207995018,
('.....................XX....OOXX....OXOOO...XOOO...XX.O....OX....','X'):-2.426329118015026,
('..........................XXX.....OOOO....XOX......X......XXX...','X'):-12.283969014862738,
('....................XX.....OXXO....OXOOO...OOOOX.....O......O...','X'):8.347885405119053,
('.....................X....XXXX....XXXX....XOXX......OX..........','O'):13.873294739652941,
('..................OXXX...OOOXXX...OXXXO...XXXO....X.XX......X...','O'):6.060245316633051,
('...................X.......XX......XOO....XOX.....XXXX....X.X...','O'):19.01298297288184,
('...................XX.....OOXOX....OXOX....OXXX.....XO..........','O'):3.6616761736100814,
('............O.......OOX....OOOX....OXOX....XXXX...XXO......OO...','O'):-0.30704112730808475,
('...........................OOOX..OOOOX...XOOXO....XXX...........','O'):0.1731701986388335,
('...................XXX...XXXXO..OXXOOOO..X.XOOO.....OO......O...','O'):4.2671841114563245,
('...........................OX......OO....OXXXXX...OXXX....XXX...','O'):1.7308668748941753,
('...........................OOO....OXXX...OOOX.....O.OX......XO..','X'):11.823645788142706,
('....................X......OXX.....OOXX....O.OX.................','O'):0.4697204514612573,
('....................OXX....OOX.....OXOO..XXX.X.......X..........','O'):10.569872700269162,
('..........................OOXX....OOXX...OOXOOO...OXXX....OXXX..','X'):10.302623418589583,
('....................X......OXO....OXOO....X.OO......O...........','X'):7.757144130935894,
('....................XX....OXXX....XXXOX...XXOOOO...OOO....OX.X..','O'):11.039975536137478,
('..........................OOOOX...XOOX.....OXXO....OO......OOX..','X'):7.268182773965453,
('...........................OX...OOOOOX..XOOOOO....OOO.....XXXX..','O'):-13.893173023815653,
('.............X.....OOOO...XXXX....XXXX....XXXX.......X..........','X'):-15.35908694871736,
('.........................OXXX.....OXO......XXO.....X.O.......O..','O'):-3.4367547393599494,
('...................OXX..OOOOOX...OOOXX...O.XXXX.....X...........','X'):-6.170181865465434,
('..........................XOOO....OXO....OXXXXX...XXXX....O.X...','O'):3.074151557272326,
('...........................OX......OX.....XXX.....XXX......OOO..','O'):7.60572096468892,
('..................XXX.....XXXX....XOXXX...XOOOOO...O.O..........','X'):-8.783647027970147,
('...........................OOOO...XXXOX....XOO.....XXX..........','O'):5.220654748231642,
('....................X......OXO...OOOOO.....XXO......XO......OX..','X'):10.6356096146235,
('.....................X.....OXX.....XOOO......X.......X..........','X'):-6.30400409365899,
('...................XX......XXO....OOOX.......OOO................','X'):0.678007674369144,
('...........................OOO...OOOOX....OOX......OOX......XO..','X'):12.41548533944297,
('.....................X...OOOOOO..XXXOO.....OOOO...OXXX.....X.O..','X'):2.6500447730903605,
('.....................X.....OXX.....OXX.....OOX.......X..........','O'):3.6782061618250848,
('....................OX....XOOOX...OOOOOX.XXXXXXX..O..X..........','X'):-7.105930027369035,
('....................O.....XXXX....XOOO...XXOX.....OXX.....XXX...','O'):7.528063068347541,
('...........................OOO....XOXX....OOX...................','X'):5.121845223450638,
('..........................OOX.....XOO.....XXOO.....X.......X....','X'):-2.582892798310782,
('...................XXXOO...XXXOO...XXXOO...XXX.O...X.X..........','O'):13.262496901180217,
('...........................OX......OX....OOOXO....OXX.....O.X...','X'):5.614174338341038,
('....................XO.....OOX.....OOOX...XXXO..................','O'):2.2072017500379073,
('...........................OOOO..OOOOXO.XXOOXX.....X.X....XXXX..','X'):5.322936296585806,
('...........................OOO....XXOO.....XOO......X...........','O'):1.8488607300227873,
('...................O.....XXOX....XXOOX....XOXXX...OXXX.....OXX..','X'):-14.63578492538826,
('............O.....XOOOX...OXOXX...OXOOX...O.OOX...O..O.......O..','O'):-3.962847940292933,
('..........................OOX.....XOXX.....OXXX....O.O.....O.O..','O'):-3.161342456553193,
('....................XXX...OOOOO...XOXX.....XOXO....OXX....O.OX..','X'):-1.1488490395294952,
('..........................XOOO...OOXO......XX.......OX......O...','O'):-7.397286879413253,
('...................OXXX....OOXO..O.OXO....OOOO....XOO......O....','X'):10.19523241903654,
('....................XX.....XXXO...XXXOO..OXXOOOO..X.............','O'):-0.1604790492546193,
('...................X.......XX....X.XXO...OXXXO.....XXO....XXX...','X'):-7.2889834955123325,
('...................XXO.....XXOO....XXXOX...XXOOO...XX...........','O'):10.198896248290342,
('...................XX......XXO.....XOOO..OOO.OX.................','X'):0.805913660960029,
('.....................X....OOXX....XOXXO..XXOOOOO..XOO.....XO....','X'):-6.943756826000502,
('.....................X.....OXX.....XXXXX.....X.......X..........','O'):12.743211657536666,
('..........................OOXX....OOXXXX..OOXXX...XOOX......XO..','O'):0.9417302830193505,
('....................OX.....OXO.....XXXXX...X.O......XX.......X..','O'):7.076099070015166,
('............O.......OO.....OOOO....OOOX....OOXXX....O.......O...','X'):12.561756468566424,
('.....................X.....OXX.....OXXXX.OOOXOOO...OOO......O...','X'):8.805911089717231,
('....................X......XXO....XOOO....XOXO....OO.......O....','O'):1.940013133906485,
('..........................XOOO...XOXO...XOOOOO....XXOX....XXX...','O'):-5.066317160737791,
('...................OOO.....OOO....XOOO....XOXXX....O.......OX...','X'):4.122810480865126,
('..........................OOOOO...XXOOX....OOXX....OOX.....O....','X'):0.8214537525440474,
('...........................OX....XXXO....OXOOO.....XO......X....','X'):0.379556152739815,
('...................OX......OXXX....XXXOO....XXX......X..........','O'):7.9389981872932305,
('.....X......OX......OX.....XOXO...XXXXXX..XO....................','O'):4.1342085701904985,
('...........................OOO...OXXXX....OOX......X......X.....','O'):-4.323427780194022,
('.....................X.....OXX.....XXX....XXXO.....XOO.......O..','O'):5.631385845856567,
('.....................XX....OXXO....XXO....XOOOO......X..........','O'):1.019574480414848,
('....................OX.....OOX.....OOOX....OXXXX...O.......O....','X'):1.6544062150662566,
('.....................XX....OOXX....OXXX....OOXO....OOX....OO.O..','X'):4.835219959274695,
('....................XX....XXXX....OOOX....OO......O.............','O'):2.0050675709585124,
('..........................OOX....XOOO.....OOXXX...OXXX..........','X'):-10.412713571782675,
('....................OOO...XXXO....XXXX.....OXX.....O.X.....O....','O'):0.4104260704984321,
('....................O....OOOO....OOOO...OOOOXXX....OXX......XO..','O'):-8.321033048220933,
('....................OX.....OXXX....OOXO..OOOXX.....O.X.....O....','X'):4.488129112463271,
('.....................XO...XXXXO...OOOOO...XOX.....XX......XXX...','X'):-4.8220120605514465,
('....................OX.....OOX.....XOX....XO.X.......X..........','X'):-8.221793488398147,
('....................OX.....OOX.....OOXX....OOXXX...XOX....X.....','X'):-3.2643694136954395,
('.....................XO....OXXXX..OOOXX...XOOXXX...XOX......O...','X'):-5.469424582483465,
('.....................X.....OXX.....OXXO....XOOX...XXO...........','O'):4.811331087758078,
('.....................X.....OXX.....OOXO....OXX......XX..........','O'):1.0160763128171155,
('...........................OX.....XXXO....XOO......O............','X'):-0.14621435542657235,
('...................XX....OOXOO....OXOO......XO..................','O'):-6.705175234734242,
('...........................OOO....XOOO....OXOO.....OO......OOX..','X'):15.563451023497612,
('.............X......XXO...XXOXX..OOOOXX....OOO.....OOO.......O..','X'):5.388613814904468,
('....................X......OXO.....OOO.....OOO..................','X'):8.876718338493497,
('....................XXXX...OXOXX...XXXOX...XXX.O....XX.......X..','O'):8.26047265404772,
('..........................XXX.....OOXO....XOXX.....X......XXX...','O'):9.876949270768366,
('.....................X.....OXX....XXXX.....O.X.......X..........','O'):9.714057352200218,
('...........................OX......OOO....XOX......X......XXX...','X'):-10.747772121273135,
('...................XX.....OXOOOO..OOOXXX...XXOOO...X............','X'):-2.143006773796492,
('....................O......OO.....XXOX.....OOX......OX..........','X'):0.9925468891443925,
('...........................OX......OXO....XXO.....XXX.....O.X...','O'):2.3866070845115357,
('....................OX.....OOX.....XOX...OOXXO....OX......O.....','X'):-0.16158326128019804,
('..........................XOOO....XOXX...OXOX.....XO............','X'):-0.43424951252174776,
('...................XXX...OOOOOO..OOOOXO...OO..X...XXX.....X.....','X'):0.6906299738276597,
('.....................X.....OXX.X..OXXX.X..XOXXOX...OOO.....OOX..','X'):-5.564391945687073,
('....................OX.....OOX.....XOX.......X.......X..........','X'):-7.904682584006688,
('............O......XOO.....XOXO...XXXXX....XXXO....XXX....X.....','O'):11.564374900883115,
('...................OOO.....XOXX...XOOX....X.OO....X.O...........','X'):1.6276918287859676,
('.........................XXXXO...XXOOO..XXXOOO....XX.O....XO....','O'):-1.3685541517902242,
('..................OOOX....OOOX....OOOOOO..OOOX.....OX.......OX..','X'):17.055651753511647,
('.....................X.....OXX.....OOOO....OXO.....X............','X'):2.8639785339862702,
('....................X......OXO.....OOOO....OX...................','X'):5.722672778010788,
('..........................OOOO...XXXOX...OOOO.....OOO......OX...','X'):9.613382477059995,
('...................OOO.....OOOOX...OXOXX..XOOXXX...O.X.....OX...','O'):-26.55789868831731,
('..........................OOXX....XOX.....XXXXX....O......OX....','O'):11.747436890031778,
('....................O......OO.....XXOX.....OOO..................','X'):4.397143008852488,
('...................XXX.....OXXX....OXXX...XOXOOO...OOX.....OX...','X'):-12.749134826057066,
('.....................X.....OXX....OOXX...OOOXX.....X.X......X...','X'):-5.405858379293754,
('....................OX.....OOX.....XOX.....XOX.......X..........','X'):-7.73694438571807,
('...................OOOO....OOXX....OOO.....OOO..................','X'):13.38010472956233,
('...................XXX....XOXX...XXXXX......OOO......X.......X..','O'):10.657906710293185,
('....................O....XXOO...OOOOOO...OXOOO....XXX.......X...','X'):8.282663547788609,
('....................XXX....XOOXO..XXXXOO..XOX..O..O.............','O'):5.962566740050151,
('....................OX.....OOX.....XXX.....X.X.......X..........','O'):11.23145241210039,
('...........................OX......OXO....XOX.....XOX......O....','X'):-2.3866070845115357,
('...........................OX.....OXX....OOXX......X.......X....','O'):-2.0507880226983795,
('...........................OX......OX.....XXXO....XOO......OX...','O'):0.9755645435819865,
('...................XXXO....XXOO....XOXX....OO.....OX............','X'):-6.352066498638928,
('...................XXX....OOXO.....OOO......OO..................','X'):7.805017284418222,
('...................O......OOX....OXOXX....XOXX....XOXX.....OXX..','X'):-3.6017938757392054,
('...........................OOO.....OOO....XXOXX...XXXX....O.X...','O'):3.071831615317451,
('....................OX.....OXX....OOXX...OXOXX....OOXX.....O.X..','X'):5.145375852548293,
('..........................OOOOO...XOXXX..OXOX.....OO......XO....','X'):9.086096426542879,
('.....................XX....OOXO....XXO...OOXOOOO...O......OOO...','X'):10.528600660024146,
('....................XO.....OOX.....OOXOO...OXOOO...X.X..........','O'):-2.636440798642637,
('...........................OX.....XXO.....XXOO.....X.......X....','O'):2.5612532994327037,
('....................O......OOX....OOXOX..OOXOOXX..XOOO......O...','O'):-10.447847177038474,
('....................O.....XXO.....XXO......OXO.......O.......O..','X'):0.7072770528219793,
('...........................OX....OOOOX.....OOX......OX..........','X'):2.8495328826006414,
('...........................OOO.....OX.....XXX.....XXX...........','O'):10.287781972414313,
('......................O..XXXXOO...XOOXO.OOOOOO....XX.O.....X....','X'):5.552633333356505,
('....................OOO...XXXOX....XXXX...XXXXX.....OX.....OX...','O'):10.51112308023084,
('...........................OX.....OXX...XXXXX.....OO.......O....','O'):1.6544739843021803,
('...................OOOOO...XOXXX..XXXO...OOOOO.....O.......O....','O'):-13.019621135735706,
('....................OX.....OOX.....OXO.....XOXO...XOXX....OO....','X'):-3.1698678009815295,
('....................X......OXO.....XOO....XO.O..................','X'):4.382504806178445,
('........................O.XOOO..XOXOOO...XXOOO....XOOO....OXX...','O'):-15.144328696057434,
('...................XXX...XXXXO.....OOOO.....OOOO..XXO.......O...','X'):-6.566379683783227,
('..................OOOOOO...OXOO....OXOXX..XOXX.....OXX..........','X'):7.414924633265869,
('..........................XOOO....XXO......OX......OX...........','O'):-2.982532556909614,
('...........................OOO....OXXX...OOOO.......X......XXX..','O'):-10.051125390734748,
('....................X......OXO.....OOX.....OOOX.................','O'):-3.625656882516837,
('...........................OOO....XOOOO....OXOX...OOOX.....OX...','X'):8.744240467054729,
('..................OXX......OXO.....XOO.......O..................','X'):8.840925691060056,
('...........O......XOO......XXO....XXXOO..OXXXOO...XXX.....OX....','O'):-15.922060448191393,
('.........................OXXX....OOXX....OOOXXX....XOO....XOOO..','O'):2.022665225246557,
('..........................XOOO....XXXX....OOX......OX...........','O'):-1.1867989103358718,
('...........................OOO....XOOX...XXOX.....OOX...........','X'):-2.1887406172113955,
('...................XXO.....XOO.....XOO...OOX.O.....X............','X'):1.4764993552036414,
('...................OX.....XXOOOO..XXXOOO...XOOOO...OX...........','O'):-2.520269804683153,
('...........................OX......OX.....XOXO.....XX.......X...','O'):1.5080571570005916,
('...........................OX......OOO....XXO.....XO.......OX...','X'):6.699238434184777,
('....................XXO....OXOO....OOXO....OOOOO................','X'):18.206807966267743,
('...........................OOO....XXX.....XXX.....XO............','O'):-2.8378247192996198,
('.....................X....XXXXO....XXXXX...OXXXX....XO......O...','O'):4.820964252460926,
('...................XXO.....XOOOO..OOOOO....XX......XX......X....','X'):-1.1545700982467584,
('..................O.......XOX......OOO...OOOOO....XXX......XXX..','X'):4.63891280320649,
('..........................XXX....OOOO......OOO..................','X'):6.074487302215908,
('..........................XOOO....XOO.....OOX......OX.......XO..','X'):4.074311966319616,
('..................XXXX....XXOOO....OXO...OOXOX....XO.X....X.O...','X'):0.9350686422441801,
('.........................OXXXXX...OXOXO.XXXOX.....OOO.....XO....','O'):1.6841508462390677,
('.....................X.....OXX.....OXX.....OXO......O........O..','X'):0.5905858725023861,
('..................OXXX....OOXX....OXXXX....X.O..................','O'):7.942349371601919,
('.....................X.....OXX.....OXX.....OOOO....X.X....XXXX..','O'):-4.031796096933973,
('....................OOO...XXOOXX...XOXX....XOXO...XXXO.....XO...','O'):3.128214858650029,
('....................XX.....OXX.....OOXO....O..X.................','O'):-5.448834372910656,
('..................OXX.....XXXO.....XOO.......O..................','O'):-5.35615111092066,
('....................OX.....OOX....OOOX....XXOXX....X.X.......X..','O'):7.203285761791946,
('...........................OXX.....OXO...OOOO.....XO............','X'):7.770525787743732,
('...........................OOO....XOXX....OOX......XOX....X.O...','O'):-4.534137625196248,
('...........................OXX...OOOOO...OOOO.....XO......XO....','X'):15.080812689983869,
('....................XX.....OXX....OOOXO...XXXXX.................','O'):6.696684528706204,
('....................OX...XXXOX...OXOOX....OX.X.....OXX.....XO...','X'):-7.820971849378192,
('.....................X.....OXX.....OOX.O..XOXXO...XX.O....XXX...','O'):1.3281689017146474,
('..................XXXXXO..OXOXO...OOXOXO....XXXX................','O'):1.2890981148361305,
('.............X....OOOX.....OOX.....OOXO....OXOOO...XXX..........','X'):0.031924861081101055,
('..........................XXXXX..OOXOO....OOOOO...OOXO....O.OX..','X'):7.14600210573186,
('...................XXXO...XXXXO..XXXOXO....XXOX....XOX.....O....','O'):13.38783402856625,
('...........................OOO....XXOO.....OOO....XXX...........','O'):1.6734278235981919,
('...................XXX....OOXXX...XOXXXX...O.OO....O.O.....O.O..','O'):-1.3748645997476827,
('.....................X....XXXX....XXOOO...XXOO....XXO......X....','X'):-8.022797812192165,
('..........................XXX.....OXOO...OOOXO.....XXX.....XX...','O'):-0.4536153083913406,
('....................XXX....OXOX....OXOOO...OXXX....X............','O'):6.067502324093106,
('....................X......XX.....XXX......OXO......OO......XO..','O'):5.44507176577822,
('...................XXO....XXXXO..XXXXOO...OXOOOO....XO......X...','O'):-0.6958406257420376,
('.....................X.....OXX.....OXX.....OXO.....XXO..........','O'):0.9981912886996569,
('...........................OOO..OOOOO....OXOOOO...XXX......XXX..','X'):14.428338114819072,
('..................OXX......OXO.....OOX.....O.OX.................','X'):2.5493585213990975,
('...........................OOO....XXOX....XOO.....O.O...........','X'):7.98646394865347,
('...........................OX.....OOOOOOXXOXX.....OXX.....XO....','X'):1.8095678228671823,
('...................XO.....OOX.....OOOX....OOOX......XX..........','O'):1.4191911973090023,
('..........................OOX.....OXO...XXOXXXX...OX......XOOO..','O'):-0.5145580248103336,
('..........................XXXXXO..XXXXO...XOXOX....OOO.....OOO..','X'):-13.700491431339962,
('.....................X....XXXXXX..OOOX...OOOXX....OOOX....XXX...','O'):6.626256653040602,
('.................XXXXXX..OOOOX...OOXXX...OOXXXX......X..........','O'):11.93441717444581,
('.....................X.....OOOX....OXXXX...O.X.....O.X..........','X'):-3.6999100577778767,
('..........................XOOO....OXOO...OOOXOOO..OOXX....OOX...','X'):17.68633944427787,
('....................X......OXO....OOXO...OOOXO....X.X...........','O'):-2.4871308241335095,
('...........................OX......OX....OOOX......X........X...','X'):0.31629888651472843,
('.....................X.....OXX.....XOOO...XXXO......X...........','O'):7.685788103264797,
('...........................OOO....XXOOO....XX.....OXO......X....','X'):6.388453122700979,
('...................OOO.....XXXXX..XOOOOO...OOOOO................','O'):-7.009877151975105,
('....................X......XX....OXXX....OXXX.....XX......XOOO..','O'):7.610011156525588,
('..................OXX......XXO....OXOO....OXXXX...OXOO..........','O'):-2.3914987608109466,
('...........................OOO....OXOO...OOOOOX....OOO....XXXX..','X'):73.58779299072722,
('...........................OX......OX...XXXXX......X........X...','O'):10.467077223260953,
('....................X.X....XXX....XXXOOX..XXOOOO...XXO....OXX...','O'):21.23842429810303,
('...........................OX.....XXXXO....XXXOO....XX.....OXO..','O'):-2.5409732911877314

}
#theoryDct = {} #COMMENT OUT BEFORE FINAL SUBMISSION
evaluateCache2 = {}

evaluateCache = evaluateCache2
orderCache = {}
verbose = False
dotSet = {}
moveCache = {}
status = {"abCache":0}
abCache = {}
nmCache = {}
hl= 13
board = ""
defaultToken = "."
moves = []
for e in s:
    if e.upper() == "V":
        verbose = True
        continue
    if "HL" in e:
        hl = int(e[2:])
    if "." in e or (('X' in e.upper() or 'O' in e.upper()) and len(e) > 3):
        board = e.upper()
    elif e.upper() in ["X","O"]:    
        defaultToken = e.upper()
    elif len(e) <= 2 and e.isnumeric():
        moves.append(int(e))
    else:
        condensePath(e)

    
tokens = {"X", "O"}

if board == "":
    board = ('.'*27 + "ox......xo" + '.'*27).upper()
if defaultToken == ".":
    defaultToken = turn(board)

opToken = tokens - {defaultToken}
opToken = "".join(opToken)
length = 64
side = int(length**0.5)
    

if __name__ == "__main__": main()


            # Note: It is not required for your Strategy class to have a "legal_moves" method,
            # but you must determine legal moves yourself. The server will NOT accept invalid moves.




# Dev Kodre, Pd. 4, 2024