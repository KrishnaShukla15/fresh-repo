#program to find factorial of a given number
n=int(input("Enter any number: "))
r=1
for i in range(1,n+1):
    r*=i
print("Factorial of ",n,"is ",r)
