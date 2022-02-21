#전보

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split()) #도시의 개수 1 <= n <= 30,000, 통로의 개수 1 <= m < = 200,000, 출발 도시 c

graph = [[] for _ in range(n+1)] #연결 리스트
distance = [INF] * (n+1) #최단 거리 테이블

for _ in range(m):
  x, y, z = map(int, input().split()) #특정 도시 x, 다른 특정 도시 y, 이동 시간 z
  graph[x].append((y, z))

def dijkstra(start):
  distance[start] = 0 #자기 자신으로 0
  q = []
  heapq.heappush(q,(0, start)) #우선순위 큐

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist: #최단 거리가 갱신되어 있는 경우
      continue
    
    for city in graph[now]: #현재 도시에 연결된 도시
      new_dist = dist + city[1] #현재 도시에 연결된 다른 도시로 이동 시간
      if new_dist < distance[city[0]]:
        distance[city[0]] = new_dist #최단 거리 테이블 갱신
        heapq.heappush(q, (new_dist, city[0])) #최단 거리 갱신하는 경우 우선순위 큐 삽입


dijkstra(c)

max_dist = 0
count = 0

for i in range(1, n+1):
  if 0 < distance[i] and distance[i] < INF: #출발 도시와 갈 수 없는 도시 제외
    count += 1
    max_dist = max(max_dist, distance[i])

print(count, max_dist)
  