#1. 문제제공
numbers=[3,10,20]

#2.값 초기화
result=0 #0+3+1+20
count=0 #대괄호안에 있는 수 카운트

#3.반복
for numbers in numbers :
    result = result+numbers
    count = count+1
print(result/count)