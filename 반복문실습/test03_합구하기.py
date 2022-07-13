# 1~N까지의 합, 숫자의 나열 range 응용이 가능하다.
# 1) while 문
n = 0
result = 0
user_input = int(input())

while n <= user_input :         # n이 user_input 값보다 작거나 같을 때까지
    result += n                 # n을 result와 계속 더해주고
    n += 1                      # n은 1씩 증가한다

print(result)

# 2) for 문
n=0
result=0 
user_input = int(input())

for a in user_input:
    n+=1 #word 단어한글자씩 들어갈때마다 1씩 카운트하여 더해준다는 의미 1+1+1+1+1+1=6
print(result)