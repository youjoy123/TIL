# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

# numbers=input()
# print(len(input()))


number = 123
if number == 0: 
    digit = 1
else:
    digit = 0
    while number > 0:
        number //= 10
        digit += 1
print(digit)

# number = 0인 경우 자릿수 1
# number > 0인 경우, 0이 될 때까지 10으로 나눠주면서 자릿수 +1