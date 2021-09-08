a, b = map(int, input().split())
num = [int(x) for x in input().split()]

pos = -1
for i in range(a):
    if num[i] == b:
      pos = i
print(pos)
# add = 1
# for i in num:
#   if i == b:
#     add += 1
# print(add)

# if add == 1:	
#   print("-1")

a,b = map(int, input().split())
num = [int(x) for x in input().split()]
chk = -1
for i in range(a):
  if num[i] == b:
    chk = i
print(chk)

a = int(input())
num = [int(x) for x in input().split()]
count = 0
for i in range(1,a):
	if num[i-1] < num[i]:
		count +=1
print(count)

N = int(input())
A = [int(x) for x in input().split()]
count = 0
for i in range(1,N):
    if A[i-1] < A[i]:
			count += 1
print(count)
  