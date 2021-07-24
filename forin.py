#rangeを利用することで5までを表現している
#for XXX in 範囲 
# for i in range(5):
#   print("hello:" + str(i+1))

# この場合10未満という意味合い
# for i in range(5,10):
#   print("hello:" + str(i+1))


#Wileを利用してみよう
# 条件式の間繰り返せる（細かいことが設定できる）
# i = 1
# while i <= 5:
#   print(i)
#   i += 1

#適当RPG
# import random
# i = 1
# hp = 30
# while hp > 0:
#   damage = random.randint(1,10)
#   print(str(damage) + "のダメージを受けた")
#   hp -= damage
#   print("残りのHPは、" + str(hp) + "残っているぞ")
# print ("そして俺の冒険は終わった")

