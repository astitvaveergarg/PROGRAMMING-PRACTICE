first,second=0,1
num=int(input("Enter The No. For Fibonaccii Series : "))
def Fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
print("Fibonaccii Series is: \n")
for i in range(0,num):
    print(Fibonacci(i))