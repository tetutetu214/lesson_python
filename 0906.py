i = int(input())
num = [int(x) for x in input().split()]
add = 0
for i in num:
  if i > 0:
    add += 1
print(add)