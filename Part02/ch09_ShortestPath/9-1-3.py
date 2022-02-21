#플로이드 워셜 알고리즘

import sys

intput = sys.stdin.readline
INF = int(1e9) #무한을 의미하는 값, 10억

n, m = map(int, input().split()) #노드의 개수 n, 간선의 개수 m

graph = [[INF]*(n+1) for _ in range(n+1)] #2차원 리스트(그래프 표현), 모든 값 무한을 초기화

for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j:
      graph[i][j] = 0 #자기 자신으로 가는 비용 0으로 초기화

for _ in range(m): #각 간선에 대한 정보
  a, b, c = map(int, input().split()) #a에서 b로 가는 거리 c
  graph[a][b] = c

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) #a에서 b로 가는 거리, a에서 k를 거쳐 b로 가는 거리 비교

#수행된 결과 2차원 리스트 출력
for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] == INF: #도달할 수 없는 경우
      print('INFINITY')
    else:
      print(graph[i][j], end=' ')

  print() #한 행 출력 후줄바꿈