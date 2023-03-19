input_string = input("Enter a string: ")

reverse_string = input_string[::-1]

if input_string == reverse_string:
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")
