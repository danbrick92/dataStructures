comparisons = 0

def getUnsortedArray():
    file = 'quicksort.txt'
    with open(file) as unsortedNumbers:
        content = unsortedNumbers.read()
    content = content.splitlines()
    trueList = list()
    for line in content:
        number = int(line)
        trueList.append(number)
    return trueList

def choosePivot(style,theArray,start,finish):
    if style == "first":
        pivot = start
    elif style == 'last':
        pivot = finish
    elif style == 'mid3':
        firstVal = theArray[start]
        lastVal = theArray[finish]
        size = (finish+1)-start
        if size%2 == 0:
            midVal = theArray[(finish + start)/2 ]
        else:
            midVal = theArray[(finish + start) / 2]
        unordered = [firstVal, lastVal, midVal]
        unordered.sort()
        if unordered[1] == firstVal:
            pivot = start
        elif unordered[1] == midVal:
            if size% 2 == 0:
                pivot = (finish + start)/2
            else:
                pivot = (finish + start)/2
        else:
            pivot = finish
    return pivot

def swapIndex(pivotIndex,unsorted,start):
    #print "Swapping " + str(pivotIndex) + " index with first element"
    pivotValue = unsorted[pivotIndex]
    firstValue = unsorted[start]
    unsorted[start] = pivotValue
    unsorted[pivotIndex] = firstValue
    return unsorted

def partition(unsorted,start,finish):
    pivotValue = unsorted[start]
    i = start+ 1
    for j in range(start + 1,finish+1):
        iVal = unsorted[i]
        jVal = unsorted[j]
        if jVal < pivotValue:
            unsorted[j]= iVal
            unsorted[i]= jVal
            i+=1
    i -= 1
    pseudoValue = unsorted[i]
    unsorted[i] = pivotValue
    unsorted[start] = pseudoValue
    return unsorted, i

def QuickSort(unsorted,start=-100,finish=-100):
    global comparisons
    if start == -100:
        start = 0
    if finish == -100:
        finish = len(unsorted) - 1
    if finish-start <= 0:
        return unsorted
    comparisons += len(unsorted[start:finish])
    method = 'mid3'
    p = choosePivot(method,unsorted,start,finish)
    if method == 'last' or method == 'mid3':
        unsorted = swapIndex(p,unsorted,start)
    partitioned, i = partition(unsorted,start,finish)
    unsorted= QuickSort(unsorted,start,i-1)
    unsorted = QuickSort(unsorted, i+1 ,finish)
    return unsorted

unsorted = getUnsortedArray()
sorted = QuickSort(unsorted)
print sorted
print comparisons