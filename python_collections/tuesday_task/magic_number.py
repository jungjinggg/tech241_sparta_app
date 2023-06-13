# Magic number game

import random

# Set magic number
magic_num = random.randint(1, 100)
# print(magic_num)

# Ask the user for a guess
guessed_num = int(input("Enter a number between 1 - 100: "))

# Check if user's guess was correct
if guessed_num == magic_num:
    print("Congratulation! You've guessed correctly")
    #break
elif guessed_num < magic_num:
    print("The number is too low")
    #continue
elif guessed_num > magic_num:
    print("The number is too high")
    #continue
else:
    print("Unfortunately! You've got it wrong this time")
    #break

# Give them the result
print(f'\nThe magic number is {magic_num}')

