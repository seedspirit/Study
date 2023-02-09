# 내 풀이
n = int(input())
data = {}

for i in range(n):
    tmp = input().split()
    data[tmp[0]] = int(tmp[1])

score_chart = sorted(list(data.values()))

for i in range(len(score_chart)):
  val = score_chart[i]
  for k, v in data.items():
    if v == val:
      print(k, end= ' ')
      
      
      
      
# 정답
n = int(input())

data = []
for i in range(n):
	input_data = input().split()
    data.append((input_data[0], int(input_data[1])))

data = sorted(data, key=lambda student:student[1])

for student in data:
	print(student[0], end=' ')
