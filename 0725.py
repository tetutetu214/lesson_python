# 1列の数値を受け取る
a,b,c = map(int, input().split())  # 3個の数字の入力を受け取る
print(a,b,c)  

# リスト（配列）を作成して、appendで追加する
# listのmapで配列リストの中の数値を変化させる（ここでは全てをappendする）
num_list = []
for i in range(5):
    num_list.append(list(map(int,input().split())))
print(num_list) 


