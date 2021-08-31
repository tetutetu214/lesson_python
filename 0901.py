# 2列の受け取り、リストの内容が同じかの確認
int = [input() for i in range(2)]
i = int.count(int[0])
if i == 2 :
    print("Yes")
else:
    print("No")

# 受け取ったものを逆から出力
int = [input() for i in range(3)]
print(int[2] + int[1] + int[0])

# リスト自体の中身を逆順にする。なのでこの状態にしたら一つずつ取り出すforつかえば出力できそう（これはやっていない）
int.reverse()
print(int)

# 部分的に表示する
s = input()
i = int(input())
print(s[i-1:i])