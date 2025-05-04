while 1:
    try:
        a = int(input("Enter a valid number: "))
        break
    except:
        continue

b = a
for i in range(b-1,1,-1):
    b*= i

print(f"\n{a}! = {b}\n")