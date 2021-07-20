# coding: utf-8
# if文による条件分岐　elif文

# ランダムをインポートして機能をつかえるようにしている
import random 
# ランダムを利用する（今回は1〜3までの数値を表す）
print ("じゃんけんマシーンだよ")
print ("1：グー 2：チョキ 3：パー")
print ("じゃんけーん")
print ("1〜3までの数字を入れてください")
get = int(input())
number = random.randint(1,3)

if number == 1:
	print( "あなたの勝ち")	#条件式が成立したときの処理
elif number == 2:
  print("あなたの負け")
else:
	print( "あいこ")	#条件式が成立しなかったときの処理

