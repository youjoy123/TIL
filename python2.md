22.7.12

## python 

#### 제어문

- 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행.

- 제어문은 순서도  flow chart로 표현이 가능



조건문의 기본? 참/거짓을 판단할 수 있는 조건식과 함께 사용

```python
a = 10
if a>=0
	print('양수')
else :
	print('음수')
print(a)
```

==>출력

양수

10

```python
# 1. num은 input으로 사용자에게 입력을 받으세요
num = int(input())
# print(num, type(num))
# 2. 조건문을 통해ㅓ 홀수/짝수 여부를 출력하세요
# int를 사용하여 숫자로서의 num (input 입력값이 문자열이라서 형변환해줘야됨)
if num % 2 == 1 :
    print('홀수')
else :
    print('짝수')
```



#### 복수 조건문

복수의 조건식을 활용할 경우 elif를 활용하여 표현

(else if의 줄임말,,)

```python
#실습문제 실습
dust=int(input())
if dust<=30 and dust>0
    : print('좋음')
elif dust<=80 and dust>30
    : print('보통')
elif dust<=150 and dust>80
    : print('나쁨')
else dus1t<=151 and dust>150
    : print('매우나쁨')


# else는 위의 모든 조건에 해당하지 않는 나머지의 경우이기에 별도의 조건은 불가능하다
# 조건문에서 else는 생략이 가능하다
#모범답안
dust = 80
if dust >150 :
    print('매우나쁨')
elif dust > 80 :
    print('나쁨')
elif dust >30 :
    print('보통')
else:
    print('좋음')
print('미세먼지 확인 완료')
```



#### 중첩조건문

```python
dust = 80
if dust >150 :
    print('매우나쁨')
elif dust > 80 :
    print('나쁨')
elif dust >30 :
    print('보통')
else:
    if dust < 0 :
        print('음수 값입니다.')
    else :
        print('좋음')
print('미세먼지 확인 완료')
```

중첩조건문은 꼭 마지막 else에만 하는 것인 아니고

```python
dust = 1000
if dust >150 :
    if dust > 300 :
        print('실외활동을 자제하세요')
    print('매우나쁨')
elif dust > 80 :
    print('나쁨')
elif dust >30 :
    print('보통')
else:
    print('좋음')
print('미세먼지 확인 완료')
```

위와 같이 if문에도 가능하다.





#### 조건표현식

조건표현식이란? 조건 표현식을 일반적으로 조건에 따라 값을 할당 할 때 활용

**<true인 경우 값> if <expression>else<false인 경우 값>**

num이 정수일때,아래의 코드는 무엇을 위한 코드?

Q. 실습문제 == 절대값을 계산하기 위한 코드였다...

value = num if num >=0 else -num

![image-20220712102748047](python2.assets/image-20220712102748047.png)



#### 반복문

* 반복문의 종류 <while vs for : 종료조건이 다르다!>                                                                                                                                                                         

  - while 문 : 조건이 참인 경우 반복적으로 코드를 실행, 무한루프를 하지 않도록 종료조건이 필요

  ```python
  a=0
  while a < 5 : #종료조건
      print(a)
      a += 1 #a=a+1 
  print('끝')
  #5번출력됨. 
  ```

  ```python
  ```

  

  - for 문 : 반복가능한 객체를 모두 순회하면 종료(별도로 종료조건이 필요없음)

​							 for문은 시퀀스를 포함한 순회가능한 매체

​		#for<변수명>in<반복가능한>:Code block

```python
#for<변수명>in<iterable>:Code block

for fruit in['apple', 'mango', 'banana']
	print(fruit)
print('끝')
#apple, mango, banana 출력
```

```python
#문자열 순회 : 사용자가 입력한 문자를 한글자씩 세로로 출력하시오
chars=input() ===> hi
for char in chars :
    print(chars)====>h
    				 i
#range를 이용한 문자열 순회

#딕셔너리순회:딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용
grades = {'john':80, 'eric':90}
for name in grades :
    print(name) ===> john,eric 출력
grades = {'john':80, 'eric':90}
for name in grades :
    print(name, grade[name]) ===> john 80, eric 90 출력
```



#### 반복문 제어

- break : 반복문을 종료

```python
#예시문
n=0
while True:
    if n ==3:
        break
    print(n)
    n +=1 ===> 0 1 2 출력

#예시문2
for i in range(10):
    if i>1:
        print('0과1만 필요해!')
        beak
    print(i) ===> 0, 1, 0과 1만 필요해! 출력
```



- continue : cotinue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

```python
for i in tange(6):
    if i%2 == 0 :
        continue
    print(i) ===> 1 3 5 출력(0,2,4는 true 다음 출력으로 넘어가는것)
```



- for-else : 끝까지 반복문을 실행한 이후에 else문 실행

  ​				break을 통해 중간에 종료되는 경우 else문은 실행되지 않음

```python
for char in 'apple':
    if char == 'b'
    	print('b!')
        break
else:
    print('b가 없습니다.') => b가 없습니다. 출력
```



![image-20220712115812976](python2.assets/image-20220712115812976.png)