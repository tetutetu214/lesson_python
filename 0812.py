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

#ここからは辞書型{}苦手だったハッシュを利用していこう
#辞書ではappendを利用しなくても代入する事ができる
#なぜならシーケンス要素ではないからである
#シーケンスとは順番という意味で、配列は順番に意味があったが、
#{}辞書型には順番という概念はない。なのでappendを利用できないが正しい
profile = {"mail": "mail@xxx.xxx", "name": "Bob", "address": "Tokyo"}
profile["phone"] = "0120XXXXXX"
print(profile)

profile_number = profile["phone"]
print(profile_number)

#profileの辞書の中にあるKeyを出力する（左側の、mail,name,address,phone）
print(profile.key())
#profileの中にあるValueを出力する
print(profile.values())
#profileのitemsを利用するという意味（左をk、右をv）にして出力
#キー{}のなかに k が出力され、値も同様に出力される
for k,v in profile.items():
	print("キー: {}, 値:{}",format(k,v))

#辞書型の削除方法はpopではない、それもシーケンスではないからという理由
del profile["name"]
print(profile)

#配列リストを深ぼる
#for前の数式を行い、リストに反映するコード。ただの2倍にするだけど
list = [1, 2, 3, 4]
double = [x * 2 for x in list]
print(double)

#もっと進化させる
#2倍して、それが2で割り切れる場合の値をevenに代入する
#この場合は、doubleで[2,4,6,8]になっており、そこから2で割り切れるものを出力となるので[4,8]が出力される
list = [1, 2, 3, 4]
double = [x * 2 for x in list]
even = [x * 2 for x in list if x % 2 == 0]
#これはif文が一つのコードに含まれている
#xが2で割った際あまりの奇数であった場合は0を掛ける
#else でそれ以外（偶数）の場合は2を掛ける
odd = [x * 0 if x % 2 == 1 else x * 2 for x in list]
print(odd)



