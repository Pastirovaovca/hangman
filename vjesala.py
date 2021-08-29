import os
import getpass

def hangman_0():
    print('_______')
    print('       ')
    print('       ')
    print('       ')

def hangman_1():
    print('_______')
    print('   O   ')
    print('       ')
    print('       ')

def hangman_2():
    print('_______')
    print('   O   ')
    print('   |   ')
    print('       ')

def hangman_3():
    print('_______')
    print('   O   ')
    print('   |   ')
    print('  /    ')

def hangman_4():
    print('_______')
    print('   O   ')
    print('   |   ')
    print('  / \  ')

def hangman_5():
    print('_______')
    print('  \O   ')
    print('   |   ')
    print('  / \  ')

def hangman_6():
    print('_______')
    print('  \O/  ')
    print('   |   ')
    print('  / \  ')

def hangman_7():
    print('_______')
    print('   O_| ')
    print('  /|\  ')
    print('  / \  ')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

game = True

while game:

    clear()
    term = list(getpass.getpass('Upiši pojam za pogađanje: ').upper())
    clear()
    hidden_term = ''
    for char in term:
        if char == ' ':
            hidden_term += ' '
        elif char != ' ':
            hidden_term += '•'

    hangman_0()
    print(hidden_term)
    game_on = True
    wrong_guesses = 0

    while game_on:

        guess = input('Pogodi slovo! ')

        while True:
            if len(guess) > 1:
                guess = input('Upiši samo jedno slovo! ')
            else:
                break

        clear()
        for i in range(len(term)):
            if guess.upper() == ''.join(term[i]):
                hidden_term = list(hidden_term)
                hidden_term[i] = guess.upper()

        if guess.upper() not in ''.join(term):
            if wrong_guesses == 6:
                hangman_7()
                print('Jaoooooo!')
                game_on = False
                break
            else:
                wrong_guesses += 1

        if '•' not in hidden_term:
            print(''.join(term))
            print('Bravo!')
            game_on = False
            break

        board = vars()[f'hangman_{wrong_guesses}']()
        hidden_term = ''.join(hidden_term)
        print(hidden_term)

    replay = True
    while replay:
        print('\n')
        new_game = input('Enter za novu igru\nBilo koja druga tipka za kraj')
        if new_game == '':
            replay = False
        elif new_game != '':
            clear()
            game = False
            break
