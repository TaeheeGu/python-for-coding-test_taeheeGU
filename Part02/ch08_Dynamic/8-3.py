#개미 전자
import sys

n = int(sys.stdin.readline()) #3 <= n <= 100 식량창고의 개수
k = list(map(int, sys.stdin.readline().split())) #0 <= k <= 1000 식량의 개수

total = [0] * 101

total[1] = k[1]
total[2] = max(k[1], k[2])

for i in range(3, n+1):
  total[i] = max(k[i-1], k[i-2]+k[i])

print(total(n))
