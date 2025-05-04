#print("Palindrome" if (n := input()) == n[::-1] else "Not a palindrome")
print((s := input("Enter a string: ")) + (" is a palindrome" if s == s[::-1] else " is not a palindrome"))