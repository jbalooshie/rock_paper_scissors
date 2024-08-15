import random
import time

def play_game():
    selection = ''
    player_score = 0
    computer_score = 0
    while selection != 'Exit':
        time.sleep(1)
        print(f'Current score is Player: {player_score} Computer: {computer_score}.')
        time.sleep(1)
        selection = input('Please make your selection.\n')
        choices = ('Rock', 'Paper', 'Scissors')
        cpu_selection = choices[random.randint(0,2)]
        if selection == 'Exit':
            time.sleep(1)
            print('Thanks for playing!')
            time.sleep(1)
            return 'Exit'
        elif selection not in choices:
            time.sleep(1)
            print("Invalid selection. Please choose Rock, Paper, or Scissors.")
        else:
            time.sleep(1)
            print('Rock...')
            time.sleep(1)
            print('Paper...')
            time.sleep(1)
            print('Scissors...')
            time.sleep(1)
            print('Shoot!')
            time.sleep(1)
            print(f'Player throws {selection}!')
            time.sleep(1)
            print(f'Computer throws {cpu_selection}!')
            time.sleep(1)
            if selection == cpu_selection:
                print(f'Both chose {selection}. Tie!')
            elif selection == 'Scissors' and cpu_selection == 'Paper':
                print('Scissors cuts Paper. You win!')
                player_score += 1
            elif selection == 'Paper' and cpu_selection == 'Rock':
                print('Paper covers Rock. You win!')
                player_score += 1
            elif selection == 'Rock' and cpu_selection == 'Scissors':
                print('Rock crushes scissors. You win!')
                player_score += 1
            elif selection == 'Scissors' and cpu_selection == 'Rock':
                print('Rock crushes scissors. Computer wins!')
                computer_score += 1
            elif selection == 'Paper' and cpu_selection == 'Scissors':
                print('Scissors cuts Paper. Computer wins!')
                computer_score += 1
            elif selection == 'Rock' and cpu_selection == 'Paper':
                print('Paper covers Rock. Computer wins!')
                computer_score += 1

if __name__ == "__main__":
    status = ''
    while status != 'Exit':
        print('Hello! Welcome to Rock, Paper, Scissors.')
        time.sleep(1)
        print("Type 'Exit' to quit the game.")
        time.sleep(1)
        print("When prompted, choose 'Rock', 'Paper', or 'Scissors'.")
        time.sleep(3)
        status = play_game()