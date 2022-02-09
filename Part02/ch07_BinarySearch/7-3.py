#떡볶이 떡 만들기
import sys

n, m = map(int, sys.stdin.readline().split()) #떡의 개수 n, 요청한 떡의 길이 m
array = list(map(int, sys.stdin.readline().split())) #현재 떡의 개별 높이

#이진 탐색을 이용한 파라메트릭 서치
start = 0
end = max(array)
result = 0 #절단점

#이진 탐색(반복문)
while start <= end:
  mid = (start + end)//2
  total = 0 #잘린 떡의 길이

  for i in array:
    if i > mid:
      total += (i - mid) #짤린 떡의 총량
  
  #total == m 없어도 결과에 지장은 없지만 실질적인 연산 횟수를 줄이기 위해 사용
  if total == m: #떡이 양이 맞아 떨어지는 경우
    result = mid
    break #더 이상은 연산은 불필요

  elif total < m: #떡의 양이 부족한 경우 절단점을 왼쪽 부분으로
    end = mid - 1
  
  else: #떡의 양이 같거나 많은 경우
    result = mid #적어도 m이상이 되어야하기 때문에 결과를 저장
    start = mid + 1 #절단점을 오른쪽 부분으로

print(result)
