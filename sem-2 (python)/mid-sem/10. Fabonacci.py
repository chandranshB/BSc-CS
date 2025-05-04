base = 0
secondary = 1

for i in range(int(input("Enter till how many numbers you want to print the fabonacci series: ")), -0, -1):
    if i == 1:
        print(base, end="")
    else:
        print(base, end=", ")
    temp = base
    base = secondary
    secondary += temp