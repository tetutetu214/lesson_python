#外部からデータを入力する
#もともとUNIXの標準入力を指している

#文字として受け取り
# int = input()

#数値を数値として受け取る
# num = int(input())
# print(num)

#複数業を受け取る(受け取り個数が分かっている場合)
#.rstripは、改行の削除

count = int(input())
for i in range(count):
  line = input().rstrip()
  print(line)

