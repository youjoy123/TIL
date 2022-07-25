# 아래 코드는 리스트에서 최댓값을 구하는 코드입니다. 원인을 적고, 수정



# 원인 : max 함수 이름이 변수 이름으로 쓰여서 함수의 역할을 하지 못한다.
number_list = [1, 23, 9, 6, 91, 59, 29]
max1 = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max1 > max2 :
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max1 < max2 :
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")