#write a program that uses built-in functions to find the largest and smallest among three numbers
#Author: Reno Robert Roney
#Rollno: 32
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
largest = max(a, b, c)
smallest = min(a, b, c)
print("The largest number is:", largest)
print("The smallest number is:", smallest)