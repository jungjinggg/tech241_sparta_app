# Magic number game

import random

# Set magic number
magic_num = random.randint(1, 100)
# print(magic_num)

# Check if user's guess was correct
guess_limit = 3
counter = 0
while counter < guess_limit:
    try:
        guessed_num = int(input("Enter a number between 1 - 100: "))
    except ValueError:
        print("Please enter a number")
        break

    counter += 1
    if guessed_num == magic_num:
        print("Congratulation! You've guessed correctly")
        print(f'\nThe magic number is {magic_num}')
        break

    elif guessed_num < magic_num:
        print("The number is too low")
        continue
    elif guessed_num > magic_num:
        print("The number is too high")
        continue

else:
    print("\nYou've run out of guesses!")
    print(f"The magic number is {magic_num}")



