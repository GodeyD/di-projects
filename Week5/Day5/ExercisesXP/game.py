import random

class Game():
    
    def get_user_item(self):
        i_user =  input('choose one, Rock, Paper, Scissors: ')
        item_user = (str(i_user)).lower()
        while item_user != 'rock' and item_user != 'paper' and item_user != 'scissors':
            print('plz, select beetwin: Rock, Paper, Scissors')
            i_user =  input('choose one, Rock, Paper, Scissors: ')
            item_user = (str(i_user)).lower()
        else:
            return item_user

    def get_computer_item(self):
        i_pc = ['rock', 'paper', 'scissors']
        item_pc = random.choice(i_pc)
        return item_pc

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 'Draw'
        if user_item == 'rock' and computer_item == 'paper':
            return 'Loss'
        if user_item == 'rock' and computer_item == 'scissors':
           return 'Win'
        if user_item == 'paper' and computer_item == 'scissors':
            return 'Loss'
        if user_item == 'paper' and computer_item == 'rock':
           return 'Win'
        if user_item == 'scissors' and computer_item == 'rock':
            return 'Loss'
        if user_item == 'scissors' and computer_item == 'paper':
           return 'Win'


    def play(self):
        user = yo.get_user_item()
        pc = yo.get_computer_item()
        result = yo.get_game_result(user, pc)
        print(f'You selected {user}. The computer selected {pc}. You {result}')
        return result





