#바닥 공사
n = int(input()) #가로 1 <= n <= 1,000
k = 2 #세로

result = [0] * n+1 #경우의 수

result[1] = 1
result[2] = 3
for i in range(3, n+1):
  result[i] = (result[i-1]+2 + 2*result[i-2]) % 796796

print(result[n])