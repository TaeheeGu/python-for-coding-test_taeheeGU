#미래 도시

import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) #전체 회사의 개수 n, 경로의 개수 m, 1 <= n,m <= 100

graph = [[INF] * (n+1) for _ in range(n+1)] #각 도시의 연결 상태

for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j:
      graph[i][j] = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1 #도시간 이동 시간은 1
  graph[b][a] = 1 #도시간 양방향 이동 가능

x, k = map(int, input().split()) #목적지 x, 경유지 k

for a in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      graph[i][j] = min(graph[i][j], graph[i][a] + graph[a][j])

dist = graph[1][k] + graph[k][x] #1에서 k로 k에서 x로 최단 거리

if dist >= INF:
  print(-1)
else:
  print(dist)