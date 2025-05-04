def getOddKeys(dictionary):
    temp = []
    for i in dictionary:
        if dictionary[i] %2 != 0:
            temp.append(i)
    
    return temp

print(getOddKeys(dict(zip(range(10),range(10)))))