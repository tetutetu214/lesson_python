N = int(input())
A = [int(x) for x in input().split()]

count = [0]*9
for x in A:
  count[x-1] += 1

for x in count:
  print(x)

N = int(input())
A = [int(x) for x in input().split()]
NUM = len(A)
count=[0]* NUM

for x in A:
  count[x-1] += 1

for x in count:
  print(x)