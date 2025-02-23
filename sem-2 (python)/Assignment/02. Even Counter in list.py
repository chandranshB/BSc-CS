def is_valid_integer(value: str) -> bool: return value.isdigit() or (value.startswith('-') and value[1:].isdigit())

def get_numbers(count: int) -> list:
    numbers = []
    while len(numbers) < count:
        value = input(f"Enter element {len(numbers) + 1}/{count}: ").strip()
        if not value: print("Input cannot be empty."); continue
        if value == 'navigate':
            try: pos = int(input("Position to correct: ")) - 1; numbers[pos] = int(input("Correct value: "))
            except: print("Invalid position or value!")
        elif is_valid_integer(value): numbers.append(int(value))
        else: print("Enter a valid integer.")
    return numbers

if __name__ == "__main__":
    try:
        n = int(input("Number of elements: ").strip())
        elements = get_numbers(n)
        print(f"\nYou entered {len(elements)} numbers, of which {sum(1 for x in elements if x % 2 == 0)} are even.")
    except ValueError: print("Invalid input for number of elements!")