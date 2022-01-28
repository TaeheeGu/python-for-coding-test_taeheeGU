#반복을 이용한 팩토리얼 연산
def factorial_iterative(n):
  result = 1
  for i in range(1, n+1):
    result *= i
  return result

#재귀 함수를 이용한 팩토리얼 연산
def factorial_recursive(n):
  if n <= 1: #종료 조건
    return 1
  return n*factorial_recursive(n-1)

print(factorial_iterative(5))
print(factorial_recursive(5))