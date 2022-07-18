22.07.14

#### 데이터구조 및 메서드

**문자열탐색**

• .find(x) :  x의 첫 번째 위치를 반환. 없으면, -1을 반환함.

```python
print('apple'.find('p'))
===> 출력 1
print('apple'.find('k'))
===> 출력 -1
```

• .index(x) : x의 첫 번째 위치를 반환. 없으면, 오류 발생

```python
print('apple'.find('p'))
===> 출력 1
print('apple'.find('k'))
===> 오류
```

**문자열변경**

• .replace(old, new[,count]) : 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
                                                   count를 지정하면, 해당 개수만큼만 시행

```python
print('coone'.replace('o','a'))
===> 출력 caane
```

• .split(sep=None, maxsplit=-1) :  문자열을 특정한 단위로 나눠 리스트로 반환

-sep이 None이거나 지정되지 않으면 연속된 공백문자를 단일한 공백문자로 간주하고, 선행/후행 공백은빈 문자열에 포함시키지 않음.
-maxsplit이 -1인 경우에는 제한이 없음.

```python
print('a,b,c'.split('_'))
===> 출력 ['a,b,c']
print('a b c'.split())
===> 출력 ['a', 'b', 'c']
```

• .strip([chars]) : 특정한 문자들을 지정하면,
-양쪽을 제거하거나(strip), 왼쪽을 제거하거나(lstrip), 오른쪽을 제거(rstrip)
-문자열을 지정하지 않으면 공백을 제거함

• 'separator'.join([iterable]) :  반복가능한(iterable) 컨테이너 요소들을 separator(구분자)로 합쳐 문자열 반환,  iterable에 문자열이 아닌 값이 있으면 TypeError 발생

```python
print(''.join(['3','5']))
===> 출
```



### List

**list의 정의** : 변경가능한 값들의 나열된 자료형

순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음. 변경 가능하며 반복가능

대괄호 형태로 정의하며 요소는 콤마로 구분

**리스트 값 추가 및 삭제**

• .append(x) : 리스트에 값을 추가함

```python
cafe=['starbucks', 'tomntoms', 'hollys']
print(cafe)
# ['starbucks', 'tomntoms', 'hollys'] 출력

cafe.append('banapresso')
print(cafe)
# ['starbucks', 'tomntoms', 'hollys','banapresso'] 출력
```

• .extend(iterable) : 리스트에 iterable의 항목을 추가함

```python
cafe=['starbucks', 'tomntoms', 'hollys']
print(cafe)
# ['starbucks', 'tomntoms', 'hollys'] 출력

cafe.extend('banapresso',''test')
print(cafe)
# ['starbucks', 'tomntoms', 'hollys','banapresso','test'] 출력
```

• .insert(i, x) : 정해진 위치 i에 값을 추가함

```python
cafe=['starbucks', 'tomntoms', 'hollys']
print(cafe)
# ['starbucks', 'tomntoms', 'hollys'] 출력

cafe.insert('0',''start')
print(cafe)
# ['start',starbucks', 'tomntoms', 'hollys'] 출력
```

![image-20220714105850431](methods_study.assets/image-20220714105850431.png)

• .remove(x) : 리스트에서 값이 x인 것 삭제

• .pop(i)  :  정해진 위치 i에 있는 값을 삭제하고, 그 항목을 반환함  

                    -i가 지정되지 않으면, 마지막 항목을 삭제하고 반환함

```python
numbers = ['hi',1,2,3]
pop_number = numbers.pop()
print(pop_number) # 3
print(numbers) #['hi',1,2]
```

• .clear()  모든 항목을 삭제함

```python
numbers = [1,2,3]
print(numbers)
# [1,2,3]
print(numbers.clear())
# []
```

• .index(x) : x값을 찾아 해당 위치 값을 반환

```python
numbers = [1,2,3,4]
print(numbers) # [1,2,3,4]
print(numbers.index(3)) # [2]
```

• .count(x) : 원하는 값의 개수를 반환함

• .sort() : 원본 리스트를 정렬함. None 반환 /  sorted 함수와 비교할 것

```python
numbers = [3, 2, 5, 1]
result = numbers.sort()
print(numbers, result) # [1,2,3,5] None >> 원본변경 정렬


#Sorted 함수 이용시
numbers = [3, 2, 5, 1]
result = sorted(numbers)
print(numbers, result) # [3,2,5,1][1,2,3,5] >> 정렬된 리스트반환같이
```

• .reverse() : 순서를 반대로 뒤집음(정렬하는 것이 아님). None 반환.



### 컬렉션(순서가 없는 데이터구조)

#### 세트(set)

• 유일한 값들의 모음(collection)
• 순서가 없고 중복된 값이 없음.
• 수학에서의 집합과 동일한 구조를 가지며, 집합 연산도 가능
• 변경 가능하며(mutable), 반복 가능함(iterable)
• 단, 세트는 순서가 없어 반복의 결과가 정의한 순서와 다를 수 있음



#### 딕셔너러니(dictionary)

• 키-값(key-value) 쌍으로 이뤄진 모음(collection)
• 키(key) :  불변 자료형만 가능 (리스트, 딕셔너리 등은 불가능함)
• 값(values) : 어떠한 형태든 관계 없음
• 키와 값은 : 로 구분 됩니다. 개별 요소는 ,로 구분됩니다.
• 변경 가능하며(mutable), 반복 가능함(iterable)
• 딕셔너리는 반복하면 키가 반환됩니다.

```python
students = {'홍길동':30, '김철수':25}
students['홍길동'] # 30
```