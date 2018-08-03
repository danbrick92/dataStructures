masterlist1 = list()

def split(original):
    size = len(original)
    list1 = original[0:size/2]
    list2 = original[size/2:size]
    return list1,list2

def sort(original):
    sorted = list()
    val1 = original[0]
    val2 = original[1]
    if val1 < val2:
        sorted.append(val1)
        sorted.append(val2)
    else:
        sorted.append(val2)
        sorted.append(val1)
    return sorted

def divideAndConquer(original):
    if len(original) <= 2:
        new = sort(original)
        masterlist1.append(new)
    else:
        list1, list2 = split(original)
        list1 = divideAndConquer(list1)
        list2 = divideAndConquer(list2)

def merge():
    sizeOfMaster = len(masterlist1)
    if len(sizeOfMaster) == 2:
        masterlist1 = sortList(masterlist1)
        return masterlist1
    else:
        size = len(sizeOfMaster)
        list1 = masterlist1[0:size/2]
        list2 = masterlist1[size/2:size]
        list1 = sortList(list1)
        list2 = sortList(list2)


def mergeSort(unsorted):
    divideAndConquer(unsorted)
    sorted = merge(masterlist1)
    return sorted

unsortedList = list()
unsortedList.append(6)
unsortedList.append(8)
unsortedList.append(5)
unsortedList.append(1)
unsortedList.append(3)
unsortedList.append(4)
unsortedList.append(7)
unsortedList.append(2)
sortedList = mergeSort(unsortedList)
print sortedList