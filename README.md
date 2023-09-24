# GIT-DEMO
版本檢視
	git --version
  
建立基本資訊
-	git config --global user.name your name 
-	git config --global user.email your email 

git設定資訊
-	git config --list

切換目錄
-	cd 路徑

初始本地倉庫
-	git init (初始化)

檢視目前狀態
-	git status
-		untrack(未控管)

加入控管
-	git add <filename>
-		untrack->Added(加入)
-		added->midified(修改)
	
	三種狀態
-		u>a>m

	以文字檔為主
	
-	git add . 將所有未加入跟變動一次確認


修改後的確認
-	M->A(git add <filename>)

新增忽略檔案
-	.gitigore
-		*.jpg
-		.vscode/


恢復上一個動作
-	git checkout .

恢復刪除後的檔案
-	git restore <filename>

查找控管檔案
-	git ls-files -s

檢視object內容物
-	git cat-file -t sha-1
-		t (blob型態)
-		p (內容)

正式儲存至倉庫區
-	git commit -m "message"
-	           -am =>add+message
-	git commit --amend
-			合併上一次的commit
-			vim
-				i(insert文字編輯)
-				esc(切換回命令列)
-				:wq(寫入後離開)

檢視目前幾個commit
-	git log
-		q(強制離開)
-	git log --oneline
-		將每個commit(縮成一行檢視)


git cot-file -p commit-shal
-	git cot-file -p tree-shal


git rm -f <filename> 
-	檔案在暫存區
-		完整刪除
-	檔案在倉庫區
-		恢復
-		git restore --staged (暫存區)
-			git add(確認刪除)
-			git restore(恢復)

git rm --cached <file>
-	不論暫存或倉庫都回到工作目錄(不控管)




分支
-	master(預設)
-	git branch(分支列表)
-	git branch <branch-name>(新增分支)

git checkout <branch-name>(切換分支)
-		-b 直接切換
		git checkout -commit(shal)
			
		git checkout HEAD
			HEAD~X(移動到前X分支)
		


git merge(合併)
-	切換回master
	
	合併發生衝突
		選擇以哪個分支為主(current/incoming/both)
		git merge abort 取消合併

git branch -D <branch-name> 
 -        刪除分支


git reset
-	重置指令
-	git reset commit(shal)
-	git reset --soft commit(shal)
-	git reset --hard commit(shal)
-	反悔
-		git reset ORIG_HEAD 回復到上一個動作


git reflog
-	查找過往的commit紀錄
-		git reset commit(shal)


git checkout HEAD
-	HEAD~X(移動到前X分支)




vscode程式指令
-	ctrl+shift+p
-		搜尋default(改成cmb)

-	cls
 
-		清空terminal



github
-	加入遠端倉庫
-	git remote add origin https://github.com/j278355469/git-demo.git


git remote -v
	-	顯示目前倉庫








-echo "# git-demo" >> README.md

-git init

-git add README.md

-git commit -m "first commit"

-git branch -M main

-git remote add origin https://github.com/j278355469/

-git-demo.git

-git push -u origin main
