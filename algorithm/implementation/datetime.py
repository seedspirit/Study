# 내가 푼 것
n = int(input())

if n < 3:
    print(16*16* (n+1))
elif n >=3 and n<13 :
    print(16*16*(n))
elif n >=13 and n <23:
    print (16*16*(n-1))
elif n == 23:
    print(16*16*(n-2))
    
    
# 정답
h = int(input())
count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)


"""
배운 것:
- 완전탐색 유형은 가능한 경우의 수를 모두 검사해보는 탐색 유형
- 다만, 이럴 경우 매우 비효율적인 시간 복잡도를 가지고 있으므로 데이터 개수가 큰 경우 (100만 개 이상) 시간 복잡도 제한에 걸릴 수 있음. 그렇지 않은 경우에 사용
- 나도 문제를 처음 풀 때 3중 for 문을 생각하긴 했지만, 시간 복잡도 때문에 그 방법을 포기하고 다른 방법을 취함.
- 하지만, 만약 데이터의 수가 충분히 작다면 한 번 시도해볼만한 방법인 것 같음.
"""
