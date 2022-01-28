n, m = map(int, input().split())
#방문 여부
visit = [[0]*m for _ in range(n)] #방문한 경우 1, 아직 가보지 않은 경우 0
#2차원 리스트의 초기화 방법, 리스트 컴프리헨션 문법

row, col, d = map(int, input().split())

visit[row][col] = 1 #시작위치는 방문체크

#게임 맵 정보 (0,0)부터 시작
game_map = []
for i in range(n):
  map_row = list(map(int, input().split()))
  game_map.append(map_row)
  #0은 육지, 1은 바다

count = 1 #방문한 칸 수
direction = [0, 1, 2, 3] #북, 동, 남, 서
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1] #북, 동, 남, 서로 이동 시 죄표 변화
first_direction = d #이동 이전의 최초의 방향

while True:
  d = (d + 3) % 4 #왼쪽으로 회전
  next_row = row + drow[d]
  next_col = col + dcol[d]

  if game_map[next_row][next_col] == 0 and visit[next_row][next_col] == 0: #이동이 가능한 경우
    visit[next_row][next_col] = 1
    row = next_row
    col = next_col
    first_direction = d #이동 후 기준 방향
    count += 1
    continue
  
  if first_direction == d: #최초 방향으로 회전할 때 까지 이동하지 못한 경우
    next_row = row - drow[d]
    next_col = col - dcol[d]
    if game_map[next_row][next_col] == 0:
      row = next_row
      col = next_col
    else:
      break

print(count)