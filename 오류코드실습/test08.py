# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 

# word = "HappyHacking"
# count = 0
#for char in word:
#    if char == "a" or "e" or "i" or "o" or "u":
#        count += 1
#print(count)

# 원인 : 모음을 char로 하나씩 대응해 주지 않음. 위와 같이 할경우 조건문의 결과는 항상 참이 되어 해당 문자 수를 출력하게 됨 all 참.
#        따라서, 대칭으로하여금 매칭시켜 조건을 확실하게 걸어주어야 함.
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count += 1

print(count)