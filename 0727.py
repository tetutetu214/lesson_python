#array配列をつくる
array = []
#5回動作をする
for i in range(5):
#array配列に(int(input()))したものを追加する
  array.append(int(input()))
#array配列を引数で、1番小さいものを表示する
print(min(array))

#受け取った数値が同じであればOK
a=input()
b=input()
if a == b:
  print("OK")
else:
  print("NG")

array = []
for i in range(2):
  array.append(input())
if array[0] == array[1]:
  print("OK")
else:
  print("NG")