#크루스칼 알고리즘

#특정 원소가 속한 집합(루트 노드) 찾기
def find_parent(parent, x):
  if parent[x] != x: #루트 노드가 아닌 경우
    parent[x] = find_parent(parent, parent[x]) #루트 노드를 찾을 때까지 재귀적 호출
  return parent[x]

#두 원소가 속한 집합을 합치기(union)
def union_parent(parent, a, b):
  root_a = find_parent(parent, a)
  root_b = find_parent(parent, b)
  if root_a > root_b:
    parent[root_a] = root_b
  else:
    parent[root_b] = root_a

#노드의 개수(v)와 간선(union 연산)의 개수(e) 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1) #부모 테이블 초기화

#모든 간선을 담을 리스트(edge)와 최종 비용을 담을 변수(result)
edges = []
result = 0

#부모 테이블에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
  parent[i] = i

#모든 간선에 대한 정보를 입력받기
for _ in range(e):
  a, b, cost = map(int, input().split()) #노드 a와 b 사이 비용 cost
  edges.append((a, b, cost))
  #edges.append((cost, a, b)) 비용순 정렬위해 첫 번째 원소를 비용으로 설정 가능

#간선을 비용순으로 정렬
edges.sort(key=lambda x : x[2])
#edges.sort()

#간선을 하나씩 확인하며
for edge in edges:
  a, b, cost = edge
  #사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b): #루트 노드가 같지 않은 경우
    union_parent(parent, a, b)
    result += cost

print(result)