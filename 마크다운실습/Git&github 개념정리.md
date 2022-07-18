**저장소 처음 만들때**
$ git init

**버전을 기록할 때**
$ git add  .
$ git commit -m '커밋메시지'

**상태 확인할 때**
$ git status : 1통, 2통 : 상태
$ git log : 커밋 확인 : 버전

**디렉토리 관리**
$ pwd : 현재 디레고리 출력
$ cd 디렉토리이름 : 디렉토리 이동
. : 현재디렉토리, .. : 상위 디렉토리
$ ls : 목록
$ mkdir : 디렉토리 생성
$ touch : 파일 생성
$ rm 파일명 : 파일 삭제하기
$ rm -r 폴더면 : 폴더삭제하기

**github upload**
$ git remote add origin http://github.com/youjoy123/test.git : 저장소 개설 (1회만 하여도 가능함) 

$ git push origin master : 실시간 업로드

```bash
307@DESKTOP-SLE8MK8 MINGW64 ~/Desktop/220706 (master)
$ git init
Reinitialized existing Git repository in C:/Users/ehdgj/Desktop/220706/.git/

307@DESKTOP-SLE8MK8 MINGW64 ~/Desktop/220706 (master)
$ git add .
warning: adding embedded git repository: gell
hint: You've added another git repository inside your current repository.
hint: Clones of the outer repository will not contain the contents of
hint: the embedded repository and will not know how to obtain it.
hint: If you meant to add a submodule, use:
hint:
hint:   git submodule add <url> gell
hint:
hint: If you added this path by mistake, you can remove it from the
hint: index with:
hint:
hint:   git rm --cached gell
hint:
hint: See "git help submodule" for more information.

307@DESKTOP-SLE8MK8 MINGW64 ~/Desktop/220706 (master)
$ git commit -m'test'
[master 05f2f75] test
 4 files changed, 1 insertion(+)
 create mode 160000 gell
 create mode 100644 gello
 create mode 100644 hello
 create mode 100644 world

307@DESKTOP-SLE8MK8 MINGW64 ~/Desktop/220706 (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
  (commit or discard the untracked or modified content in submodules)
        modified:   gell (modified content, untracked content)

no changes added to commit (use "git add" and/or "git commit -a")

307@DESKTOP-SLE8MK8 MINGW64 ~/Desktop/220706 (master)
$ git log
commit 05f2f7576cf040347b8b292ce2ec6309ccaf9743 (HEAD -> master)
Author: youjoy123 <limuj333@gmail.com>
Date:   Wed Jul 6 13:52:01 2022 +0900

    test

commit a9ae8deb4a039c1a906a756d65f89a8825c29d0d (origin/master)
Author: youjoy123 <limuj333@gmail.com>
Date:   Wed Jul 6 10:46:16 2022 +0900

    test

307@DESKTOP-SLE8MK8 MINGW64 ~/Desktop/220706 (master)
$ git remote add origin http://github.com/youjoy123/test.git
error: remote origin already exists.

307@DESKTOP-SLE8MK8 MINGW64 ~/Desktop/220706 (master)
$ git push test master
fatal: 'test' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

307@DESKTOP-SLE8MK8 MINGW64 ~/Desktop/220706 (master)
$ git push origin master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 311 bytes | 311.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/youjoy123/test.git
   a9ae8de..05f2f75  master -> master

307@DESKTOP-SLE8MK8 MINGW64 ~/Desktop/220706 (master)
$ git log
commit 05f2f7576cf040347b8b292ce2ec6309ccaf9743 (HEAD -> master, origin/master)
Author: youjoy123 <limuj333@gmail.com>
Date:   Wed Jul 6 13:52:01 2022 +0900

    test

commit a9ae8deb4a039c1a906a756d65f89a8825c29d0d
Author: youjoy123 <limuj333@gmail.com>
Date:   Wed Jul 6 10:46:16 2022 +0900

    test
```

