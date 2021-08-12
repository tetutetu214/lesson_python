#ラムダ式（かんたんな関数のこと。何度も書くの面倒だからΛ（ラムダ）という記号を置いて省略の意味ね！から由来している。）
#公式としては"f = lambda x:"までで、x＝x＊2を代入している（代入が値でなくて式になっている）で、省略したfに2という数値を与えて計算する
f = lambda x: x * 2
print(f(2))

#ラムダ式に1、2を代入すると、a + bが発動する
f = lambda a,b: a + b
print(f(1,2))

#リストにも使用できる
f = lambda x: x[0]
list = [0, 1, 2, 3, 4]
print(f(list))

#numのリストを2倍する式
#list(map という形にすると、リストの形で数値を、今回はdoubleに入れ直してくれる
#fのラムダ式で、numのリストに適用した値を、list(mapを利用して、doubleに代入
f = lambda x: x * 2
num = [1, 2, 3, 4]
double = list(map(f, num))
print(double)

