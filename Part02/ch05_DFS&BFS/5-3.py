#음료수 얼려 먹기
n, m = map(int, input().split())

graph = []

for i in range(m):
  graph.append(list(map(int, input())))

def dfs(row, col): 
  if row < 0 or row >= n or col < 0 or col >= m: #주어진 범위를 벗어나는 경우 종료
    return False
  
  if graph[row][col] == 0: #아직 방문하지 않은 경우
    graph[row][col] = 1 #방문 여부 변경
    #현재 노드의 위치에서 재귀적으로 연결된 모든 지점 방문
    dfs(row-1, col) #상
    dfs(row+1, col) #하 
    dfs(row, col-1) #좌
    dfs(row, col+1) #우
    return True #연결된 구역의 존재 유무

  return False #모두 방문한 경우

result = 0

for i in range(n): #전체 노드에 대한 방문
  for j in range(m):
    if dfs(i, j) == True: #현재 위치에서의 dfs 호출
      result += 1

print(result)