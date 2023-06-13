# Magic number game

# Set magic number
magic_num = 21

# Ask the user for a guess
guessed_num = int(input("Enter a number between 1 - 50: "))

# Check if user's guess was correct
if guessed_num == magic_num:
    print("Congratulation! You've guessed correctly")
else:
    print("Unfortunately! You've got it wrong this time")

# Give them the result
print(f'\nThe magic number is {magic_num}')

