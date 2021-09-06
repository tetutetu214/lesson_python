#右と左の文字をn回受け取り、多い方を出力する
n = int(input())
st = [input() for i in range(n)]
le = st.count('left')
ri = st.count('right')
if le > ri:
  print('left')
elif le < ri:
  print('right')
else:
  print('same')

#数字を受ける、リストの中にbの値があれば”Yes”
a,b = map(int, input().split())
num = [int(x) for x in input().split()]
if b in num:
    print("Yes")
else:
    print("No")

#値を受けとり、リストの中にbの値がいくつあるかカウントする
a, b = map(int,input().split())
num = [int(x) for x in input().split()]
print(num.count(b))