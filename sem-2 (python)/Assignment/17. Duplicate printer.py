def occourance_count(array):
    occourance = {}
    for i in array:
        if i in occourance:
            occourance[i] += 1
        else:
            occourance[i] = 1
    return occourance

tup = occourance_count((1,2,3,4,5,6,2,3,4,5))

for item in tup:
    if tup[item] != 1:
        print(f"{item} occoured {tup[item]} times")