import sys
sys.setrecursionlimit(100000)
CACHE = {}
def change(n, coinLst):
    if len(coinLst) == 1 or n == 0: 
        return 1

    if n < coinLst[0]: return change(n,coinLst[1:])
    if n == coinLst[0]: return change(n-coinLst[0],coinLst) + change(n,coinLst[1:])
    key = (n,*coinLst)
    if key not in CACHE:
        CACHE[key] = change(n-coinLst[0],coinLst) + change(n,coinLst[1:])
    return CACHE[key]
    
    #if n >= coinLst[0]:
        #return 1 + change(n-coinLst[0],coinLst) + change(n,coinLst[1:])
    #if n > 0:
        #return 1 + change(n,coinLst[1:])
    #return x

x = change(10000, [100,50,25,10,5,1])
print(x)