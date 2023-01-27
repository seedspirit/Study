# 내 풀이
n = input()

point = len(n) // 2
front = 0
back = 0

for i in range(point):
    front += int(n[i])
    back += int(n[-i-1])

if front == back:
    print('LUCKY')
else:
    print('READY')
    
    
# 정답
n = input()
length = len(n)
summary = 0

for i in range(length//2):
	summary += int(n[i])
   
for i in range(length //2, length):
	summary -= int(n[i])
   
if summary == 0:
	print("LUCKY")
else:
	print("READY")
