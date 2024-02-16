# file : ds21_dfs.py
# desc : Graph 깊이 우선 탐색 구현

# graph class 선언, 인접 행렬을 담고 있는 객체
class Graph():
    SIZE = graph = None # 멤버 변수

    def __init__(self, size) -> None:
        self.SIZE = size
        self.graph = [[0 for _ in range(self.SIZE)] for _ in range(self.SIZE)]

# 전역변수 선언
G1 = None
stack = []
visited = [] #[]
MAX = 4

# Main Code
G1 = Graph(MAX)
G1.graph[0][2] = G1.graph[2][0] = 1
G1.graph[0][3] = G1.graph[3][0] = 1
G1.graph[1][2] = G1.graph[2][1] = 1
G1.graph[2][3] = G1.graph[3][2] = 1

print('무방향 그래프 > ')


for row in range(MAX):
    for col in range(MAX):
        print(G1.graph[row][col], end=' ')
    print()

## 탐색 시작
curr = 0 # Start 정점 Vertex
stack.append(curr) # Push (A)
visited.append(curr) # list['A']

while len(stack) != 0:  #스택이 0이 되면 더이상 방문할 곳 없다
    next = None # 다음 정점 초기화
    for vertex in range(MAX):
        if G1.graph[curr][vertex] == 1:
            if vertex in visited:
                pass
            else:# 미방분 정점
                next = vertex 
                break # for 문을 탈출

    if next != None: # 다음 정점에 있으면
        curr = next
        stack.append(curr) # stack 방문한 정점 push
        visited.append(curr)

    else:
        curr = stack.pop()

print('Visit 순서 --> ', end= ' ')
for i in visited:
    print(chr(ord('A')+i), end=' ')