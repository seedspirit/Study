# 내 풀이

S = input()
data_list = sorted(S)
result = 0
tmp = []

for data in data_list:
    if int(data) == True:
        result += int(data)
        print("result: ", result)
    else:
        tmp.append(data)
        print("tmp: ", tmp)
        
        
# 정답
data = input()
result = []
value = 0

for x in data:
	if x.isalpha():
    	result.append(x)
    else:
    	value += int(x)

result.sort()

if value != 0:
	result.append(str(value))
 print(''.join(result))
