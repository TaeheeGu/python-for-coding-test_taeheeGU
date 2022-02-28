#팀 결성

import sys

input = sys.stdin.readline

n, m = map(int, input().split()) #학생 수 n, 합치기 연산 횟수 m

team = [0] * (n+1)

for i in range(n+1):
  team[i] = i #부모 테이블 초기화

def find_team(team, x): #같은 팀 여부 확인
  if team[x] != x: #루트 노드가 아닌 경우
    team[x] = find_team(team, team[x])
  return team[x]

def union_team(team, a, b):
  root_a = find_team(team, a)
  root_b = find_team(team, b)
  if root_a > root_b:
    team[root_a] = root_b
  else:
    team[root_b] = root_a

result = ''

for _ in range(m):
  check, a, b = map(int, input().split()) #연산종류 확인 check, 학생1 a, 학생2 b
  if check == 0: #팀 합치기 연산일 경우
    union_team(team, a, b)
  else: #같은 팀 여부 확인 연산일 경우
    if team[a] == team[b]: #같은 팀인 경우
      result += 'YES\n'
    else:
      result += 'NO\n'

print(result.rstrip())