import random
import string

def password_generator():
    length = int(input("Enter the desired password lenght: "))
    if length < 4:
        print("The password length must be greater than 4.")
        return
    include_uppercase = input("Include the uppercase letter? (yes/no): ").lower().strip()
    include_digit = input("Include digits? (yes/no): ").lower().strip()
    include_special = input("Include special characters? (yes/no): ").lower().strip()

    
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase == "yes" else " "
    special = string.punctuation if include_special == "yes" else " "
    digits = string.digits if include_digit == "yes" else " "

    all_characters = lower + upper + special + digits
    
    required_character = []
    if include_uppercase == "yes":
        required_character.append(random.choice(upper))
    if include_special == "yes":
        required_character.append(random.choice(special))
    if include_digit == "yes":
        required_character.append(random.choice(digits))

    remaining_characters = length - len(required_character)
    password = required_character

    for _ in range(remaining_characters):
        charcter = random.choice(all_characters)
        password.append(charcter)

    random.shuffle(password)

    str_password = "".join(password)
    return str_password

password = password_generator()
print(password)