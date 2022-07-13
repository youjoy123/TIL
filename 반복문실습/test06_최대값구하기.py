#최댓값 구하기
numbers = [0, 20, 100, 40]
max_num = 0
#1.반복
for n in numbers:
    print(n)
    #2. 만약, max 값이 n보다 작으면 바꾼다.
    if max_num < n:
        print()
        mab_num = n
print(max_num)