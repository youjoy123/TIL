# 아래 코드는 숫자의 길이를 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# number = 22020718
# print(len(number))

# 원인 : TypeError: object of type 'int' has no len() 
         # 해당 숫자가 정수로 잡혀 len함수를 이용할 수 없기에 따옴표 처리를 통해 문자열로 변환, 글자수 길이 코드 출력
number = '22020718'
print(len(number))