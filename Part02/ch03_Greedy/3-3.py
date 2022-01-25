#숫자 카드 게임
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data) #입력 행에서 가장 작은 수
    if min_value > result:
        result = min_value
    # result = max(result, min_value)

print(result)
