#부품 찾기
import sys

n = int(sys.stdin.readline())
array_N = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
array_M = list(map(int, sys.stdin.readline().split()))

#이진 탐색 풀이
array_N.sort() #이진 탐색을 위해 정렬 O(NlogN)

def binary_search(array, target, start, end):
  if start > end:
    return 'no'

  mid = (start + end)//2

  if target == array[mid]:
    return 'yes'
  elif target < array[mid]:
    return binary_search(array, target, start, mid-1)
  else:
    return binary_search(array, target, mid+1, end)
  
for i in array_M: #O(M)
  print(binary_search(array_N, i, 0, n-1), end= ' ') #O(logN)
  
#시간 복잡도 NlogN + MlogN = (N+M)logN