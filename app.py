import random

def main_menu():
    status = ''
    while status != 'Exit':
        print('Hello! Welcome to rock, paper, scissors.')
        status = play_game()

def play_game():
    selection = ''
    while selection != 'Exit':
        selection = input('Please make your selection.')
        choices = ('Rock', 'Paper', 'Scissors')
        cpu_selection = choices[random.randint(0,2)]
        if selection == cpu_selection:
            print(f'Both chose {selection}. Tie!')
        elif selection == 'Scissors' and cpu_selection == 'Paper':
            print('Scissors cuts Paper. You win!')
        elif selection == 'Paper' and cpu_selection == 'Rock':
            print('Paper covers Rock. You win!')
        elif selection == 'Rock' and cpu_selection == 'Scissors':
            print('Rock cruches scissors. You win!')
        elif selection == 'Scissors' and cpu_selection == 'Rock':
            print('Rock crushes scissors. Computer wins!')
        elif selection == 'Paper' and cpu_selection == 'Scissors':
            print('Scissors cuts Paper. Computer wins!')
        elif selection == 'Rock' and cpu_selection == 'Paper':
            print('Paper covers Rock. Computer wins!')
        elif selection == 'Exit':
            print('Thanks for playing!')
            return 'Exit'
        else:
            print("Invalid selection. Please choose Rock, Paper, or Scissors.")

main_menu()