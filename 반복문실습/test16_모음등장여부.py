# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u

word=str(input())
count=0
for i in word :
    if i == 'a':
        count+=1
    if i == 'e':
        count+=1
    if i == 'i':
        count+=1
    if i == 'o':
        count+=1
    if i == 'u':
        count+=1
print(count)

# print를 for구문에 맞춰 작성하여야지, 총 합의 count 출력값이 나오고
# if 구문과 맞출시 각 if문의 걸러져 값이 나오기 때문에 이점 주의를 해야한다.