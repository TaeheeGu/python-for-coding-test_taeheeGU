#왕실의 나이트
point = input()

count = 0

row = int(point[1])
col = ord(point[0]) - ord('a') + 1 #문자의 유니코드 정수값 ord 사용

moves = [(2, 1), (2, -1), (-2, 1), (-2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)] #나이트가 움직일 수 있는 경우의 수

for move in moves:
  move_row = row + move[0] #나이트의 다음 행
  move_col = col + move[1] #나이트의 다음 열
  if (move_row >= 1 and move_row <= 8) and  (move_col >= 1 and move_col <= 8): #나이드의 이동 가능 여부
    count += 1



print(count)