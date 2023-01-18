n, m = map(int, input().split())
tmp = []

for i in range(n):
  data = list(map(int, input().split()))
  data.sort()
  tmp.append(data[0])
 
tmp.sort()
result = tmp[-1]
print(result)
