word = 'banana'
dic = {}
for i in word:
    if i in dic:
        dic[i] += 1 #딕셔너리에 키가 있으면
    else :
        dic[i]= 1 #딕셔너리에 키가 없으면, 키링값을 1으로 초기화 한다
#출력부분
for i in dic:
    print(i,dic[i])

#b=key, b의개수가 value로 매칭하는 딕셔너리를 작성한다.