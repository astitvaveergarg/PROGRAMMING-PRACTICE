num = input("Enter a number: ")
sum = 0
temp = int(num)

while temp > 0:
   digit = temp % 10
   sum += digit ** len(num)
   temp //= 10

num=int(num)
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")