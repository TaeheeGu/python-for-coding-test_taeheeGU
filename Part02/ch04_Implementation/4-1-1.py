#상하좌우
n = int(input()) #정사각형 크기
moves = input().split() #이동계획

row, col = 1, 1 #시작 위치 1행, 1열

direction = ['L', 'R', 'U', 'D'] #이동방향
drow = [0, 0, -1, 1] #이동방향에 따른 행의 변화
dcol = [-1, 1, 0, 0] #이동방향에 따른 열의 변화

for move in moves: #이동계획
  for i in range(len(direction)):
    if move == direction[i]: #이동계획에 따라 이동방향에 따른 행과 열의 변화
      nrow = row + drow[i]
      ncol = col + dcol[i]
  if nrow < 1 or nrow > n or ncol < 1 or ncol > n: #이동후 정사각형을 벗어나는 경우
    continue #이동 변화없이 다음 계획으로
  
  row, col = nrow, ncol #이동에 따른 행과 열의 변화

print(row, col)

