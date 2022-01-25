#1이 될 때 까지
n, k = map(int, input().split())

count = 0

while True:
  if n == 1:
    break
  
  if n%k == 0:
    n = n//k
  else:
    n -= 1
  count += 1

print(count)

'''
while True:
  target = (n//k)*k   # n보다 작은 k로 나누어 떨어지는 수
  count += (n-target) # target이 될 때까지 -1의 횟수
  n = target

  if n < k: # n이 k보다 작으면 더 이상 나눌 수 없다
    break

  count += 1
  n //= k

count += (n-1) #마지막으로 남은 수에 대하여 1씩 빼기 
'''