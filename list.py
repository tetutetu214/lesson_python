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
print(team)