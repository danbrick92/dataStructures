from random import randint
import random

class Vertex:
    identity = ""
    incidents = list()

    def __init__(self,id,ListOfIncidents):
        self.identity = id
        self.incidents = ListOfIncidents

def readFile(filename):
    finalList = list()
    with open(filename) as file:
        contents = file.read()
    contents = contents.splitlines()
    for line in contents:
        splits = line.split("\t")
        index = splits[0]
        isFirst = True
        listOfVerticies = list()
        for number in splits:
            if isFirst:
                isFirst = False
                continue
            if number == '':
                continue
            number = int(number)
            listOfVerticies.append(number)
        newVertex = Vertex(index, listOfVerticies)
        finalList.append(newVertex)
    return finalList

def pickRandomDeleteUnityIndex(adjacencyList):
    indexDelete = randint(0, len(adjacencyList)-1)
    indexUnity = randint(0, len(adjacencyList)-1)
    while indexUnity == indexDelete:
        indexUnity = randint(0, len(adjacencyList)-1)
    return indexDelete, indexUnity

def removeSelfLoops(incidents,index):
     i = 0
     for incident in incidents:
         if incident == index:
             del incidents[i]
         i+=1
     return incidents

def replaceDeletedReferences(adjacencyList,vertexOfDeletion,vertexOfReplacing):
    for adjacency in adjacencyList:
        for incident in adjacency.incidents:
            if incident == vertexOfDeletion:
                incident = vertexOfReplacing
    return adjacencyList

def findMinCut(adjacencyList):
    while len(adjacencyList) > 2:
        #indexDelete,indexUnity = choose_random_key(adjacencyList)
        indexDelete,indexUnity = pickRandomDeleteUnityIndex(adjacencyList)
        unified = adjacencyList[indexUnity]
        unified.incidents = unified.incidents + adjacencyList[indexDelete].incidents
        unified.incidents = removeSelfLoops(unified.incidents,unified.identity)
        adjacencyList[indexUnity] = unified
        vertexOfDeletion = adjacencyList[indexDelete].identity
        vertexOfReplacing = adjacencyList[indexUnity].identity
        del adjacencyList[indexDelete]
        adjacencyList = replaceDeletedReferences(adjacencyList,vertexOfDeletion,vertexOfReplacing)
    crazylist = list()
    for vert in adjacencyList:
        crazylist.append(len(vert.incidents))
    return crazylist[1]

lowestNumber = 100000000000000000000000000000000
adjacencyList = readFile("mincut.txt")
#timesToRun = len(adjacencyList)
timesToRun = 10000
for k in range(0,timesToRun):
    adjacencyList = readFile("mincut.txt")
    mincut = findMinCut(adjacencyList)
    if mincut < lowestNumber:
        lowestNumber = mincut
print "Lowest mincut found = " + str(lowestNumber)
