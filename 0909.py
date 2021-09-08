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