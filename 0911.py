N = int(input())
A = [int(x) for x in input().split()]
chk = A[0]
for i in A:
  if chk > i:
    chk = i
print(chk)