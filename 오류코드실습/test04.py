# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# words = list(map(int, input().split()))
# print(words)

# 원인 : 변수값은 문자열로 출력되기 때문에 int가 아닌 str로 수정해줘야한다.
words = list(map(str, input().split( )))
print(words)