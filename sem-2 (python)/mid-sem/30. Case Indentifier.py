upperCount = 0
other = 0
lowerCount = 0
space = 0
text = input("Enter anything u don't worry about: ")
for i in text:
    if ord(i) >= 65 and ord(i) <= 90:
        upperCount += 1
    elif ord(i) >= 97 and ord(i) <= 122:
        lowerCount += 1
    elif i == " ":
        space += 1
    else:
        other += 1

print(f"It contained {upperCount} Uppercase, {lowerCount} lowercase, {space} spaces and {other} characters which are neither uppercase nor lowercase.")