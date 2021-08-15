#単純なじゃんけんゲームを作成していく
#enum(列挙型＝イーナム)とは3つ以上選択肢のあるフラグを表現

form enum import Enum

class JankenHand(Enum)
    ROCK = 0
    SCISSORS = 1
    PAPER = 2
#
def __str__(self):
