# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

a = input()
result = 0
for digit in a :
    result+=int(digit)

print(result)