#간단한 다익스트라 알고리즘
#시간복잡도 O(V^2)

import sys
input = sys.stdin.readline
INF = int(1e9) #무한을 의미(10억)

n, m = map(int, input().split()) #노드의 개수 n, 간선의 개수 m
start = int(input()) #시작 노드 번호

graph = [[] for _ in range(n+1)] #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트

visited = [False] * (n+1) #각 노드에 대한 방문 여부
distance = [INF] * (n+1) #최단 거리 테이블, 무한으로 초기화

for _ in range(m):
  a, b, c = map(int, input().split()) #a번 노드에서 b번노드로 가능 비용 c
  graph[a].append((b, c)) #연결 노드에 대한 정보 저장

def get_smallest_node(): #방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
  min_value = INF
  index = 0 #가장 최단 거리가 짧은 노드 번호(인덱스)

  for i in range(1, n+1): #최단 거리 테이블을 순차 탐색
    if distance[i] < min_value and not visited[i]: #방문하지 않은 노드 중에서가장 짧은 최단 거리의 노드를 찾는다.
      min_value = distance[i]
      index = i
    return index

def dijkstra(start): #다익스트라 알고리즘
  distance[start] = 0 #시작 노드 초기화
  visited[start] = True #시작 노드 방문처리
  for i in graph[start]: #시작 노드에 연결된 노드들의 거리 입력
    distance[i[0]] = i[1]

  for _ in range(n-1): #시작 노드를 제외한 n-1개의 노드에 대해 반복
    now = get_smallest_node() #현재 최단 거리가 가장 짧은 노드
    visited[now] = True #현재 노드 방문 처리
    for i in graph[now]: #현재 노드와 연결된 노드 확인
      cost = distance[now] + i[1] #현재 노드를 거쳐서 연결 노드로 가능 거리
      if cost < distance[i[0]]: #현재 노드를 거쳐서 가는 거리가 기존 거리보다 짧은 경우
        distance[i[0]] = cost

dijkstra(start)

for i in range(1, n+1): #1번 노드부터 n번 노드까지 start노드에서 각각의 노드로 가기 위한 최단거리
  if distance[i] == INF: #갈 수 없는 경우 무한
    print('INFINITY')
  else:
    print(distance[i])