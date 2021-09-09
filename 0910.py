N = int(input())
A = [int(x) for x in input().split()]
count = 0
for i in range(1,N):
  if A[i-1] < A[i]:
    count += 1
print(count)