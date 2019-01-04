import operator

highestNumber = 0
t = 0
s = 0

def readFile(filename):
    global highestNumber
    edgeList = list()
    with open(filename) as file:
        contents = file.read()
    contents = contents.splitlines()
    for line in contents:
        line = line.split(" ")
        tail = int(line[0])
        head = int(line[1])
        if tail > highestNumber:
            highestNumber = tail
        elif head > highestNumber:
            highestNumber = head
        edge = { "tail" : tail, "head" : head}
        edgeList.append(edge)
    return edgeList

def generateVerticies(edgeList):
    verticies = list()
    for i in range(0,highestNumber+1):
        incoming = list()
        outgoing = list()
        rev_incoming = list()
        rev_outgoing = list()
        vertex = { "id" : i , "explored": False, "finishingTime": 0, "incoming" : incoming, "outgoing" : outgoing, "rev_incoming" : rev_incoming, "rev_outgoing" : rev_outgoing, "leader" : 0, "isLeader" : 0}
        verticies.append(vertex)
    for edge in edgeList:
        verticies[edge.get("tail")].get("outgoing").append(edge.get("head"))
        verticies[edge.get("head")].get("incoming").append(edge.get("tail"))
        verticies[edge.get("tail")].get("rev_incoming").append(edge.get("head"))
        verticies[edge.get("head")].get("rev_outgoing").append(edge.get("tail"))
    return verticies

def DFSLoop(g,type,gsort=""):
    global s
    for i in range(len(g)-1, 0, -1):
        if gsort == "":
            if g[i].get("explored") == False:
                s = i
                g = DFS(g,i,type)
        else:
            if gsort[i].get("explored") == False:
                id = gsort[i]["id"]
                s = id
                g = DFS(g, id, type)
    return g

def DFS(g, i, type):
    global t
    global s
    g[i]["explored"] = True
    g[i]["leader"] = s
    if type == "reg":
        g[s]["isLeader"] += 1
        outgoingNodes = g[i].get("outgoing")
    else:
        outgoingNodes = g[i].get("rev_outgoing")
    for edge in outgoingNodes:
        if g[edge].get("explored") == False:
            g = DFS(g,edge,type)
    t += 1
    g[i]["finishingTime"]= t
    return g

def processNodesWithFinishingTimes(g):
    for vertex in g:
        vertex["explored"] = False
        origin = vertex["id"]
        vertex["id"] = vertex["finishingTime"]
        print "Replacing origin " + str(origin) + " with " + str(vertex["id"])
        for node in vertex["incoming"]:
            for index in g[node]["outgoing"]:
                if index == origin:
                    index = vertex["id"]
        for node in vertex["outgoing"]:
            for index in g[node]["incoming"]:
                if index == origin:
                    index = vertex["id"]
    return g

def kosaraju(g):
    g = DFSLoop(g, "rev")
    for item in g:
        item["explored"] = False
    gsort = list(g)
    gsort.sort(key=operator.itemgetter('finishingTime'))
    print "----"
    g = DFSLoop(g, "reg",gsort)
    g.sort(key=operator.itemgetter('isLeader'),reverse=True)
    for item in g:
        print str(item["id"]) + ", " + str(item["isLeader"])


edgeList = readFile('scc.txt')
verticies = generateVerticies(edgeList)
kosaraju(verticies)