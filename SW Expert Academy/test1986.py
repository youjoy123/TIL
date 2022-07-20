# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    
    ans = 0
    
    for i in range(1, num+1):
        if i%2:				# 홀수라면
            ans = ans + i
        else:				# 짝수라면
            ans = ans - i
    print('#{} {}'.format(tc, ans))