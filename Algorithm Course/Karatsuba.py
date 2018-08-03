class KaratItem:
    value = ""
    zeros = 0

def karatsuba(x,y):
    size = len(x)
    listx = list()
    listy = list()
    i = 0
    # Split to nuclear level
    while i < size:
        val1 = KaratItem()
        val1.value = x[i:i+2]
        val1.zeros = (size-(i+2))
        val2 = KaratItem()
        val2.value = y[i:i + 2]
        val2.zeros = (size-(i+2))
        j = 0
        for j in range(val1.zeros):
            val1.value = str(val1.value) + "0"
            val2.value = str(val2.value) + "0"

        listx.append(val1)
        listy.append(val2)
        i+=2
    i = 0
    listFinal = list()
    # Multiply
    for i in range(len(listx)):
        j = 0
        preprod = str(int(listx[i].value) * int(listy[i].value))
        listFinal.append(preprod)

    i = 0
    while i <= size-1:
        xprod = int(listx[i].value) + int(listx[i+1].value)
        yprod = int(listy[i].value) + int(listy[i+1].value)
        listFinal.append(xprod * yprod)
        i+=4
    print listFinal



def splitFully(number):
    sufficient = False
    while (sufficient == False):
        if (smallEnough(number) == True):
            sufficient = True
            return number
        else:
            half1, half2 = split(number)
            half1 = splitFully(half1)
            half2 = splitFully(half2)
            sufficient = True
            list1 = list()
            list1.append(half1)
            list1.append(half2)
            return list1

def smallEnough(number):
    if len(number) == 2:
        return True
    else:
        return False

def split(number):
    size = len(number)
    firstHalf = number[0:size/2]
    secondHalf = number[size/2:size]
    return firstHalf,secondHalf

#x = "3141592653589793238462643383279502884197169399375105820974944592"
#y = "2718281828459045235360287471352662497757247093699959574966967627"
x = "5678"
y = "1234"
karatsuba(x,y)
