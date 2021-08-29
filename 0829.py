num = int(input())*2
print(num)

num = int(input()) % 5
print(num)

int = input()
print(int*3)

受け取った文字の部分だけ出力する
str = input()
print(str[2])

time = int(input())
num = 24 - time
print(num)

#方法1 受け取りの値が複数で決まっていない
num = [int(x) for x in input().split()]
print(max(num))

#方法2 受け取りの値が決まっている（今回2つ）
a, b = map(int, input().split())
if a > b:
  print(a)
else:
  print(b)