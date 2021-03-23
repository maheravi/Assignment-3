import random

List = set()

num = int(input("Number of array : "))

i = 0

while i < num:
    n = random.randint(0, 100)
    if n not in List:
        i += 1
        List.add(n)

print(List)