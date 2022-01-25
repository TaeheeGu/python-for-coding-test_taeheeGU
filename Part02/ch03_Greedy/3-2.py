#큰 수의 법칙
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

result = 0
count = 0

max_value = max(data) #가장 큰 수
data.remove(max_value) #기존 리스트에서 가장 큰 수 제거
second_max = max(data) #두 번째로 큰 수

for i in range(m):
  if count < k:
    result += max_value
    count +=1
  else:
    result += second_max
    count = 0

print(result)

'''
data.sort()
first = data[n-1]
second = data[n-2]

count = (m//(k+1))*k + (m%(k+1)) #가장 큰 수 더하는 횟수

result = 0
result = conut * first + (m - count) * second
'''