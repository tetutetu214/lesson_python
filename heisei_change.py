# 西暦年から平成年を求める
import datetime
kotosi = datetime.date.today().year
print("さて今年は" + str(kotosi) + "年ですが、西暦を平成に直します。1989以上の数値を入力してください")
seireki = int(input())
if seireki >= 1989:
  print("あなたの調べたい西暦" + str(seireki) + "年は、", end="")
  heisei = seireki - 1988
  print("平成"+ str(heisei) + "年です")
else:
  print("そんな西暦ありません")