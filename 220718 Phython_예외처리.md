22.7.18  TIL 에러와 예외처리

#### 에러와 예외

1. 문법 에러(Syntax Error)
   
   • SyntaxError가 발생하면, 파이썬 프로그램은 실행이 되지 않음
   
   • 파일이름, 줄번호, ^ 문자를 통해 파이썬이 코드를 읽어 나갈 때(parser) 문제가
   발생한 위치를 표현
   
   • 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호(^)를 표시

2. 예외(Exception)

        • 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
        • 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
        • 실행 중에 감지되는 에러들을 예외(Exception)라고 부름
        • 예외는 여러 타입(type)으로 나타나고, 타입이 메시지의 일부로 출력됨
        • NameError, TypeError 등은 발생한 예외 타입의 종류(이름)
        • 모든 내장 예외는 Exception Class를 상속받아 이뤄짐
        • 사용자 정의 예외를 만들어 관리할 수 있음

        • 파이썬 내장 예외 (built-in-exceptions)

            ![](C:\Users\ehdgj\AppData\Roaming\marktext\images\2022-07-18-21-09-27-image.png)



#### 예외처리

try 문(statement) / except 절(clause)을 이용하여 예외 처리를 할 수 있음
**try문**
• 오류가 발생할 가능성이 있는 코드를 실행
• 예외가 발생되지 않으면, except 없이 실행 종료
**except 문**
• 예외가 발생하면, except 절이 실행
• 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함

```python
try :
    num = input('숫자입력 : ')
    print(int(num))
except:
    print('숫자가 아닙니다')
except ZeroDivisionError:    
    print('0으로 나눌 수 없습니다.')
```

• try : 코드를 실행함
• except :  try 문에서 예외가 발생 시 실행함
• else :  try 문에서 예외가 발생하지 않으면 실행함
• finally :  예외 발생 여부와 관계없이 항상 실행함 ex) print('파일 읽기를 종료합니다')



#### 예외발생시키기

raise를 통해 예외를 강제로 발생 :: raise <표현식> (메세지)

==> 표현식에서 예외 타입 지정, 주어지지 않을 경우 현재 스코프에서 활성화된 마지막 예외를 다시 일으킴
