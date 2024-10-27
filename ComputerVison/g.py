class Graph():
    def __init__ (self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

G1, G3 = None, None
graphSize = 6

G1 = Graph(graphSize)
G1.graph[0][1] = 1; G1.graph[0][3] = 1; G1.graph[0][4] = 1
G1.graph[1][0] = 1; G1.graph[1][3] = 1
G1.graph[2][3] = 1; G1.graph[2][4] = 1; G1.graph[2][5] = 1
G1.graph[3][1] = 1; G1.graph[3][2] = 1; G1.graph[3][4] = 1; G1.graph[3][5] = 1
G1.graph[4][0] = 1; G1.graph[4][2] = 1; G1.graph[4][3] = 1
G1.graph[5][1] = 1; G1.graph[5][2] = 1; G1.graph[5][3] = 1

print('## G1 무방향 그래프 ##')
for row in range(graphSize):
    for col in range(graphSize):
        print(G1.graph[row][col], end=' ')
    print()