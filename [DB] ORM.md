## 0824 KDT Class_note_down

### 학습 목표 : 데이터베이스 활용

#### 1. ORM(Object Relational Mapping)

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술

- 파이썬에서는 SQLAIchemy, peewee 등 라이브러리가 있으며, Django 프레임워크에서는 내장 Django ORM을 활용

- "객체(object)로 DB를 조작한다"
  
  ```
  Genre.objects.all()
  ```

- DB 조작(관리) 시 모델링 파트, 테이블 조작 파트가 따로 존재
  
  - 모델링 할 땐 class 생성, 테이블 조작 할 땐 Migration ⭐️
  - 참고) CRUD Operation은 객체를 조작하면서 작동
  - 모델 설계 및 반영
  
  ```
  - 1. 클래스를 생성하여 내가 원하는 DB의 구조를 만듦
  class Genre(models.Model):
      name = models.CharField(max_length = 30)
  
  - 2. 클래스의 내용으로 데이터베이스에 반영하기 위한 마이그레이션 파일을 '자동' 생성
  $ python manage.py makemigrations
  
  - 3. DB에 migrate
  $ python manage.py migrate
  ```
  
  > Migration(마이그레이션)
  > 
  > - Model에 생긴 변화를 DB에 반영하기 위한 방법
  > - 마이그레이션 파일을 만들어 DB 스키마를 반영
  > - 명령어
  >   - `makemigrations` : 마이그레이션 파일 생성
  >   - `migrate` : 마이그레이션을 DB에 반영
  
  - Migrate 살펴보기
  
  ```
  BEGIN;
  --
  -- Create model Genre
  -- 
  CREATE TABLE "db_genre" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(30 NOT NULL);
  COMMIT;
  
  -- cf) 트랜잭션
  ```

- 데이터베이스 조작(Database API)
  
  ```shell
  Genre.         objects.     all()
  #Class Name    #MANAGER     #QuerySet API
  ```

#### 2. ORM 기본 조작

- Create
  
  ```
  # 1. create 메서드 활용
  Genre.objects.create(name = '발라드')
  
  # 2. 인스턴스 조작
  genre = Genre()
  genre.name = '인디밴드'
  genre.save()
  ```
  
  **✏️ `Get`과 `Filter`의 차이** ⭐️
  
  ```python
  In [14]: Genre.objects.get(id=1)
  Out[14]: <Genre: Genre object (1)>
  -> 반드시 하나. 없거나, 많으면 오류 띄움
  -> PK : PRIMARY KEY 사용은 get 사용
  
  In [15]: Genre.objects.filter(id=1)
  Out[15]: <QuerySet [<Genre: Genre object (1)>]>
  -> 무조건 결과가 QuerySet(일종의 리스트)
  ```

- Read
  
  ```python
  # 1. 전체 데이터 조회
  Genre.objects.all()
  # <QuerySet [<Genre: Genre object (1)>, <Genre: Genre object (2)>, <Genre: Genre object (3)>]>
  
  # 2. 일부 데이터 조회(get)
  Genre.objects.get(id=1)
  # <Genre: Genre object (1)>
  
  # 3. 일부 데이터 조회(filter)
  Genre.objects.filter(id=1)
  # <QuerySet [<Genre: Genre object (1)>]>
  ```

- Update
  
  ```python
  # Create는 처음부터 새로 만드는 것, Update는 기존 테이블을 가져와서 수정하는 것
  
  # 1. genre 객체 활용
  genre = Genre.objects.get(id=1)
  
  # 2. genre 객체 속성 변경
  genre.name = '트로트'
  
  # 3. genre 객체 저장
  genre.save()
  ```

- Delete
  
  ```python
  # 1. genre 객체 활용
  genre = Genre.objects.get(id=1)
  
  # 2. genre 객체 삭제
  genre.delete()
  
  # 이렇게도 사용 가능
  Genre.objects.get(id=1).delete()
  # 파이썬에서 '  abc  '.strip().upper() 같은 느낌으로 작동
  ```

- Artist 모델 생성
  
  ```python
  class Artist(models.Model);    name = models.CharField(max_length=30)  debut = models.DateField()
  ```

✏️ **꿈에서도 잊지 말자, 마이그레이션!!!**

- 마이그레이션 파일 생성 ➡️ 마이그레이션을 DB에 반영
  
  ```python
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```
