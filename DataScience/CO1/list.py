#21MCA033
#9. Write a program to add elements of given 2 lists
l = int(input("Enter a limit for fist list"))
lst = []
print("Enter the elements:")
for i in range(l):
    number=input()
    lst.append(number)
lst2 = []
print("Enter the elements for 2nd list:")
for i in range(l):
    number=input()
    lst2.append(number)
s=0
for i in lst:
    s=s+int(i)
print("sum of 1st list elements= ", s)
s2=0
for i in lst2:
    s2=s2+int(i)
print("sum of 2nd list elements= ", s2)