# 내 풀이
# 떡들을 작은 순서대로 정렬하고
# height 이상인 떡을 찾아 거기에서부터 새로운 떡 후보군을 만들고
# 후보군에서 떡 길이를 잘라서 합이 정확히 손님이 요청한 길이가 될때까지 자르는 것을 반복한다
# 아래는 틀린 정답이고, 재귀함수 최대 깊이에 걸리는 에러가 난다

n, m = map(int, input().split())
data = list(map(int, input().split()))
answer = 0
result = 0

data.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (end-start) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        binary_search(array, target, start, mid-1)
    else:
        binary_search(array, target, mid+1, end)

while True:
    answer += 1
    start_point = binary_search(data, answer, 0, len(data)-1)
    for i in data[start_point:]:
        result += (i - answer)
    if result == m:
        break
    else:
        continue

print(answer)

# 예제 코드
import sys
# 떡의 개수 N과 요청한 떡의 길이 M 입력 받기
n, m = map(int, sys.stdin.readline().rstrip().split())
# 떡의 개별 높이 입력 받기
n_list = list(map(int, sys.stdin.readline().rstrip().split()))

# 이진 탐색 시작 위치와 종료 위치 초기화
start = 0
end = max(n_list)

# 절단기의 높이
result = 0

while (start < end):

    # 절단기 높이 지정
    mid = (start+end)//2

    sum = 0
    # 절단기로 모든 떡을 잘랐을 때, 남은 떡의 길이 계산
    for n in n_list:
        # 떡의 높이가 더 높을 때만 자를 수 있음
        if (n > mid):
            sum += n - mid

    # 남은 떡의 길이가 손님이 요청한 떡의 길이보다 적을 경우, 
    # 절단기의 높이를 낮춰야함
    if (sum < m):
        end = mid - 1

    # 남은 떡의 길이가 손님이 요청한 떡의 길이보다 많거나 같을 경우, 
    # 해당 절단기의 높이를 기록하고, 절단기의 높이를 높여야함
    else:
        result = mid
        start = mid + 1

print(result)
