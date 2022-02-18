#다익스트라 알고리즘
#우선순위 큐 사용, 시간복잡도 O(ElogV)

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) #무한을 의미하는 값

n, m = map(int, input().split()) #n은 노드의 개수, m은 간선의 개수
start = int(input()) #시작 노드 번호

graph = [[] for _ in range(n+1)] #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
distance = [INF] * (n+1) #최단 거리 테이블 모두 무한으로 초기화

for _ in range(m): #모든 간선 정보 입력 받기
  a, b, c = map(int, input().split()) #a번 노드에서 b번 노드로 가는 거리 c
  graph[a].append((b, c))

def dijkstra(start):
  q = [] #우선순위 큐
  heapq.heappush(q, (0, start)) #시작 노드로 가는 최단 거리는 0, 큐에 삽입
  distance[start] = 0 #시작 노드로의 최단 거리는 0

  while q: #큐를 모두 비울때까지 반복
    dist, now = heapq.heappop(q) #가장 최단 거리가 짧은 노드 정보 큐에서 꺼내기

    if distance[now] < dist: #이미 처리되어 현재 노드(now)까지 거리가 큐에 저장된 최단 거리보다 짧은 경우
      continue #처리된 적이 있는 노드는 무시하고 넘어간다
    
    for  i in graph[now]: #현재 노드와 연결된 다른 인접한 노드 확인
      cost = dist + i[1] #현재 노드를 거쳐서 인접 노드로 가는 비용
      if cost < distance[i[0]]: #현재 노드를 거쳐서 인접 노드로 가는 거리가 더 짧은 경우
        distance[i[0]] = cost #해당 노드의 최단 거리 갱신
        heapq.heappush(q, (cost, i[0])) #갱신된 노드의 정버(거리, 번호)를 큐에 삽입

dijkstra(start)

for i in range(1, n+1): #1 ~ n번 까지의 노드
  if distance[i] == INF:
    print('INFINITY') #도달할 수 없는 경우
  else:
    print(distance[i]) #start 노드부터 각각의 노드까지 최단 거리 출력
    