d1 = {}
print("Enter 'stop' stop inserting values")
while 69:
    key = input("Enter Key: ")
    if key == "stop":
        break
    value = input("Enter the value: ")
    if value == "stop":
        break
    else:
        d1[key] = value
print(d1)