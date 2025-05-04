from random import randrange
def is_prime(number):
    for i in range(number-1,1,-1):
        if number <3 and number > 0:
            return 1
        if number % i == 0:
            return 0 
    return 1

count = 0
x = int(input("How many prime numbers do you want? "))
while(count != x):
    a  = randrange(99) #It does not make sense printing a hundred values... no one would do that! right?
    if is_prime(a):
        count += 1
        print(a)
    