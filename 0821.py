inamurateppei@mbp projects % mkdir myweb
inamurateppei@mbp projects % cd myweb
#gitで管理をするよという宣言　　作業ディレクトリ
inamurateppei@mbp myweb % git init

hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint: 	git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint: 	git branch -m <name>

Initialized empty Git repository in /Users/inamurateppei/projects/myweb/.git/


inamurateppei@mbp myweb % echo line1 > index.html
inamurateppei@mbp myweb % ls 
index.html
inamurateppei@mbp myweb % cat index.html
line1
inamurateppei@mbp myweb % ls -la
total 8
drwxr-xr-x    4 inamurateppei  staff   128  8 21 21:25 .
drwxr-xr-x  104 inamurateppei  staff  3328  8 21 21:23 ..
drwxr-xr-x    8 inamurateppei  staff   256  8 21 21:25 .git
-rw-r--r--    1 inamurateppei  staff     6  8 21 21:25 index.html

#git add ステージングエリア（インデックス）へ昇格
inamurateppei@mbp myweb % git add index.html
inamurateppei@mbp myweb % git log
fatal: your current branch 'master' does not have any commits yet
inamurateppei@mbp myweb % git commit -m "firstcommit"
[master (root-commit) f61bdd3] firstcommit
 1 file changed, 1 insertion(+)
 create mode 100644 index.html

#gitの情報を確認する
inamurateppei@mbp myweb % git log
commit f61bdd3575f701cb36b96317322532be60ebf113 (HEAD -> master)
Author: tetutetu214 <lemoned.i.scream.art.of.noise@gmail.com>
Date:   Sat Aug 21 21:27:22 2021 +0900

    firstcommit

#gitの情報を一行で表示するための方法
inamurateppei@mbp myweb % git log --oneline
f61bdd3 (HEAD -> master) firstcommit

#どこを変更しているかの確認
inamurateppei@mbp myweb % git log -p
commit f61bdd3575f701cb36b96317322532be60ebf113 (HEAD -> master)
Author: tetutetu214 <lemoned.i.scream.art.of.noise@gmail.com>
Date:   Sat Aug 21 21:27:22 2021 +0900

    firstcommit

diff --git a/index.html b/index.html
new file mode 100644
index 0000000..a29bdeb
--- /dev/null
+++ b/index.html
@@ -0,0 +1 @@
+line1

#どこのファイルが変更されているかの確認
inamurateppei@mbp myweb % git log --stat
commit f61bdd3575f701cb36b96317322532be60ebf113 (HEAD -> master)
Author: tetutetu214 <lemoned.i.scream.art.of.noise@gmail.com>
Date:   Sat Aug 21 21:27:22 2021 +0900

    firstcommit

 index.html | 1 +
 1 file changed, 1 insertion(+)
inamurateppei@mbp myweb %

#vimでhtmlを編集したけれども、削除したい場合の流れ
inamurateppei@mbp myweb % vim index.html
#変更した状態を確認する 
inamurateppei@mbp myweb % git status
On branch master
Changes not staged for commit:
#modified=変更　が表示され、次にaddなのか、restore消去なのか表示してくれる
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")
#今回は消去したいので、restoreを選択してみました
inamurateppei@mbp myweb % git restore index.html
inamurateppei@mbp myweb % cat index.html
line1
inamurateppei@mbp myweb %