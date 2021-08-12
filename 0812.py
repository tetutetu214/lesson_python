#配列をそのまま表示する
list = [1, 2, 3]
print(list)
#配列が逆順となる
list.reverse()
print(list)
#配列の最後に値を追加する
list.append(5)
print(list)
#配列の0番目（今回だと1）を消去
list.pop(0)
print(list)
#配列を小さい順から並び替える
list.sort()
print(list)
#配列の全てを消去する
list.clear()
print(list)

#配列から取得する際に4番目まで取得する
list = [1, 2, 3, 4, 5, 6, 7, 8,]
slice = list[:4]
print(slice)

#配列から取得する際に4番目以降を取得する（コロンの位置で書き分け）
slice = list[4:] 

#後ろから3までを取得する
list = [1, 2, 3, 4, 5, 6, 7, 8,]
slice = list[:-3]
print(slice)

#後ろから3つだけを取得する
list = [1, 2, 3, 4, 5, 6, 7, 8,]
slice = list[-3:]
print(slice)

#2つ飛ばしで取得する.この場合は1・3・5・7と表示される
list = [1, 2, 3, 4, 5, 6, 7, 8,]
slice = list[::2]
print(slice)

#reverseを利用しなくても後ろから表示することもできる
list = [1, 2, 3, 4, 5, 6, 7, 8,]
slice = list[::-1]
print(slice)

