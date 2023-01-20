# 내가 작성한 답안
import sys
input = sys.stdin.readline
n = int(input())
x = 1
y = 1
for i in range(n):
    tmp = input().split()
    if tmp == 'R':
        y += 1
        if y > n:
            y -= 1
    if tmp == 'L':
        y -= 1
        if y <= 0:
            y += 1
    if tmp == 'U':
        x -= 1
        if x <= 0:
            x -= 1
    if tmp == 'D':
        x += 1
        if x > n:
            x += 1
print(x, y)


------

# 정답

# n 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_types)): 
    # types에서 하나씩 원소 꺼내보며 확인하기
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
    # 공간을 벗어나는 경우 무시하기
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  # 이동 수행
  x , y = nx, ny

print(x, y)
