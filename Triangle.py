height = int(input("Enter the height of the triangle (number of rows): "))
print("Right triangle pattern: ")

i = 1
for i in range(1, height + 1):
    for j in range(i):
        print("*", end="")
    print()
