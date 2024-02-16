# file : ds21_dfs.py
# desc : Graph 깊이 우선 탐색 구현

# graph class 선언, 인접 행렬을 담고 있는 객체
class Graph():
    SIZE = graph = None # 멤버 변수

    def __init__(self, size) -> None:
        self.SIZE = size
        self.graph = [[0 for _ in range(self.SIZE)] for _ in range(self.SIZE)]

# 전역변수 선언