# print("-" * 10)
# print(len("introduction"))
# a = "introduction"
# print(a[0])

# a = "abcdefghijklmnopqrstuvwxyz"
# # print(a[-1])

#コロンはX~Yまでの間を呼び出してくれる
# # print(a[10:20])
# print(a[14])
# print(a.find("opq"))
# print(a.find("opt"))

b = "Language:English"
i = b.find(":")
print(i)
#コロンの前までの全て
print(b[:i])
#コロンの後ろ全て
print(b[i:])
#コロンからの後ろ全て
print(b[i+1:])