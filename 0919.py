print("アルファベットを入力してください")
print("アルファベットの入れ替えたい場所を入力してください")

S = input()
N,M=map(int, input().split())
S_list = list(S)
tmp = S_list[N-1]
S_list[N-1] = S_list[M-1]
S_list[M-1] = tmp
S = "".join(S_list)
pritn(S)