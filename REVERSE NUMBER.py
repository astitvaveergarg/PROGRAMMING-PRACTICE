a=int(input("Enter The No.: "))
reversednumber=0
while a!=0:
    digit=a%10
    reversednumber=reversednumber*10+digit
    a=a//10
print("The Reversed No. Is ",reversednumber)
