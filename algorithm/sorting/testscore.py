# 내 풀이
n = int(input())

data = []
for i in range(n):
    data.append((input().split()))

data = sorted(data, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(data[i][0], end='\n')
    
# 책 풀이
n = int(input())
students = []

for _ in range(n):
	students.append(input().split())
    
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
	print(student[0])
