a, b = map(int, input().split)
num = [int(x) for x in input().split()]

pos = -1
for i in range(a):
    if num[i] == b:
      pos = i
print(pos)