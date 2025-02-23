t1 = {1,4,7}
def multiplier(tuple):
    prod = 1
    for i in tuple:
        prod *= i
    return prod

print(multiplier(t1))