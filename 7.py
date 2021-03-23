list = []

n = int(input("Enter number of array : "))

for i in range(0, n):
    array = int(input())

    list.append(array)  # adding the element

print(list)

fn = 0
i = 1
while i < len(list):
    if list[i] < list[i - 1]:
        fn = 1
    i += 1

if not fn:
    print("Yes, Your list is sorted.")
else:
    print("No, Your list is not sorted.")
