#아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다. 오류 찾아 수정하시오.

from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count = {fruit: 1}
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)

# fruit_count = {fruit: 1} 를 사용했을 경우, 반복문이 돌아갈때마다 기존의
# value를 replace하게된다. 결국 fruits의 마지막 value만 fruits_count에 저장된다
# fruit_count[fruit] = 1 를 사용하면 새로운 fruits가 생길때마다 기존에 + 된다

from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)