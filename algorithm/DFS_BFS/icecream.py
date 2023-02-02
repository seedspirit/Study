# 문제의 n, m 값 입력받기
n, m = map(int, input().split())

# 2차원 리스트 만들기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
print(graph)

# DFS로 특정 노드 방문 후 그와 연결되어 있는 노드들 방문하기
def dfs(x, y):
    # 2차원 리스트의 범위를 벗어나는 경우
    if x <= -1 or x>=n or y<=-1 or y>=n:
        return False
    # 아직 방문하지 않은 노드라면
    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 1
        # 해당 노드에서 다른 노드들 탐색
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

# 모든 노드에 대해서 탐색하기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)
