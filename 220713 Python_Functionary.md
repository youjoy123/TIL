22.7.13

#### 함수기초

함수의 정의 : 특정한 기능을 하는 코드의 조각, 특정명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요시에만 호출하여 간편히 사용

#### Functionary

```python
#정의
#1.def
#2.함수이름:add
#3.input:a,b
def add(a,b):
    #4.return:값을반환
    return a+b
#호출
print(add(5,10))
```

정의되지않는 함수는 에러라고 뜬다. 따라서 함수는 무조건 정의를 해야함.

```python
#내장함수 호출
print(sum[1,2,3])
#내장함수는 이미 내장된 값으로 사용할 수 있음
```

#### 함수의 결과값 output

return 함수는 결과값 하나만 리턴한다. 명시적인 리턴이 없는경우에도 none을 반환 

함수는 return과 동시에 실행이 종료  

```python
def minus_and_product(x,y):
    return x-y
    return x*y
minus_and_product(4,5)
===> 출력
```

리턴두줄로 return하는 경우는 마지막추가는 무시됨, 리턴문을 한번만 사용하면서 두 개 이상의 값을 반환하는 방법은 아래와 같이 튜플반환을 사용하는 것이다. 

```python
# 튜플 반환
def minus and product(x,y) :
    return x-y, x*y
minus_and_product(4,5)
===> 출력 (-1,20)
```



#### 함수 input

• Parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
• Argument : 함수를 호출 할 때, 넣어주는 값



#### 함수응용

**map(function, iterable)**

순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고, 그 결과를 map object로 반환

```python
words=map(int, input().split())
```