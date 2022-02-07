#위에서 아래로
n = int(input())

array = []

for i in range(n):
  array.append(int(input()))

result = sorted(array, reverse = True) #내림차순 정렬

for i in result: #정렬이 수행된 결과를 출력
  print(i, end=' ')