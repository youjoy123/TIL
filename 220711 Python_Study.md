## 파이썬

### 파이썬 개발 환경

파이썬은 객체 지향 프로그래밍으로, 모든 것이 객체로 구현되어 있음 

• 객체(object) : 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것

### 파이썬 기본 자료형

* 불린형(Boolean)
  
  - True/False값을 가진 타입은 bool
  
  - 비교/논리 연산을 수행함에 있어서 활용됨
  
  - bool()함수 : 특정 데이터가 true인지 false인지 검증 (and, or, not)
- 수치형
  
  - int 정수, float 실수, complex 복소수
3. 산술연산자
   
   - 기본적인 사칙 연산외
     - 나머지%, 나눗셈 /, 몫 //, ** 거듭제곱
     - <,<=,>,>=,==,!=

4. 문자열

모든 문자는 str타입, 보통 작은따옴표로 표기

- 중첩따옴표::중첩사용시 ''큰범주 ""작은범주 사용으로 가능, 반대도 ok

- 삼중따옴표까지도 가능, 이때는 하나로 정해서 사용 ''로 보통 사용한다

- 컴퓨터에서는 숫자를0부터 센다

- 인덱싱

fruit = 'apple'

**접근/인덱싱**

print(fruit[1]) => 출력값 p

=>컴퓨터에서는 숫자를 0 부터 셈

**슬라이싱**

print(fruit[1:3]) => 출력값 pp => 인덱스 1 이상, 3미만

print([5:2:-1])

print[:3] 처음부터3미만

print[5:] 5부터끝까지

print[::] 처음부터 끝까지 즉, 그대로 출력

print[::-1]  거꾸로출력

**마지막값은?**

파이썬은 음의 인덱스도 가지고 있다!  따라서 print(fruit[-1]) 가능

**문자열안에 변수 넣기**

- 문자열은 문자끼리만 합칠 수 있다!

- 타입이 매우 중요!
  
  ex) score = 100  print(f '내 점수는' {score}이야.')

```python
name = 'kim'
score = 4.5

# %-formatting 변수 단순 삽
print('Hello, %s'% name) # Hello, kim
print('내 성적은 %d'% score) # 내 성적은 4
print('내 성적은 %d'% score) # 내 성적은 4.500000 


# f-string 변수를 활용한 문장구성
name = 'Kim'
score = 4.5
print(f'Hello, {name}! 성적은 {score}') # Hello, Kim! 성적은 4.5
```

#### 형변환

파이썬에서 데이터형태는 서로 변환할 수 있음

#### 리스트(컨테이너 유형)

student = ['동현', '효근', '예지'...]

print(student[0]) => 동현 출력

print(student[-1]) => 예지 출력

#딕셔너리 : 키-값의 쌍

students = {'1회차' : ['동현','효근'], '2회차' : ['수경','나영'], '3회차' :['다경','예지']}

따라서 키값으로 접근함

print(students['1회차']) => 출력값 '동현', '효근'

* 리스트 

```python
# 값 추가는 .append()를 활용하여 추가하고자하는 값을 전달
even_numbers = [2, 4, 6, 8]
even_numbers.append(10)
even numbers => [2,4,6,8,10]

# 값 삭제는 .pop()을 활용하여 삭젷고자 하는 인덱스를 전달
even_numbers = [2, 4, 6, 8]
even_numbers.pop(0)
even_numbers => [4,6,8]

#예제
boxes = ['apple', 'banana']
len(boxes) #2
boxes[1] #b
```

- 튜플 : 불변한 값들의 나열, 순서를 가지며 서로 다른타입의 요소를 가짐

- 레인지 range

```python
range(4)
# range(0,4)
list(range(4))
# [0,1,2,3]
```

- set

set_a={1,2,3,4,5}

set_b={'hi', 1, 2}

print(set_a) => {1,2,3} 출력

print(set_b)=>{1,2,'hi'}출력



#내부적으로 '표현'만 똑같이 하는 방법이 있을 뿐 순서는 없다

#set과 dict은 아예 다른 자료구조

*셋의 활용:다른 컨테이너에서 중복된 값을 쉽게 제거할 수 있음=>중복제거