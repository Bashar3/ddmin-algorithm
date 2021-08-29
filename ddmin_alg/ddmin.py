import itertools as iters
import argparse

n = 2
checkNValues = []

parser = argparse.ArgumentParser(description="`\n Usage python ddmin.py -s <sequence> -f <fail_input>")
parser.add_argument("-s", type=list, dest="sequence", help="ints or chars sequence ")
parser.add_argument("-f", dest="fail", help="The expected fail input")
parsed_args = parser.parse_args()


def main():
    try:
        s = parsed_args.sequence
        f = parsed_args.fail
        ddmin(s, f)
    except Exception:
        print(parser.description)
        exit(0)


def ddmin(sequence, fail):
    if len(sequence) == 1:
        return sequence
    else:
        print(Test(sequence, fail))


# chunkIt()
# Takes a sequence as list and the failing input and runs the core of the algorithm
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

    if len(checkNValues) >= 4 and checkNValues[-1] == 2 and checkNValues[-2] == 2:
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


# Chuncks the sequence into small sublists of the same length
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


# Gives combinations of the cuncked lists of lists the sublists.
# And deletes chunck 1..len(seq) and cmbine them
def removeChunckAndMergeRest(a_list):
    removedChunck = []
    list_of_tuples_combinations = list(iters.combinations(a_list, len(a_list) - 1))
    list_of_lists_combinations = [list(elem) for elem in list_of_tuples_combinations]

    for elem in list_of_lists_combinations:
        joinSublists = list(iters.chain.from_iterable(elem))
        removedChunck.append(joinSublists)

    return removedChunck


# Counts the duplicates of each sublist for a given number
def countDuplicates(sequence, fail):
    a = list(map(lambda x: x.count(fail), sequence))
    return a


# Flattens a list
def toList(alist):
    flat_list = [item for sublist in alist for item in sublist]
    return flat_list


if __name__ == '__main__':
    main()
