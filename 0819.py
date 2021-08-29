git code

#gitリポジトリを作成する
git init

#gitに変更するファイルをindexに追加する
#indexに事前登録してから、実際にコミットする（gitの絶対ルール）
git add . #こちらだと今いるディレクトリ全てが反映される
git add テキスト名

#上記はインデックス登録(ステージングという)のため、まだリポジトリに登録できていないので注意。次にコミットをする
git commit #ローカルリポジトリにコミット
#これだけだとviエディタが開かれる、一行目にコメントを入れる
git commit -m 'テキスト内容を追加しました'
#こちらのほうが面倒でない　

#履歴を確認できる
git log

git push   #ローカルをリモートへ反映する

git