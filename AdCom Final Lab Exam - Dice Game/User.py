from User_Manager import UserManager
from Dice_Game import Game
from score import Score

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def main_menu(self):
        while True:
            try:
                print()
                print('Menu:')
                print('\n(1) Register')
                print('(2) Log In')
                print('(3) Exit')

                choice = input('\nChoose an option: ')
                if not choice:
                    continue
                choice = int(choice)
                if choice == 1:
                    self.register()
                elif choice == 2:
                    self.login()
                elif choice == 3:
                    exit()
                else:
                    print('\nInvalid input. Please enter an option from the menu.')
            except ValueError as e:
                print(f'\nError: {e} Invalid input. Please enter an integer.')

    def register(self):
        print('\nRegister:')
        self.username = input('\nEnter a username: ').strip()
        if not self.username:
            self.main_menu()
        else:
            while len(self.username) < 4:
                print('\nUsername must be at least 4 characters long.')
                self.register()
                break

        if UserManager.validate_username(self.username):
            print('\nUsername already taken.')
            self.register() 

        self.password = input('Enter a password: ').strip()
        if not self.password:
            self.main_menu()
        while len(self.password) < 8:
            print('\nPassword must be at least 8 characters long.')
            self.password = input('\nEnter a password: ').strip()
            if not self.password:
                self.main_menu()

        UserManager.save_users(self.username, self.password)
        print(f'\nRegistration Successful!')
        self.login()

    def login(self):
        print('\nLog-In:')
        self.username = input('\nEnter your username: ')
        if not self.username:
            self.main_menu()
        elif not UserManager.validate_username(self.username):
            print('\nUsername does not exist.')
            self.login()
        else:
            self.password = input('Enter your password: ')
            if not self.password:
                self.main_menu()
            elif not UserManager.validate_password(self.username, self.password):
                print('\nIncorrect password.')
                self.login()
            else:
                print(f'\nLog-in successful!')
                self.game_menu()

    def game_menu(self):
        while True:
            print()
            print(f'Welcome to Dice Game {self.username}!')
            print('\n(1) Start Game')
            print('(2) View Top Scores')
            print('(3) Log-Out')
            try:
                choice = input('\nChoose an option: ')
                if not choice:
                    self.main_menu()
                    break
                choice = int(choice)
                if choice == 1:
                    game = Game(self.username)
                    game.play_game()
                elif choice == 2:
                    top_scores = Score.load_top_scores() 
                    print('\nTop Scores:')
                    print(top_scores)
                    UserManager.ask()
                elif choice == 3:
                    self.main_menu()
                    break
                else:
                    print('\nInvalid input. Please enter an option from the menu.')
            except ValueError:
                print('\nInvalid input. Please enter an integer.')

