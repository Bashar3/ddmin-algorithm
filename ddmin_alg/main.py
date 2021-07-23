import itertools
import math
import itertools as iters
from collections import Counter

n = 2
checkNValues = []


def ddmin(sequence, fail):
    if len(sequence) == 1:
        return sequence
    else:
        checkInputC(sequence, fail)


def checkInputC(sequence, fail):
    if fail.isnumeric():
        ddMinNumbersTest(sequence, fail)
    else:
        exit()
        # ddMinChars(c, n)


def ddMinNumbersTest(sequence, fail):
    # n=2
    # [a,b,c,v,v,c,b,a]
    chunckPlace = None
    global n

    newSplitList = chunkIt(sequence, n)
    countRepeated = countDuplicates(newSplitList, fail)

    for i in range(len(countRepeated)):
        if 0 <= countRepeated[i] <= 1:
            n = min(2 * n, len(sequence))
            # SplitList = chunkIt(sequence, n)
            # a = removeChunck(SplitList, bigchunck)
            # l = toList(a)
            ddMinNumbersTest(sequence, fail)

    else:
        n = max(n - 1, 2)


# chunkIt()

def Test(sequence, fail):
    global n
    global checkNValues

    boolList = []
    slicedList = chunkIt(sequence, n)
    removedChunckAndMergedList = removeChunckAndMergeRest(slicedList)
    removedChunckRevesed = removedChunckAndMergedList[:: -1]
    alist = countDuplicates(removedChunckRevesed, fail)
    checkNValues.append(n)
    print("n = ", n)

    for i in range(len(removedChunckRevesed)):
        if not 0 <= alist[i] <= 1:
            boolList.append(False)
            print(removedChunckRevesed[i], "==> FAIL")

        else:
            boolList.append(True)
            print(removedChunckRevesed[i], "==> PASS")

    if len(checkNValues) >= 3 and checkNValues[-1] == 2 and checkNValues[-2]==2:
        print("Can't split anymore n =", n)
        print(removedChunckRevesed)
        exit()

    if n == 8 and all(boolList):
        print(removedChunckRevesed)
        print("Can't split anymore n =", n)

        exit()

    if all(boolList):
        n = min(2 * n, len(sequence))
        Test(sequence, fail)

    else:
        n = max(n - 1, 2)
        for i in range(len(slicedList)):
            if not boolList[i]:
                Test(removedChunckRevesed[i], fail)




def chunkIt(seq, num):
    if num == 0:
        return seq
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out


def removeChunckAndMergeRest(a_list):
    removedChunck = []
    list_of_tuples_combinations = list(iters.combinations(a_list, len(a_list)-1))
    list_of_lists_combinations = [list(elem) for elem in list_of_tuples_combinations]

    for elem in list_of_lists_combinations:
        at = list(iters.chain.from_iterable(elem))
        removedChunck.append(at)

    return removedChunck


def countDuplicates(sequence, fail):
    a = list(map(lambda x: x.count(fail), sequence))
    return a


def toList(alist):
    flat_list = [item for sublist in alist for item in sublist]
    return flat_list


#print(removeChunck(chunkIt([1, 2, 3, 4, 5, 6, 7, 8], 4), 2))
h = [[1, 2, 3, 4] , [5, 6, 7, 8]]
an = [[1, 2],[3, 4], [5, 6], [7, 8]]
dup = [[4, 3],[4, 3], [4, 4]]
asd = [1,2,3,2,2,2,2,2]
#print(removeChunck(an))
# print(ddMinNumbersTest([1, 2, 3, 4, 5, 6, 7, 8], 2))
at = list(map(lambda x: x.count(2), an))
#print(removeChunckAndMergeRest(h))
#print(countDuplicates(dup, 4))
print(asd.count(2))
#print(list(iters.chain.from_iterable(an)))
print(Test([1,2,3,4,4,3,2,1], 4))
# print(2 not in [1, 2, 3, 4])
# print(all(iter([True, False, True])))
