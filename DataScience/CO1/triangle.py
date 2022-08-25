#21MCA033
#3. Given sides of a triangle, write a program to check whether given triangle is an isosceles, equilateral or scalene.

n1=int(input("Enter the first side of triangle:"))
n2=int(input("Enter the second side of the triangle:"))
n3=int(input("Enter the third side of the triangle:"))
if(n1==n2==n3):
    print("triangle is equilateral")
elif (n1 == n2 != n3) | (n1 != n2 == n3) | (n1 != n3 == n2):
    print("triangle is isosceles")
else:
    print("triangle is scalar")