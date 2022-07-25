#실습문제 실습
dust=int(input())
if dust<=30 and dust>0
    : print('좋음')
elif dust<=80 and dust>30
    : print('보통')
elif dust<=150 and dust>80
    : print('나쁨')
else dus1t<=151 and dust>150
    : print('매우나쁨')


# else는 위의 모든 조건에 해당하지 않는 나머지의 경우이기에 별도의 조건은 불가능하다
# 조건문에서 else는 생략이 가능하다
#모범답안
dust = 80
if dust >150 :
    print('매우나쁨')
elif dust > 80 :
    print('나쁨')
elif dust >30 :
    print('보통')
else:
    if dust < 0 :
        print('음수 값입니다.')
    else :
        print('좋음') #음수값은 좋음이 출력되며 안되기 때문에 else구문에 넣어놈
print('미세먼지 확인 완료')