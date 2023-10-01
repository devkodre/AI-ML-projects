import sys; args = sys.argv[1:]
from time import perf_counter



def main():

 
    #args['Ints4A.txt', 'Ints4B.txt', 'Ints4C.txt']
    f1, f2, f3 = 'Ints4A.txt', 'Ints4B.txt', 'Ints4C.txt'
    s = perf_counter()
    #with open(f1) as f:
    with open(args[0]) as f:
        f1_list = []
        f1_unique = []
        f1_set = set()
        f1_heap = []
        f1_occurances = {}
        for line in f:
            n = int(line.strip())
            f1_list.append(n)
            if n not in f1_set:
                f1_unique.append(n)
                add(f1_heap, n)
                f1_occurances[n] = 1
            else:
                f1_occurances[n] +=1
            f1_set.add(n)
                

    #with open(f2) as f:        
    with open(args[1]) as f:
        f2_list = []
        f2_unique = []
        f2_set = set()
        f2_heap = []
        f2_doubleCheck = set()
        f2_occurances = {}
        for line in f:
            n = int(line.strip())
            f2_list.append(n)
            if n in f2_set:
                f2_occurances[n] +=1
            if n not in f2_set:
                f2_unique.append(n)
                f2_occurances[n] =1
            elif n not in f2_doubleCheck:
                maxAdd(f2_heap, n)
                f2_doubleCheck.add(n)
            f2_set.add(n)

    #with open(f3) as f:    
    with open(args[2]) as f:
        f3_list = [int(line.strip()) for line in f]


    print("#0: Read in files: {0:.3g}s".format(perf_counter()-s))

    challenge1(f1_set,f2_set)
    challenge2(f1_unique)
    challenge3(f1_occurances, f2_occurances, f3_list)
    challenge4(f1_heap)
    challenge5(f2_heap)
    challenge6(f1_list)

    print("Total Time: {0:.3g}s".format(perf_counter()-s))


def challenge1(s1,s2):
    start = perf_counter()
    sum = len(s1.intersection(s2))
    print(f"#1: {sum};", end='')
    print("{0:.3g}s".format(perf_counter()-start))

def challenge2(unique):
    start = perf_counter()
    sums = set()
    for i in range(99, len(set(unique)), 100):
        sums.add(int(unique[i]))
    print(f"#2: {sum(sums)};", end='')
    print("{0:.3g}s".format(perf_counter()-start))

def challenge3(d1,d2,l3):
    start = perf_counter()
    sum = 0
    for n in l3:
        if n in d1: 
            sum += d1[n]
        if n in d2:
            sum += d2[n]
    print(f"#3: {sum};", end='')
    print("{0:.3g}s".format(perf_counter()-start))

def challenge4(heap):
    start = perf_counter()
    h = [remove(heap) for n in range(10)]
    print(f"#4: {h};", end='')
    print(f"{(perf_counter()-start):.3g}s")

def challenge5(heap):
    start = perf_counter()
    h = [maxRemove(heap) for n in range(10)]
    print(f"#5: {h};", end='')
    print("{0:.3g}s".format(perf_counter()-start))

def challenge6(l1):
    start = perf_counter()
    min_sum = 0
    seen = set()
    min_heap = []
    for n in l1:
        if n not in seen:
            add(min_heap, n)
        if n % 53 == 0:
            min_sum += remove(min_heap)
        seen.add(n)

    print(f"#6: {min_sum};", end='')
    print("{0:1.3g}s".format(perf_counter()-start))
            
#min heap pq

def heapDown(heap, k, lastIndex):
    l = 2*k
    r = 2*k + 1
    min = k
    if 1 > lastIndex and r > lastIndex:
        return
    if l > lastIndex:
        return
    if heap[l] - heap[min] < 0:
        min = l
    if r < lastIndex and heap[r] - heap[min] < 0:
        min = r
    if heap[k] - heap[min] > 0:
        swap(heap, k, min)
        heapDown(heap, min, lastIndex)

def swap(heap, a, b):
    heap[a], heap[b] = heap[b], heap[a]

def heapUp(heap, k):
    if k/2 == 0:
        return
    if k>= 2 and heap[k//2] - heap[k] > 0:
        swap(heap, k, k//2)
        heapUp(heap, k//2)

def add(heap, e):
    heap.append(e)
    heapUp(heap, len(heap)-1)

def remove(heap):
    swap(heap, 1, len(heap)-1)
    e = heap[-1]
    del heap[-1]
    heapDown(heap,1,len(heap)-1)
    return e

def peek(heap):
    if heap:
        return heap[1]
    return

#max heap pq

def maxHeapDown(heap, k, lastIndex):
    l = 2*k
    r = 2*k + 1
    max = k
    if 1 > lastIndex and r > lastIndex:
        return
    if l > lastIndex:
        return
    if heap[l] - heap[max] > 0:
        max = l
    if r < lastIndex and heap[r] - heap[max] > 0:
        max = r
    if heap[k] - heap[max] < 0:
        swap(heap, k, max)
        maxHeapDown(heap, max, lastIndex)

def maxHeapUp(heap, k):
    if k/2 == 0:
        return
    if k>= 2 and heap[k//2] - heap[k] < 0:
        swap(heap, k, k//2)
        maxHeapUp(heap, k//2)

def maxAdd(heap, e):
    heap.append(e)
    maxHeapUp(heap, len(heap)-1)

def maxRemove(heap):
    swap(heap, 1, len(heap)-1)
    e = heap[-1]
    del heap[-1]
    maxHeapDown(heap,1,len(heap)-1)
    return e


if __name__=="__main__": main()


 # Dev Kodre Pd:4 2024  