str = input().rstrip()
if str == "Hello":
	print("こんにちは")
elif str == "Good morning":
	print("おはよう")
else:
	print("はじめまして")

num = int(input())
if num < 100:
	print(str(num) + "は100より小さい")
elif num < 200:
	print(str(num) + "は100以上200より小さい")
else:
	print(str(num) + "は200以上")

num = int(input())
if num <= 100:
	print(num)