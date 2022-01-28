from collections import deque

#BFS 너비 우선 탐색
def bfs(graph, start, visited):
  #큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  visited[start] = True #현재 노드 방문 처리
  #큐가 빌 때까지 반복
  while queue:
    v = queue.popleft() #큐에서 하나의 원소를 뽑아 출력, 선입선출
    print(v, end=' ')
    #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]: #현재 노드의 인접 노드 탐색
      if not visited[i]: #인접 노드 방문여부 확인, 방문하지 않은 경우
        queue.append(i) #방문하지 않은 노드를 큐에 추가
        visited[i] = True #추가된 노드의 방문여부 체크

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[],
[2, 3, 8],
[1, 7],
[1, 4, 5],
[3, 5],
[3, 4],
[7],
[2, 6, 8],
[1, 7]
]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9

#정의된 DFS 함수 호출
bfs(graph, 1, visited)