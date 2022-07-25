# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# N = 10
# answer = ()
# for number in range(N + 1):
#    answer.append(number * 2)

# print(answer)

# 원인 : ()는 튜플 형태이므로, append처럼 값을 추가하거나 삭제할 수 없다. 따라서 튜플이 아닌 리스트로 바꿔주기 위해 () => [] 수정
#       **리스트로까지의 접근까지는 좋았으나, ()가 튜플이고 []가 리스트임을 인지하지 못함. 이건 정보의문제. 접근은 좋았다. GOOD
N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)