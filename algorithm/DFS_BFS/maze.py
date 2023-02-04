# 내 풀이

n, m = map(int, input().split())

# 미로 만들기
graph = []
for i in range(n):
    for j in range(m):
        graph.append(list(int(input())))

def dfs(x, y):
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
    else:
        return False

def visited():
    if
    
    
# 정답
from collecitons import deque

n, m = map(int, input().split())

# 미로 만들기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
# 이동할 네 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def bfs(x,y):
	queue = deque()
	queue.append((x,y))
	while queue:
	x, y = queue.popleft()
	for i in range(4):
    	nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
        	continue
        if graph[nx][ny] == 0:
        	continue
        if graph[nx][ny] == 1:
        	graph[nx][ny] = graph[x][y] + 1
            queue.append((nx,ny))
	return graph[n-1][m-1]
 
 print(bfs(0,0))
