import math
accuracy = []
class Node:
    def __init__(self,name):
        self.name = name
        self.pagerank = 0
        self.visited = False

def graphfromfile():
    #return calculategraphscaleFreeGraph()
    return graphfromfilecsv("data/routes.csv")

def graphfromfilecsv(filename):
    directedgraph = {}
    undirectedgraph = {}
    nodemap = {}
    count = 0
    with open(filename) as fp:
        for line in fp:
            count += 1
            source = line.split(",")[2]
            dest = line.split(",")[4]
            #-----------------------------------
            if not (source in nodemap):
                nodemap[source] = Node(source)
            if not (dest in nodemap):
                nodemap[dest] = Node(dest)
            #------------------------------------
            if not (dest in directedgraph):
                directedgraph[dest] = []

            if source in directedgraph:
                directedgraph[source].append(dest)
            else:
                directedgraph[source] = [dest]
            #------------------------------------

            if not (dest in undirectedgraph):
                directedgraph[dest] = []
            if source in undirectedgraph:
                undirectedgraph[source].append(dest)
            else:
                undirectedgraph[source] = [dest]
            if dest in undirectedgraph:
                undirectedgraph[dest].append(source)
            else:
                undirectedgraph[source].append(dest)
            #--------------------------------------
    #print("Total number of lines:--> "+str(count))
    return nodemap, directedgraph, undirectedgraph
x = None
def calculategraphscaleFreeGraph():
    global x
    import scipy.io as spio
    if x is None:
        file3 = "D://feastpack_v1.1//feastpack_v1.1//data/test.mat"
        matrix = spio.loadmat(file3)['G_bter']
        x = [(i, j) for i in range(0, 497) for j in range(0, 497) if matrix[i, j] == 1]
    directedgraph = {}
    undirectedgraph = {}
    nodemap = {}
    count = 0
    for t in x:
        source = t[0]
        dest = t[1]
        if not (source in nodemap):
            nodemap[source] = Node(source)
        if not (dest in nodemap):
            nodemap[dest] = Node(dest)
        # ------------------------------------
        if not (dest in directedgraph):
            directedgraph[dest] = []

        if source in directedgraph:
            directedgraph[source].append(dest)
        else:
            directedgraph[source] = [dest]
        # ------------------------------------

        if not (dest in undirectedgraph):
            directedgraph[dest] = []
        if source in undirectedgraph:
            undirectedgraph[source].append(dest)
        else:
            undirectedgraph[source] = [dest]
        if dest in undirectedgraph:
            undirectedgraph[dest].append(source)
        else:
            undirectedgraph[source].append(dest)
    return nodemap, directedgraph, undirectedgraph

def checkconnectivity(graph, nodemap, node):
    if nodemap[node].visited:
        return
    nodemap[node].visited = True
    if not node in graph:
        return
    for adjnode in graph[node]:
        checkconnectivity(graph, nodemap, adjnode)

def removeunconnectedcomponents(undirectedgraph, directedgraph, nodemap):
    node = list(nodemap.keys())[150]
    checkconnectivity(undirectedgraph,nodemap,node)
    notvisited = 0
    notvisitedlst = []
    for node in nodemap.keys():
        if not nodemap[node].visited:
            notvisited += 1
            notvisitedlst.append(node)
    for node in notvisitedlst:
        undirectedgraph.pop(node, None)
        directedgraph.pop(node, None)
        nodemap.pop(node,None)
    return notvisited

'''
  Initalizing the pagerank of the nodes with 1/N
  So that they will sum to ONE 
'''
def initilizationofPageRank(nodemap,val = None):
    keys = list(nodemap.keys())
    N = len(keys)
    if val is None:
        val = 1/N
    for node in nodemap:
        nodemap[node].pagerank = val


'''
  Make inverted graph
'''
def construct_invertedgraph(graph):
    invertedgraph = {}
    for node in graph:
        adjList = graph[node]
        for childnode in adjList:
            if not (node in invertedgraph):
                invertedgraph[node] = []

            if childnode in invertedgraph:
                invertedgraph[childnode].append(node)
            else:
                invertedgraph[childnode] = [node]
    return invertedgraph

'''
   This is will print states of the graph
   like number of nodes in graph, number of edges in graph
   
'''
def printstats(graph, invertedgraph):
    nodes = list(graph.keys())
    numvertices = len(nodes)
    edges = 0
    outdegrees = []
    indegree = []
    for node in nodes:
        adjList = graph[node]
        edges += len(adjList)
        outdegrees.append(len(adjList))
    for node in invertedgraph:
        adjList = invertedgraph[node]
        indegree.append(len(adjList))
    print("-------------- stats ----------------")
    print("num vertices:---->>>"+str(numvertices))
    print("num edges:------->>>"+str(edges))
    print("avg outdegree vertices-->>"+str(sum(outdegrees)/len(outdegrees)))
    print("avg indegree vertices-->>" + str(sum(indegree) / len(indegree)))
    print("-------------------------------------")

