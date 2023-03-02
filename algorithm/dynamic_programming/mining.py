# 책 풀이
for tc in range(int(input())):
  # 금광 정보 입력
  n, m = map(int, input().split())
  array = list(map(int, input().split()))

  # 다이나믹 프로그래밍을 위한 2차원 dp 테이블 초기화
  dp =[]
  index = 0
  for i in range(n):
    dp.append(array[index:index + m])
    index += m

  # 다이나믹 프로그래밍 진행
  for j in range(1, m):
    for i in range(n):
      # 왼쪽 위에서 오는 경우
      if i == 0:
        left_up = 0
      else:
        left_up = dp[i-1][j-1]
      # 왼쪽 아래에서 오는 경우
      if i == n-1:
        left_down = 0
      else:
        left_down = dp[i+1][j-1]
      # 왼쪽에서 오는 경우
      left = dp[i][j-1]
      dp[i][j] = dp[i][j] + max(left_up, left_down, left)

result = 0
for i in range(n):
  result = max(result, dp[i][m-1])

print(result)

"""
3. 새롭게 알게 된 것 or 새삼 다시 알게 된 것

1) 알게 된 것은 아니고 의문: 매 직후에 가장 큰 값을 선택하는 방식으로 진행이 되는데 이렇게 어떻게 보면 탐욕적으로? 진행해도 괜찮은 것인가? 직후에 가장 최대 값이 되는 것을 고르는게 최종적으로도 최대값이라는 것을 어떻게 보장하지?

2) dp 테이블이 반드시 1차원일 필요는 없다

3) 2차원 테이블 만드는 코딩 스킬
"""
