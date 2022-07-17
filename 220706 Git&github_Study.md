*22.7.6 TIL(TODAY I LEARN)* 

# Git & Github 



## Git 개념정리

**Git이란? 분산 버전 관리 시스템** 

작업 진행시 작업물을 add하여 Staging area에 모아 Commit으로 버전기록을 하게 된다.

1. **working directory**

   파일의 변경사항

   -> add

2. **staging area** 버전으로 기록하기 위한 파일 변경사항의 목록

   : 워드나 엑셀 같은 오피서 문서 작업 중 갑자기 꺼지더라도 임시저장된 문서파일을 사용자에게 보여주는 것과 비슷한 개념? 

   -> commit

3. **repository** 커밋(버전)들이 기록되는곳 

   

![](https://git-scm.com/book/en/v2/images/areas.png)

Git은 파일을 modified, staged, committed로 관리 

• modified : 파일이 수정된 상태 (add 명령어를 통하여 staging area로) 

• staged : 수정한 파일을 곧 커밋할 것이라고 표시한 상태 (commit 명령어로 저장소) 

• committed : 커밋이 된 상태

> 출처 : https://git-scm.com/book/en/v2/images/areas.png



## Git 용어 정리

1. **저장소 처음 만들때**
   $ git init

2. **버전을 기록할 때**
   $ git add  .
   $ git commit -m '커밋메시지'

3. **상태 확인할 때**
   $ git status : 1통, 2통 : 상태
   * Git 저장소에 있는 파일의 상태를 확인하기 위하여 활용
     - Status로 확인할 수 있는 파일의 상태 
       • Tracked : 이전부터 버전으로 관리되고 있는 파일 
       • Unmodified : git status에 나타나지 않음 
       • Modified : Changes not staged for commit
       • Staged : Changes to be committed 
       • Untracked : 버전으로 관리된 적 없는 파일 (파일을 새로 만든 경우)

4.  **버전 확인할 때**

   $ git log : 커밋 확인 : 버전 

   - 현재 저장소에 기록된 커밋을 조회다양한 옵션을 통해 로그를 조회할 수 있음

​		$ git log -1 / $ git log --oneline / $ git log -2 --oneline



5. **디렉토리 관리**
   $ pwd : 현재 디레고리 출력
   $ cd 디렉토리이름 : 디렉토리 이동
   . : 현재디렉토리 / .. : 상위 디렉토리
   $ ls : 목록
   $ mkdir : 디렉토리 생성
   $ touch : 파일 생성
   $ rm 파일명 : 파일 삭제하기
   $ rm -r 폴더면 : 폴더삭제하기



## Git hub **원격저장소 활용 명령어**

**$ git push<원격저장소이름><브랜치이름> ::  *로컬 ---> 원격저장소***

​	• 원격 저장소로 로컬 저장소 변경 사항(커밋)을 올림(push) 
​	• 로컬 폴더의 파일/폴더가 아닌 저장소의 버전(커밋)이 올라감

**$ git pull<원격저장소이름><브랜치이름> ::  *원격저장소--->로컬***

​	• 원격 저장소로부터 변경된 내역을 받아와서 이력을 병합함

그 외) 

| 명령어                          | 내용                               |
| ------------------------------- | ---------------------------------- |
| git clone  <URL>                | 원격 저장소 복제                   |
| git remote -v                   | 원격저장소 정보확인                |
| got remote add<원격저장소><url> | 원격저장소 추가(일반적으로 origin) |
| git remote rm<원격저장소>       | 원격저장소 삭제                    |



### **github upload**
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

