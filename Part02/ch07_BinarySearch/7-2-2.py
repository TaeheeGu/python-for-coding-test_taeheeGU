#부품 찾기
import sys

n = int(sys.stdin.readline())
array_N = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
array_M = list(map(int, sys.stdin.readline().split()))

#계수 정렬 풀이
count_array = [0] * 1_000_001 #n의 범위 1부터 1,000,000 까지
#count_array = [0] * (max(array_N)+1)

for i in array_N:
  count_array[i] += 1

for i in array_M:
  if count_array[i] == 0:
    print('no', end=' ')
  else:
    print('yes', end=' ')
