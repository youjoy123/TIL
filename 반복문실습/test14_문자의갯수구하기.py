#문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.

word=str(input())
count=0
for i in word :    
    if i == 'a' :
        count+=1
print(count) 