'''
single iteration step 

this method will return boolean value says whether to continue for next iteration or not that it
'''
def pagerankiteration(nodemap, graph, invertedgraph,d, threshold):
    maxchange = 0
    evalution_of_pages = []
    for node in invertedgraph:
        adjList = invertedgraph[node]
        evalution_of_pages.append(node)
        currentpagerank = 0
        for childnode in adjList:
            currentpagerank += (nodemap[childnode].pagerank/len(graph[childnode]))
        temp = (1-d)+(d*currentpagerank)
        maxchange = max(maxchange, math.fabs(temp-nodemap[node].pagerank))
        nodemap[node].pagerank = temp
    #print(evalution_of_pages)
    #print(maxchange)
    if maxchange <= threshold:
        return False
    return True

'''
  This method will take number of iterations we need to compute pagerank
'''
def dopagerank(nodemap, graph, invertedgraph, d=0.5,threshold=0.000001):
    print("-------------------- In page rank ----------------------------")
    iter_count = 1
    while pagerankiteration(nodemap, graph, invertedgraph, d, threshold):
        #printpagerank(nodemap)
        iter_count += 1
    #print(iter_count)
    print("------------------ End of Page rank --------------------------")
    return iter_count

def createnodemap(graph):
    nodemap = {}
    for node in graph:
        nodemap[node] = Node(node)
    return nodemap

def printpagerank(nodemap):
    for node in nodemap:
        print(node+" "+str(nodemap[node].pagerank))

def top5pages(nodemap):
    pagevalues = sorted(nodemap.values(), key = lambda x: -1*x.pagerank)
    for i in range(5):
        print(pagevalues[i].name+"-------------->>>>>>"+str(pagevalues[i].pagerank))

def compareorder(truthorder, curorder):
    curres = []
    for i in range(1,6):
        items = int(i/100 * len(truthorder))
        truthnames = [truthorder[i].name for i in range(items)]
        curnames = [curorder[i].name for i in range(items)]
        intersectionset = set(truthnames) & set(curnames)
        curres.append(len(intersectionset)/len(curnames) * 100 )
    accuracy.append(curres)
    '''
    for i in range(0,len(truthorder)):
        if truthorder[i].name != curorder[i].name:
            print("---->>> "+str(i));
            break
    '''
def pageranktruthorder():
    nodemap, directedgraph, undirectedgraph = graphfromfile()
    removeunconnectedcomponents(undirectedgraph, directedgraph, nodemap)
    invertedgraph = construct_invertedgraph(directedgraph)
    initilizationofPageRank(nodemap)
    d = 0.85
    iterationcount = dopagerank(nodemap, directedgraph, invertedgraph, d , 0)
    pagevalues = sorted(nodemap.values(), key=lambda x: -1*x.pagerank)
    return pagevalues

def pagerank():
    steps = [0.05]
    laststep = 0.05
    truthorder = pageranktruthorder()
    while laststep < 1:
        laststep = laststep + 0.05
        steps.append(laststep)
    res = []
    for i in range(len(steps)):
        nodemap, directedgraph, undirectedgraph = graphfromfile()
        removeunconnectedcomponents(undirectedgraph, directedgraph, nodemap)
        invertedgraph = construct_invertedgraph(directedgraph)
        initilizationofPageRank(nodemap)
        d = steps[i]
        iterationcount = dopagerank(nodemap, directedgraph, invertedgraph, d , 0)
        curorder = sorted(nodemap.values(), key = lambda x: -1*x.pagerank)
        compareorder(truthorder,curorder)
        #truthorder = curorder
        print(res)
        res.append((d, iterationcount))
        print(res)
        print(accuracy)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(accuracy)


def testcase1():
    graph = {}
    graph['A'] = ['B']
    graph['B'] = ['A']
    #-----------------------
    invertedGraph = {}
    invertedGraph['B'] = ['A']
    invertedGraph['A'] = ['B']
    #------------------------
    nodemap = {}
    nodemap['A'] = Node('A')
    nodemap['B'] = Node('B')
    nodemap['A'].pagerank = 0.5
    nodemap['B'].pagerank = 0.5
    dopagerank(nodemap, graph, invertedGraph, 0.5, 0)
    print(nodemap['A'].pagerank)
    print(nodemap['B'].pagerank)

def testcase2():
    graph = {}
    graph['A'] = ['B','C']
    graph['B'] = ['C']
    graph['C']  = ['A']
    graph['D'] = ['C']
    invertedgraph = construct_invertedgraph(graph)
    nodemap = createnodemap(graph)
    initilizationofPageRank(nodemap,20)
    dopagerank(nodemap, graph, invertedgraph, 0.1, 0)
    printpagerank(nodemap)
    print("---------- inverted graph -------------------------")
    print(invertedgraph)
    print("---------------------------------------------------")
    print("---------- graph ----------------------------------")
    print(graph)
    print("--------------------------------------------------- ")

def testcase3():
    graph = {}
    graph['A'] = ['B','C']
    graph['B'] = ['C']
    graph['C'] = ['A','B']
    invertedgraph = construct_invertedgraph(graph)
    nodemap = createnodemap(graph)
    initilizationofPageRank(nodemap, 1)
    dopagerank(nodemap, graph, invertedgraph, 0.75, 0)
    printpagerank(nodemap)
    print("---------- inverted graph -------------------------")
    print(invertedgraph)
    print("---------------------------------------------------")
    print("---------- graph ----------------------------------")
    print(graph)
    print("--------------------------------------------------- ")

#testcase1()
#testcase2()
#testcase3()
pagerank()
