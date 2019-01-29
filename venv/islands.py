"""
Author: ConnerDavis
"""
class Tile:
    def __init__(self, tileType):
        self.tileType = tileType
        self.connections = list()
        self.visited = False

    def addEdge(self, other):
        self.connections.append(other)
        other.addEdgeReciprocal(self)

    def addEdgeReciprocal(self, other):
        self.connections.append(other)

    def traverse(self):
        self.visited = True
        for other in self.connections:
            if not other.getVisited():
                if other.getTileType() == 'C' or other.getTileType() == 'L':
                    other.traverse()

    def getVisited(self):
        return self.visited

    def getTileType(self):
        return self.tileType


def process(strings):

    if strings is None:
        return -1

    twoD_list = list()

    anyL = False
    for i in range(0, len(strings)):
        twoD_list.append(list())
        for j in range(0, len(strings[i])):
            tmp = strings[i][j:j+1]
            twoD_list[i].append(Tile(tmp))
            if i != 0:
                twoD_list[i][j].addEdge(twoD_list[i-1][j])
            if j != 0:
                twoD_list[i][j].addEdge(twoD_list[i][j-1])
            if tmp == 'L':
                anyL = True

    if not anyL:
        return 0

    result = 0
    for i in twoD_list:
        for j in i:
            if not j.getVisited():
                if j.getTileType() == 'L':
                    j.traverse()
                    result += 1
    return result