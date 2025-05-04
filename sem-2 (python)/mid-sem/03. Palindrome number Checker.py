n = input("Enter a number: ")
print(n + (" is a palindrome" if n.isdigit() and n == n[::-1] else " is not a palindrome number"))