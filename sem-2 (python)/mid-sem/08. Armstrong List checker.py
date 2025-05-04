numbers = [153, 9474, 123, 9475, 370]
for num in numbers:
    print(f"{num} is {'an' if num == sum(int(d)**len(str(num)) for d in str(num)) else 'not an'} Armstrong number.")