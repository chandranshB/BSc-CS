def count_vowels(s: str) -> int: return sum(1 for c in s if c.lower() in "aeiou")

def highlight_vowels(s: str) -> str: return ''.join(f"\033[32m{c}\033[0m" if c.lower() in "aeiou" else c for c in s)

if __name__ == "__main__":
    user_input = input("Enter your string: ")
    print(f"There are {count_vowels(user_input)} vowels in the input \"{highlight_vowels(user_input)}\"")
