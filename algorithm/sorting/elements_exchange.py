# 1. 내 풀이

n, k = map(int, input().split())
array_a = sorted(input().split())
array_b = sorted(input().split(), reverse=True)

for i in range(k):
    if array_a[i] < array_b[i]:
        array_a[i], array_b[i] = array_b[i], array_a[i]
    else:
        continue

result = 0

for j in range(n):
    result += int(array_a[j])

print(result)

# 2. 정답
n, k = map(int, input().split())
array_a = sorted(list(map(int, input().split())))
array_b = sorted(list(map(int, input().split())))

for i in range(k):
	if array_a[i] < array_b[i]:
    	array_a[i], array_b[i] = array_b[i], array_a[i]
    else:
    	break

print(sum(array_a))
