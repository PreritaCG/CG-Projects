# Function to check if a character is an alphabet
def is_alphabet(char):
    if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
        print(f"'{char}' is an alphabet.")
    else:
        print(f"'{char}' is not an alphabet.")
# Get user input

character = input("Enter a character: ")

is_alphabet(character)