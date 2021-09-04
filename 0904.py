#文字を受け取り全てを一つにJoinして合計を求める
n = int(input())
st = [input() for x in range(n)]
result = "".join(st)
print(len(result))

#リストで多い方を出力する
n = int(input())
st = [input() for i in range(n)]
le = st.count('left')
ri = st.count("right")
if le > ri:
  print("left")
else:
  print("right")