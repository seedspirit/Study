n = int(input())
stock = sorted(list(map(int, input().split())))
m = int(input())
request = sorted(list(map(int, input().split())))
print(f"stock: {stock}, request: {request}")

def binary_search(array, target, start, end):
  if start > end:
    return print('no')
  mid = (start+end) // 2
  if array[mid] == target:
    return print('yes')
  elif array[mid] < target:
    return binary_search(array, target, mid+1, end)
  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)


for i in range(m):
  target = request[i]
  binary_search(stock, target, 0, len(stock)-1)
