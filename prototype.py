WORD = 'KAAKE'

for guess_num in range(1, 7):
    guess = input(f'\nGuess {guess_num}: ').upper()
    if guess == WORD:
        print('Correct')
        break

    correct_letters = {
        letter for letter, correct in zip(guess, WORD) if letter == correct
        }
    misplaced_letters = set(guess) & set(WORD) - correct_letters
    wrong_letters = set(guess) - set(WORD)

    print(f'Correct letters: {", ".join(correct_letters)}')
    print(f'Misplaced letters: {", ".join(misplaced_letters)}')
    print(f'Wrong letters: {", ".join(wrong_letters)}')