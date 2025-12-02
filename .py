import random
import string

def generate_password():
    print("\n----- Random Password Generator -----")
    
    length = int(input("Enter password length: "))
    
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    
    characters = string.ascii_lowercase  # always included
    
    if include_upper:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("❌ No character sets selected!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    
    print(f"\nGenerated Password: {password}\n")

generate_password()
