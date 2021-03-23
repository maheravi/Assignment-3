n = int(input('Please Input Your Number: '))

p = len(str(n))

sum = 0

num = n
while num > 0:
   digit = num % 10
   sum += digit ** p
   num //= 10

if n == sum:
   print(n, "is an Armstrong number")
else:
   print(n, "is not an Armstrong number")