count = 0

def SortAndCount(A, size):
    if size==1:
        return A
    else:
        left = A[0:size/2]
        right = A[size/2:size]
        B = SortAndCount(left, len(left)) # my problem had to do with assuming the size of both arrays were the same. they aren't
        C = SortAndCount(right, len(right))
        D = SortAndCount_split_inversion(B,C)
    return D

def SortAndCount_split_inversion(B,C):
    global count
    D = list()
    i = j = 0 # counter for B
    k = 0
    for k in range(len(B) + len(C) + 1):
        if B[i] < C[j]:
            D.append(B[i])
            i+=1
            if i == len(B) and j != len(C):
                while j != len(C):
                    D.append(C[j])
                    j += 1
                break
        else:
            D.append(C[j])
            count += (len(B)-i)
            j += 1
            if j == len(C) and i != len(B):
                while i != len(B):
                    D.append(B[i])
                    i += 1
                break
    return D

def getUnsortedArray():
    file = '100k.txt'
    with open(file) as unsortedNumbers:
        content = unsortedNumbers.read()
    content = content.splitlines()
    trueList = list()
    for line in content:
        number = int(line)
        trueList.append(number)
    return trueList

unsorted = getUnsortedArray()
#unsorted = [1,3,5,2,4,6]
SortAndCount(unsorted,len(unsorted))
print count