#write a program to print a pyramid of numbers using loop
#Author: Reno Robert Roney
#Rollno: 32
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")  
    for j in range(i):
        print(i, end=" ")
    print()  
