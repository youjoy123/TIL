# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 내가 시도 했던 풀이
# a, b = map(int, input().split(,))
# testcase = 0 
# for i in testcase:
#     if a>0 and b<10:
#         print(a+b, sep="/n")

#답안
T = int(input()) # 변수 T에 input함수를 이용하여 정수형 값을 입력받는다.
for i in range(T): # 반복문의 반복횟수를 변수 T에 저장한 값만큼 반복한다. T에서 입력받은 반복횟수 만큼 돌려준다 이해.
    A, B = map(int, input().split( )) # 변수 A,B에 input 함수를 이용하여 정수형 값을 입력 받은 뒤, split함수를 이용하여 " "기준으로 슬라이싱하여 각각 변수에 저장
    print(A + B) # A+B 더한값을 출력

#총평
#접근 자체는 거의 동일 했다 다만, 순서에 변수값 입력에 차이가 있었다. 그래도 접근을 가까이 했다는 점에 의의를 두자.