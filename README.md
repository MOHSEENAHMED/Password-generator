This is a simple Python-based Password Generator that allows users to create secure and customizable passwords. The user can specify the password length and choose whether to include:
1. Uppercase Letters
2. Digits (Numbers)
3. Special Characters (Symbols like @, #, $)

The program ensures that if the user selects any of these options, at least one character from each chosen category is included. The rest of the password is randomly generated from the selected character set.

Features
1. Generates strong and random passwords
2. Allows users to customize password length
3. Ensures that at least one uppercase, digit, or special character is included if selected
4. Uses random.shuffle() to ensure password randomness

How It Works
The user inputs the desired password length (must be greater than 4).
The user selects whether to include:
  1. Uppercase letters (A-Z)
  2. Digits (0-9)
  3. Special characters (!, @, #, etc.)
The program ensures that at least one selected character type is included.
The password is generated and shuffled to enhance security.
The final password is displayed on the screen.
