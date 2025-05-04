lst = input("Enter elements of the list separated by spaces: ").split()
print(f"The list {lst} is a palindrome" if lst == lst[::-1] else f"The list {lst} is not a palindrome")