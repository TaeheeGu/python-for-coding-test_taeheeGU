#시각
n = int(input())

count = 0

#24*60*60 = 86,400 최대 연산횟수
#데이터 개수 100만개 이하일 때 완전 탐색 사용 가능
for hour in range(n+1): #시간
  for minute in range(60): #분
    for second in range(60): #초
      if '3' in str(hour) + str(minute) + str(second): #00시00분00초에 3포함 여부
        count += 1

print(count)