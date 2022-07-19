number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count=0

for number in number_list:
    total += number
    count += 1 #들여쓰기를 통해 count +1 이 되도록 해야하며

print(total / count)