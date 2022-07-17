#문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요. 
#a 가 없는 경우에는 -1을 출력해주세요.

#풀이 1
word = str(input())
index = 0
for i in word:
    if i=='a':
        break  # a를 찾을때까지 index+=1 증가하다가, 만나면 break
    index += 1

if index>=len(word): #a의 위치가 단어의 길이보다 커지는 경우, 즉 a가 없는경우 '-1'을 프린트하고
    print(-1)
else:
    print(index)     #그외에는 상위 if문 index가 반영된 값을 프린트한다


#풀이2
word ='banana'
#문자로 순회하는 것이 아니라, 인덱스로 접근해서 쓰도록 하자.
for idx in range(len(word)) :
    if (idx,word[idx]) == 'a' :
        print(idx)
        is_a=true
        break
if not is a:
    print(-1)