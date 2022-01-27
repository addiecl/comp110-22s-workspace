"""EX02 - Creating a one shot Wordle."""

__author__ = "730401487"


secret_word: str = "python"
secret_length: int = len(secret_word)
user_guess: str = input(f"What is your {secret_length}-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(user_guess) != len(secret_word):
    user_guess = input(f"That was not {secret_length} letters! Try again: ")

i: int = 0
emoji_guess: str = ("")

while i < len(secret_word):
    if user_guess[i] == secret_word[i]:
        emoji_guess = emoji_guess + GREEN_BOX
    else:
        alt_idx: int = 0
        chr_exists: bool = False
        while not chr_exists and alt_idx < len(secret_word):
            if user_guess[i] == secret_word[alt_idx]:
                chr_exists = True
            else:
                alt_idx = alt_idx + 1
        if chr_exists:
            emoji_guess = emoji_guess + YELLOW_BOX
        else:
            emoji_guess = emoji_guess + WHITE_BOX
    i = i + 1

print(emoji_guess)
if user_guess == secret_word:
    print("Woo! You got it!")
if user_guess != secret_word:
    print("Not quite. Play again soon!")