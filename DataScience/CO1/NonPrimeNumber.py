print("21MCA033-Nimisha Tony")

n = int(input("Enter the limit:"))
for i in range(1, n):
    for j in range(2, i):
        if i % j == 0:
            print(i)
            break
