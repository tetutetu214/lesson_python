#リスト＝配列を学び直す
player_1="勇者"
player_2="魔法使い"

print(player_1)
print(player_2)

team = ["勇者","魔法使い",100,player_1]
print(team)
print(team[0])
num = 1

#length を省略してlen で中身の数を表示できる
print(len(team))
team[2] = "まめ"
team[3] = "ため"
print(team)

team.pop(3)
print(team[0])

for i in team:
	print(i)

#変数で読み込む
#rstripで改行を削除している
line = input().rstrip()
print(line)
#配列で読み込む
#改行を削除した値を、[,]で分割してリストする
line = input().rstrip().split(",")
print(line)

#複数行（行数が不明の場合は）readlineを利用する
#これでは一行しか格納できない
line = input().rstrip()
print(line)

#ここから複数行
#何行も読み込むための、readlinesを呼び出すためのsystem standird in とう名称
import sys
for line in sys.stdin.readlines():
  print(line)

#今度は読み込んだ複数業をリストに追加するために
#appendは配列の中に取り組む
import sys
  array = []
    for line in sys.stdin.readlines():
			array.append(line.rstrip())
print(array)

# coding: utf-8
# 複数行のカンマ区切りデータを出力する

import sys
for line in sys.stdin.readlines():
	# ここに、文字列を分割して、出力するコードを書く
	enemy = line.rstrip().split(",")
	print(enemy[0] + "が" +enemy[1] + "匹現れた")