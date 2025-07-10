#Write a program to find the roots of a quadratic equation ax^2 + bx + c.
#write a program to find roots of a quadratic equation without function
import cmath
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = (b**2) - (4*a*c)
sol1 = (-b + cmath.sqrt(d)) / (2 * a)
sol2 = (-b - cmath.sqrt(d)) / (2 * a)
print("The solutions are {0} and {1}".format(sol1, sol2))