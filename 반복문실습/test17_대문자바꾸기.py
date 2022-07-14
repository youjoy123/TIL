# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오. .upper(), .swapcase() 사용 금지
# 풀이1
word=str(input())
result=''
for i in word :
    temp = ord(i)
    temp -= 32
    result +=chr(temp)
print(result)

# 풀이2
word=str(input())
for i in word:
    print(chr(ord(i)-32),end='') #end=''는 print함수로 문구를 출력하고, 마지막\n이 아닌 다른 값으로 설정할 수 있음. 또는 개행삭제
                                 #for A in B B에서 A에값을 하나씩 반환하는 것으로 출력시 개행처리되어 출력, 따라서 end=''로정리