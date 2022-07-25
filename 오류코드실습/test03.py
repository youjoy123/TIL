# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# numbers = input().split()
# print(sum(numbers))

# 원인 : sum은 정수의 합계를 구하는 함수로, 변수값을 int로 매핑하여 설정해주어야한다.
numbers = map(int, input().split( ))
print(sum(numbers))