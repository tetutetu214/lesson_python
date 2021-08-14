#csvファイルを開く
#構文としてwith open()as file:を利用する。（ファイル名、リード）
with open('student.csv', 'r')as f:
  student = {}
#CSVの中を全て読み込むという意味でのreadlines
  data = f.readlines()
  print(data)
#繰り返しを利用してデータを一行ずつ受け取り、一行ずつ表示する
  data = f.readlines()
  for line in data:
    print(line)
#繰り返しを利用して辞書型の要素に追加をする
#辞書型はシーケンス要素はないため、append利用出来ない
with open('student.csv', 'r')as f:
  student = {}
  data = f.readlines()
  for line in data:
    line = line.strip().split(",")
    name = line[0]
    score = int(line[1])
#このラインで受け取った値を2つに分けて、辞書へ
    student[name] = score
  print(student)

#この後半を利用して平均を求める方法を記載していきます

    student[name] = score
#valuesを利用してstudentの辞書にある値をsum(合計する)で、len（要素の数（生徒数））を表示していく
  average = sum(student.values()) / len(student)
  print(average)

#そして残酷ながら順番を出していきます
  average = sum(student.values()) / len(student)
#sortはリストで使用しているので、辞書型はsorted
#簡易なラムダ式を利用して、辞書型のキーのなかで[1]に該当するものを、reverse順で出力
  student = sorted(student.items(),key=lambda x: x[1], reverse=True)
  print(student)

#自分でも書きながら思うけど辞書オブジェクトの中では、values keys itemsを利用するみたい（詳しくはまだわかっていない）
avarage = sum(student.values()) / len(student)
student = sorted(student.item(), key=lambda x: x[1], reverse=True)
for s in student:
  print("名前: {}, 点数: {}".format(s[0],s[1]))