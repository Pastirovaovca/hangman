import os
import getpass
from time import sleep


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


clear()
print('\n')
hello = '    V J E Š A L A   '
for i in range(20):
    print(hello[i], end=' ', flush=True); sleep(0.2)

game = True

while game:

    while True:
        clear()
        term = list(getpass.getpass('Upiši pojam za pogađanje: ').upper())
        start = input('\nZa nastavak pritisni Enter\nZa novi unos bilo koju drugu tipku: ')
        if start == '':
            break

    clear()
    hidden_term = ''
    for char in term:
        if char == ' ':
            hidden_term += ' '
        elif char != ' ':
            hidden_term += '•'

    hangman_0()
    print(hidden_term)

    wrong_guesses = 0
    tried_guesses = []
    game_on = True

    while game_on:

        guess = input('Pogodi slovo! ').upper()

        while True:
            if len(guess) > 1:
                guess = input('Upiši samo jedno slovo! ').upper()
            elif guess == '':
                guess = input('Prije Entera upiši slovo! ')
            elif guess in tried_guesses:
                guess = input('Slovo već upotrijebljeno, probaj drugo! ').upper()
            else:
                break

        tried_guesses.append(guess)

        clear()
        for i in range(len(term)):
            if guess.upper() == ''.join(term[i]).upper():
                hidden_term = list(hidden_term)
                hidden_term[i] = guess.upper()

        if guess.upper() not in ''.join(term).upper():
            if wrong_guesses == 6:
                hangman_7()
                print('\nJaoooooo!')
                print('\nRješenje je:\n' + ''.join(term))
                game_on = False
                break
            else:
                wrong_guesses += 1

        if '•' not in hidden_term:
            print('Rješenje je:\n' + ''.join(term))
            print('\nBravo!')
            game_on = False
            break

        board = vars()[f'hangman_{wrong_guesses}']()
        hidden_term = ''.join(hidden_term)
        print(hidden_term)

    replay = True
    while replay:
        print('\n')
        new_game = input('Enter za novu igru\nBilo koja druga tipka za kraj ')
        if new_game == '':
            replay = False
        elif new_game != '':
            clear()
            game = False
            break
