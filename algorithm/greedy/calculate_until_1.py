### 나의 문제 풀이

n, k = map(int, input().split())
count = 0
while True:
  if n == 1:
    break
  while n % k != 0
    count += 1
    n -= 1
  count += 1
  n //= k
print(count)


### 더 효율적인 문제 풀이

n, k = map(int, input().split())
count = 0

while True:
  target = (n // k) * k
  count = n - target   # 한 번에 빼줌으로써 연산횟수를 줄임 (내 버전에서는 순차적으로 1씩 빼는거라 시간 복잡도가 증가)
  n = target
  
  if n < k:
    break
  
  count += 1
  n //= k
  
count += (n-1)
print(count)
