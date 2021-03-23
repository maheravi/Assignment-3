n = int(input('Please Input Your Number: '))

num = n
while n > 1:
    for i in range(2, n+1):
        if n % i == 0:
            n /= i
        else:
            break
    if n == 1:
        print('yes,', num, 'is a factorial number')
    else:
        print('No,', num, 'is not a factorial number')
        break
