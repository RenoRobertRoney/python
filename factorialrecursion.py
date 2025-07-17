#write a function to find the factorial of a number using recursion
#Author: Reno Robert Roney
#Rollno: 32
def factorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * factorial(n - 1)  
n = int(input("Enter a number: "))
print(f"Factorial of" ,n, "is:", factorial(n))
