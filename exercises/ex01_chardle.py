"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730401487"

user_word: str = input("Enter a 5-character word: ")
if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

user_char: str = input("Enter a single character: ")
if len(user_char) != 1:
    print("Error: Character must be a single character")
    exit()

print("Searching for " + user_char + " in " + user_word)

matching_char: int = 0

if user_word[0] == user_char:
    print(user_char + " found at index 0")
    matching_char = matching_char + 1
if user_word[1] == user_char:
    print(user_char + " found at index 1")
    matching_char = matching_char + 1
if user_word[2] == user_char:
    print(user_char + " found at index 2")
    matching_char = matching_char + 1
if user_word[3] == user_char:
    print(user_char + " found at index 3")
    matching_char = matching_char + 1
if user_word[4] == user_char:
    print(user_char + " found at index 4")
    matching_char = matching_char + 1

if matching_char == 1: 
    print(str(matching_char) + " instance of " + user_char + " found in " + user_word)
else:
    if matching_char == 0:
        print("No instances of " + user_char + " found in " + user_word)
    else:
        if matching_char > 1:
            print(str(matching_char) + " instances of " + user_char + " found in " + user_word)