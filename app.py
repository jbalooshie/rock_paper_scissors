def main_menu():
    while True:
        print('Hello! Welcome to rock, paper, scissors. Type "New" to start a new game. Type "Exit" to exit.')
        menu_choice = input()
        if menu_choice == 'New':
            play_game()
        elif menu_choice == 'Exit':
            return print('Goodbye')
        else:
            print('Invalid selection. Please choose "New" or "Exit".')

def play_game():
    selection = ''
    while selection != 'Exit':
        selection = input('Please make your selection.')
        cpu_selection = 'Rock'
        if selection == 'Paper':
            print('Paper covers Rock. You win!')
        elif selection == 'Rock':
            print('Both chose Rock. Tie!')
        elif selection == 'Scissors':
            print('Rock beats scissors. You lose!')
        elif selection == 'Exit':
            print('Thanks for playing!')
            return False
        else:
            print("Invalid selection. Please choose Rock, Paper, or Scissors.")

main_menu()