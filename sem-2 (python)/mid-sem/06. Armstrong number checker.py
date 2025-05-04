def is_armstrong(n): 
    return n == sum(int(d) ** len(str(n)) for d in str(n))

def main(): 
    print(f"{(num := int(input('Enter a number: ')))} is {'an Armstrong' if is_armstrong(num) else 'not an Armstrong'} number.")

if __name__ == "__main__": 
    main()
