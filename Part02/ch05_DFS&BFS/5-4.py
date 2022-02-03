#미로 탈출
from collections import deque

n, m = map(int, input().split())

graph=[]
for i in range(n):
  graph.append(list(map(int, input())))

#상, 하, 좌, 우 이동 방향
drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

def bfs(row, col):
  queue = deque()
  queue.append((row, col)) #현재 위치 큐에 삽입

  while queue: #큐가 빌 때 까지 실행
    row, col = queue.popleft() #큐에서 탐색을 시작할 노드를 꺼낸다
    for i in range(4):
      nrow = row + drow[i]
      ncol = col + dcol[i]

      if nrow < 0 or nrow >= n or ncol < 0 or ncol >= m: #범위를 벗어난 경우
        continue #다음 이동 방향 탐색
      
      if graph[nrow][ncol] == 0: #이동 위치가 벽인 경우
        continue #다음 이동 방향 탐색
      
      #해당 노드를 처음 방문하는 경우에만 최단 거리 기록이 된다
      if graph[nrow][ncol] == 1: #이동이 가능한 경우, 처음 방문하는 노드일 경우
        graph[nrow][ncol] = graph[row][col] + 1 #방문 순서를 기록
        queue.append((nrow, ncol)) #이동된 위치를 큐에 삽입
  
  return graph[n-1][m-1] #가장 오른쪽 아래의 노드까지의 방문 횟수

print(bfs(0, 0)) #시작 위치로 bfs 호출