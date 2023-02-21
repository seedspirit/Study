# 내 풀이
d = [0] * 30000

x = int(input())
def cal_cnt(x):
  if x == 1:
    return None
  elif x % 5 == 0:
    x //= 5
    d[x] = 1
    return cal_cnt(x)
  elif x % 3 == 0:
    x //= 3
    d[x] = 1
    return cal_cnt(x)
  elif x % 2 == 0:
    x //= 2
    d[x] = 1
    return cal_cnt(x)
  elif (x % 5 != 0) and (x % 3 != 0) and (x % 2 != 0):
    x -= 1
    d[x] = 1
    return cal_cnt(x)

cal_cnt(x) 
print(d)
print(d.count(1) + 1)


# 책 풀이
x = int(input())
d = [0] * 30001

# 다이나믹 프로그래밍 진행 (바텀업)
for i in range(2, x+1):
  # 현재의 수에서 1을 빼는 경우
  d[i] = d[i-1] + 1
  # 현재의 수가 2로 나눠떨어지는 경우
  if i % 2 == 0:
    d[i] = min(d[i], d[i//2]+1)
  # 현재의 수가 3로 나눠떨어지는 경우
  if i % 3 == 0:
    d[i] = min(d[i], d[i//3]+1)
  # 현재의 수가 2로 나눠떨어지는 경우
  if i % 5 == 0:
    d[i] = min(d[i], d[i//5]+1)
