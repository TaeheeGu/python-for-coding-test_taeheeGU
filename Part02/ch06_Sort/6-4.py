#두 배열의 원소 교체
n , k = map(int, input().split())
array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

array_A = sorted(array_A) #배열 A를 오름차순으로 정렬
array_B = sorted(array_B, reverse=True) #배열 B를 내림차순으로 정렬

for i in range(k): #바꿔치기 k번
  if array_A[i] < array_B[i]: #배열 A의 원소가 배열 B의 원소보다 작은 경우
    array_A[i] = array_B[i] #배열 A의 원소를 배열 B의 원소로 교체
  else: #배열 A의 값이 배열 B의 원소보다 클 경우 필요없다.
    break

print(sum(array_A))