#효율적인 화폐 구성
n, m = map(int, input().split()) #1 <= n <= 100, 1 <= m <= 10,000

money = []

for i in range(n):
  money.append(int(input()))

d = [10001] * (m+1) #0 ~ m 까지, 화폐를 구성할 수 없는 경우 10001

d[0] = 0 #0원을 만드는 화폐의 개수는 0개

for i in range(n): #각각의 화폐
  for j in range(money[i], m+1): #각각의 화폐로 만들 수 있는 조합
    if d[j - money[i]] != 10001: #d[j - money[i]]원을 만드는 경우의 수가 존재하는 경우
      d[j] = min(d[j], d[j - money[i]] + 1)
      #기존의 값d[j]과 d[j - money[i]]원에서 money[i]를 더해 d[j]원을 만드는 경우를 비교

if d[m] == 10001:
  print(-1)
else:
  print(d[m])