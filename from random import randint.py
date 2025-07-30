from random import randint

number = randint(1, 100)
guess_list = []

print('Welcome to "Guess the Number"! 🎲')
print('Try to guess the random number between 1 and 100. Good luck!')

# Function for getting a valid user input
def get_user_input():
    while True:
        try:
            return int(input('What number do you think it is? '))
        except ValueError:
            print('Please enter a valid whole number!')

while True:
    guess = get_user_input()

    if guess == number:
        print('You got it – awesome!! 🎉')
        total_attempts = len(guess_list) + 1
        if total_attempts == 6:
            print('You needed 6 attempts – not bad, but could be better.')
        elif total_attempts > 6:
            print(f'That could have been faster – you needed {total_attempts} attempts.')
        else:
            print(f'Wow, you did it in {total_attempts} attempts – that\'s quick!!')
        break

    elif guess > number:
        print('The number is smaller.')
    else:
        print('The number is bigger.')

    guess_list.append(guess)

input('\nPress Enter to exit...')