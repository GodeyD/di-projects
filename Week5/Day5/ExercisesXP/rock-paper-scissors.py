from game import *

def get_user_menu_choice():
    for _ in range(1):
        selction = input('Select choice number:\n1.-Play a new game\n2.-Show scores\n3.-Quit\nchouse 1, 2 or 3: ')
        select = int(selction)
        print(select)
        return(select)
     

def print_results(results= dict):
    print(f'The results are:\nWins: {results[list(results)[0]]} \nLoses: {results[list(results)[1]]}\nDraws: {results[list(results)[2]]}\n')

def main():    
    get_user_menu_choice()
    
    if get_user_menu_choice() == 1:
        new_game = Game()
        new_game.play()
        main()
    elif get_user_menu_choice() == 2:
        print_results(Game.scores)
        main()
    else:
        print_results(Game.scores)
        print('Tks for playing')

main()