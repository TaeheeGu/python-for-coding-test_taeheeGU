#부품 찾기
import sys

n = int(sys.stdin.readline())
#set자료형 활용. 단순히 특정 데이터가 존재하는지 검사할 때 매우 효과적
#중복을 허용하지 않으며, 순서가 없다. add(), remove(), update() 함수 존재
array_N = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
array_M = list(map(int, sys.stdin.readline().split()))

for  i in array_M:
  if i in array_N:
    print('yes', end=' ')
  else:
    print('no', end=' ')