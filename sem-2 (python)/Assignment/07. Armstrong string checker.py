def is_armstrong_string(s):
    try:
        return (n := int(s)) == sum(int(d) ** len(s) for d in s)
    except (ValueError, TypeError):
        return False

def main():
    s = input("Enter a string: ")
    print(f"'{s}' is {'an Armstrong' if is_armstrong_string(s) else 'not an Armstrong'} string.")

if __name__ == "__main__":
    main()