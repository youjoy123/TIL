# 1. num은 input으로 사용자에게 입력을 받으세요
num = int(input())
# print(num, type(num))
# 2. 조건문을 통해ㅓ 홀수/짝수 여부를 출력하세요
# int를 사용하여 숫자로서의 num (​input 입력값이 문자열이라서 형변환해줘야됨)
if num % 2 == 1 :
    print('홀수')
else :
    print('짝수')