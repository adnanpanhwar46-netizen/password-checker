password = input("Enter your password: ")

has_min_length = len(password) >= 8
has_number = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)

if has_min_length and has_number and has_upper:
    print("Strong Password")
else:
    print("Weak Password")
