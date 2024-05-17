import random
from score import Score
from User_Manager import UserManager

class Game:
    def __init__(self, username):
        self.username = username
        self.stage = 1
        self.player_score = 0
        self.computer_score = 0
        self.stages_won = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def play_round(self):
        player_roll = self.roll_dice()
        computer_roll = self.roll_dice()
        print(f"\nYour roll: {player_roll}, CPU roll: {computer_roll}")
        if player_roll > computer_roll:
            return "You win this round!"
        elif player_roll < computer_roll:
            return "You lose this round."
        else:
            return "It's a tie!"

    def play_stage(self):
        player_wins = 0
        computer_wins = 0
        print(f'\nStage {self.stage}:')
        for _ in range(3):
            result = self.play_round()
            print(result)
            if result == "You win this round!":
                self.player_score += 1
                player_wins += 1
            elif result == "You lose this round.":
                computer_wins += 1
            

        if player_wins > computer_wins:
            self.player_score += 3
            self.stages_won += 1
            print(f"\nStage {self.stage} Winner: {self.username}")
            self.stage += 1
            return True
        elif player_wins == computer_wins:
            print(f"\nStage {self.stage} Winner: None")
            return False
        else:
            print(f"\nStage {self.stage} Winner: CPU")
            return False

    def play_game(self):
        while True:
            win = self.play_stage()
            if win is False:
                self.display_result()
                UserManager.ask()
                break

            print(f"\nYour score: {self.player_score}, Stages won: {self.stages_won}")
            choice = input("\nEnter 1 to continue to the next stage or 0 to stop: ")
            if choice == "0":
                self.display_result()
                print("\nGame ended.")
                UserManager.ask()
                break
            elif choice != "1":
                print("\nInvalid choice. Game will end.")
                self.display_result()
                UserManager.ask()
                break

    def display_result(self):

        if self.player_score > 0:
                print(f"\nGame over. Your final score: {self.player_score}, Stages won: {self.stages_won}")
                Score.save_scores(self.username, self.player_score, self.stages_won)
        elif self.stages_won == 0:
            print(f"\nGame over. Your final score: {self.player_score}, Stages won: {self.stages_won}")
