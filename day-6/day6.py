from collections import defaultdict

def readFile(file):
    inplist = []
    with open(file) as f:
        line = f.readline().rstrip()
        while line:
            inplist.append(line)
            line = f.readline().rstrip()
    return inplist

def buildGraph(ilist):
    graph = defaultdict(str)
    for pair in ilist:
        pair = pair.split(')')
        graph[pair[1]] = pair[0]
    return graph
        
def countOrbits(graph, node):
    if node in graph.keys():
        parent = graph[node]
        if parent in memo.keys():
            result = memo[parent]
        else:
            result = countOrbits(graph, parent)
        return (1 + result)
    return (0)

def findPath(graph, source, target):
    root = 'COM'
    node = source
    path1, path2 = [], []
    while node != root:
        node = graph[node]
        path1.append(node)
    node = target
    while node != root:
        node = graph[node]
        path2.append(node)
    path1.reverse()
    path2.reverse()
    i = 0
    while path1[i] == path2[i]:
        i += 1
    path1 = path1[i:]
    path2 = path2[i:]
    return (len(path1) + len(path2))

print("Part 1:")
inp = readFile("orbits.txt")
g = dict(buildGraph(inp))
count = 0
memo = {}
for i in g.keys():
    res = countOrbits(g, i)
    memo[i] = res
    count += res
print("Sum of Orbits:",count)
print("Part 2:")
print("Number of transfers:",findPath(g, 'YOU', 'SAN'))
