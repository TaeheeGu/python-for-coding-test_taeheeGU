#성적이 낮은 순서로 학생 출력하기
n = int(input())

array = []
for i in range(n):
  name, grade = input().split() #이름과 점수 입력
  array.append((name, int(grade))) #이름과 점수를 리스트에 추가, 점수는 int로

result = sorted(array, key=lambda x : x[1]) #점수(x[1])를 기준으로 정렬

for i in result: #정렬이 수행된 결과에서 이름을 출력
  print(i[0], end=' ')